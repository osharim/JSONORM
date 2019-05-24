# encoding: utf-8


class QuerySet(object):
    """
    Creates a connection new to specific <JSON file> provided
    """

    def __init__(self, objects, ):
        """
        file: system path of our current JSON file. 
        """
        self._objects = objects
        self._filtered_objects = objects

    def all(self):
        """
        List entirely our queryset _object
        return <Objects> 
        """
        return self._objects

    def count(self):
        """
        Count objects in a queryset 
        return <Type Integer> 
        """
        return len(self._filtered_objects)

    def filter(self, *args, **kwargs):
        """
        Filter by keyworded argument: <Actor, Genre>

        e.g
        movies.queryset.filter(actors=['Ryan Reynolds', 'William Ackman']
        """
        self._filtered_objects = []
        for property, value in kwargs.items():
            self._filtered_objects = list(filter(lambda data: any(
                elem in value for elem in data[property]), self._objects))

        return self._filtered_objects

    def group_by(self, property):
        """
        Classify information through a group by system.
        Group elements by <property>

        e.g
        movies.queryset.group_by('actors')

        return: [{'grouped_by_actors': 'Woody Harrelson', results: [<Movie with this author in cast>, <Movie with this author in cast>, ... ]}]


        """
        # Check if property is a List or a String to build a Group output
        # Return all data from a specific List
        # eg. if property == 'actors' Will return all actors in this DB

        grouped_values = [item for sublist in map(
            lambda data: data[property], self._objects) for item in sublist]

        # Unique values through Set structure
        unique_grouped_values = list(set(grouped_values))

        # Group db by unique grouped values.
        # ej. 'Michael Shannon' will  be the property containing a List of objects related to it.

        self._filtered_objects = []

        # dynamic property name eg. grouped_by_genre, grouped_by_actors
        property = 'group_by_{0}'.format(property)

        grouped_bundle = []

        for value in unique_grouped_values:
            results = self.filter(actors=[value])
            bundle_results = {}
            bundle_results[property] = value
            bundle_results['results'] = results
            grouped_bundle.append(bundle_results)

        self._filtered_objects = grouped_bundle
        return self._filtered_objects

    def order_by(self, property):
        """
        Order elements by a property given
        e.g
        movies.queryset.order_by('ratings')

        return: [<Movie ordered by rating>, <Movie ordered by rating>,
                     <Movie ordered by rating>, ..., <Movie ordered by rating>  ]

        """

        # if the value is a Integer, then, order through a Integer; otherwise perform a sum to
        # return an Integer an then order this List using this integer
        elements_to_order = []
        for element in self._objects:
            sum_property = 0
            if isinstance(element[property], list):
                sum_property = sum(element[property])
            else:
                sum_property = element[property] or 0
            element['__sum__'] = sum_property
            elements_to_order.append(element)

        return sorted(
            elements_to_order, key=lambda element: element['__sum__'], reverse=True)
