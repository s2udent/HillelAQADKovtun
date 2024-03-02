import csv

test_row = ['Dima', 'Kovtun', 15, 'Male', 1234]


class ActionsWithCSV:

    def __init__(self):
        self.__lines = []

    def _fill_list(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                self.__lines.append(line)

    def cleanup(self):
        self.__lines = []

    def add_row(self, filename: str, row: list):
        self._fill_list(filename)
        with open(filename, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            self.__lines.append(row)
            writer.writerows(self.__lines)
        self.cleanup()

    def del_row(self, filename: str, remove_row_index=-1):
        self._fill_list(filename)
        with open(filename, 'w') as file:
            writer = csv.writer(file, delimiter=',')
            self.__lines.pop(remove_row_index)
            writer.writerows(self.__lines)
        self.cleanup()

# csv_actions = ActionsWithCSV()
# csv_actions.add_row('example.csv', test_row)
# csv_actions.del_row('example.csv')


