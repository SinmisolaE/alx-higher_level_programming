#!/usr/bin/python3
""" Define class Base """
import csv
import json


class Base:
    """ Contain attributes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list = []
                for i in list_objs:
                    list.append(i.to_dictionary())
                f.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """ converts from json string to object """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        try:
            with open(file, 'r') as f:
                list = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in csv """
        file = cls.__name__ + ".csv"
        with open(file, 'w', newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in csv """
        file = cls.__name__ + ".csv"
        try:
            with open(file, 'r', newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                dict_list = csv.DictReader(f, fieldnames=fieldnames)
                dict_list = [dict([k, int(v)] for k, v in d.items())
                             for d in dict_list]
                return [cls.create(**d) for d in dict_list]
        except IOError:
            return []
