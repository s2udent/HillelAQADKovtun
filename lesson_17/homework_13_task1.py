import csv
import json


# Task 1
class JSONConverter:
    def __init__(self):
        self.__lines = None

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            '''Перевизначення, після якого не треба робити cleanup'''
            self.__lines = json.load(json_file)
            print(self.__lines)

    def get_keys(self):
        return [key for key in self.__lines[0]]

    def write_file(self, filename: str):
        headers = self.get_keys()
        with open(filename, 'w') as writer:
            csv_writer = csv.DictWriter(writer, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(self.__lines)


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example_task1.csv')
converter.read_file('example.json')
converter.write_file('example.csv')
