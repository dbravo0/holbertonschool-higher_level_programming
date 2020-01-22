#!/usr/bin/python3
class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        d = {}
        for i in attrs:
            try:
                d[i] = self.__dict__[i]
            except:
                continue

        return d

    def reload_from_json(self, json):
        for key, val in json.items():
            self.__dict__[key] = val
