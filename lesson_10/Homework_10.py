import csv

# Task 1
from lesson_10 import dog_to_human_years
from lesson_10 import toss_a_coin

print(dog_to_human_years(3))
print(toss_a_coin())

# Task 2


def get_domains_list(file) -> list:
    domains_list = []
    with open(file) as file:
        for item in file.readlines():
            if '.' in item:
                item = item.replace('.', '')
            if '\n' in item:
                item = item.replace('\n', '')
            domains_list.append(item)
    return domains_list


print(f'Task_2: {get_domains_list('domains.txt')}')

# Task 3


def get_last_name(file) -> list:
    last_name_list = []
    with open(file) as file:
        for item in file.readlines():
            item = item.split(',')
            last_name_list.append(item[1].strip())
    return last_name_list


print(f'Task_3: {get_last_name('names.txt')}')

# Task 4


def get_date(file) -> list:
    date_list = []
    with open(file) as file:
        for row in file.readlines():
            date_dict = {}
            if '-' in row:
                row = row.split('-')
                date_dict['date'] = row[0].strip()
                date_list.append(date_dict)
    return date_list

# 1 дата - не содержит число, если цель достать только дату с числом,
# я бы использовал re ('[0-9]\w+\s\w+\s[0-9]{4}')


print(f'Task_4: {get_date('authors.txt')}')

# Task 5
test_data = [[1, 'Wendy Wallace'], [2, 'Walter Burgess'], [3, 'Carlton Chavez']]


def write_csv(file, rows):
    with open(file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def read_csv(file):
    with open(file) as file:
        reader = csv.reader(file)
        return list(reader)


write_csv('persons.csv', test_data)
current_csv = read_csv('persons.csv')

print(f'Task_5: {current_csv}')

current_csv.append([4, 'Shelia Hogan'])
current_csv.append([5, 'Kerry Marshall'])

write_csv('updated_persons.csv', current_csv)





