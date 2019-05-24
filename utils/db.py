# encondig: utf-8
import json
from .query import QuerySet


class Connection:
    """
    Creates a connection new to specific <JSON file> provided
    """

    def __init__(self, file, ):
        """
        file: system path of our current JSON file. 
        """
        self.file = file
        self.connect()

    def connect(self,):
        """
        Read and parse our json file into a valid JSON data type 
        """

        _objects = []
        with open(self.file, "r") as read_io:
            _objects = json.load(read_io)
            self.queryset = QuerySet(_objects)

