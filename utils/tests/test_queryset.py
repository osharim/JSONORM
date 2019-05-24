# encoding: utf-8
import pytest
from ..db import Connection


class TestQuerySet:

    def test_higher_ranked_by_popularity(self):
        """
        Test our Ranking based on popularity. We use 'ratings' as a popularity metric. 

        We perform this query and match againts our highest know value which is '211' rating scored.  
        """

        movies = Connection('movies-database-v2.json')

        ordered_by_popularity = movies.queryset.order_by('ratings')[0]

        assert ordered_by_popularity['__sum__'] == 211

    def test_lower_ranked_by_popularity(self):
        """
        Test our Ranking based on popularity AKA 'rantings'.

        We perform this query and match againts our lower know value which is '139' rating scored.  
        """

        movies = Connection('movies-database-v2.json')

        ordered_by_lower_popularity = movies.queryset.order_by('ratings')[-1]

        assert ordered_by_lower_popularity['__sum__'] == 139

    def test_ordered_by_imdb_rating(self):
        """
        Test our ordering query againts IMDB rating, our test must be ensure that our higher ranked movie is "Logan" with 9.5 score
        """

        movies = Connection('movies-database-v2.json')
        ordered_by_imdb_rating = movies.queryset.order_by('imdbRating')[:1]

        # Logan: The Wolverine is our top IMDB Rated movie with a 9.5.
        assert ordered_by_imdb_rating[0]['__sum__'] == 9.5

    def test_classification_by_actors(self):
        """
        Test our actor classification through a Group By Method
        """

        movies = Connection('movies-database-v2.json')

        classified_by_actors = movies.queryset.group_by('actors')

        # There are 93 unique actors in this JSON File.
        assert len(classified_by_actors) == 93

    def test_filter_by_actors(self):
        """
        Test our Filter Method, ensure we return only two results with this two authors
        """

        movies = Connection('movies-database-v2.json')

        classified_by_actors = movies.queryset.filter(
            actors=['Ryan Reynolds', 'William Ackman'])

        assert len(classified_by_actors) == 2

    def test_filter_by_genre(self):
        """
        Test our Filter Method by genre
        """

        movies = Connection('movies-database-v2.json')

        classified_by_genres = movies.queryset.filter(
            genres=['Horror', 'Sci-Fi'])

        # There are only 6 movies with ['Horror', 'Sci-Fi'] as an attribue.
        assert len(classified_by_genres) == 6
