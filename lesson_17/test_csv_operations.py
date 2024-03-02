from lesson_17.homework_13_task2 import ActionsWithCSV

file_name = 'example.csv'


class TestCSVOperations:

    def get_num_of_rows(self):
        with open(file_name, 'r') as file:
            num_of_rows = len(file.readlines())
        return num_of_rows

    def test_inserting(self):
        num_of_rows1 = self.get_num_of_rows()
        csv_actions = ActionsWithCSV()
        csv_actions.add_row(file_name, ['Josie', 'Miller', 30, 'F', 4500])
        num_of_rows2 = self.get_num_of_rows()
        assert num_of_rows2 == num_of_rows1+1

    def test_removing(self):
        num_of_rows1 = self.get_num_of_rows()
        csv_actions = ActionsWithCSV()
        csv_actions.del_row('example.csv', )
        num_of_rows2 = self.get_num_of_rows()
        assert num_of_rows2 == num_of_rows1-1
