#!/usr/bin/python3

import json
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of the Base class with an optional ID.

        Args:
            id (int, optional): An optional unique identifier for the instance.
                If not provided, a new ID will be generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representing the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be serialized and saved to a file.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string into a list of dictionaries.

        Args:
            json_string (str): A JSON string to be parsed.

        Returns:
            list: A list of dictionaries extracted from the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class with attributes initialized from a dictionary.

        Args:
            **dictionary: A dictionary containing attribute-value pairs.

        Returns:
            Base: An instance of the class with attributes set based on the provided dictionary.
        """
        default_size = 1 if cls.__name__ != "Rectangle" else (1, 1)
        dummy = cls(*default_size)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                obj_list = cls.from_json_string(file.read())
                return [cls.create(**obj_dict) for obj_dict in obj_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be serialized and saved to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if not list_objs:
                file.write("[]")
            else:
                fieldnames = cls._get_csv_fieldnames()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: A list of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                fieldnames = cls._get_csv_fieldnames()
                csv_data = csv.DictReader(file, fieldnames=fieldnames)
                csv_data = [dict([(k, int(v)) for k, v in d.items()]) for d in csv_data]
                return [cls.create(**d) for d in csv_data]
        except IOError:
            return []

    @staticmethod
    def _get_csv_fieldnames():
        """
        Get the appropriate fieldnames for CSV based on the class name.

        Returns:
            list: A list of fieldnames for CSV data, specific to the class name.
        """
        if Base.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        def draw_shape(shape, color):
            turt.color(color)
            for obj in shape:
                turt.showturtle()
                turt.up()
                turt.goto(obj.x, obj.y)
                turt.down()
                for _ in range(2):
                    turt.forward(obj.width)
                    turt.left(90)
                    turt.forward(obj.height)
                    turt.left(90)
                turt.hideturtle()

        draw_shape(list_rectangles, "#ffffff")
        draw_shape(list_squares, "#b5e3d8")

        turtle.exitonclick()
