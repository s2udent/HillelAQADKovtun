from random import randint, choice

if __name__ == '__main__':
    # Task 1

    num_list1 = [3, 7, 5, 6, 1]
    num_list2 = [10, 5, 8, 7, 3]


    def find_intersec(list1, list2):
        intersection_list = list(set(list1).intersection(set(list2)))
        return sorted(intersection_list)

    print('Task_1:', find_intersec(num_list1, num_list2))

    # Task 2

    students_dict = {'Alex': randint(1, 5),
                    'Mark': randint(1, 5),
                    'Tolik': randint(1, 5),
                    'John': randint(1, 5),
                    'Joana': randint(1, 5)}

    print('Task_2: dict_example', students_dict)

    def calk_medium_mark(dictionary) -> float:
        v = dictionary.values()
        medium_mark = sum(list(v)) / len(list(v))
        return medium_mark


    def find_top_students(dictionary) -> str:
        names = ''
        for k, v in dictionary.items():
            if v > calk_medium_mark(dictionary):
                names = names + ' ' + k
        names = names.strip().replace(' ', ', ')
        return names


    print('Task_2: Medium mark:', calk_medium_mark(students_dict))
    print('Task_2: Student names:', find_top_students(students_dict))

    # Task 3

    name = ['Lyla', 'Parker', 'Dorian', 'Felix', 'Russell']
    surname = ['Norris', 'Clarke', 'Wyatt', 'Delarosa', 'McCarthy']
    location = ['Geneve', 'White City', 'San Pablo', 'Kathmandu', 'New York']

    def generate_person_location(name_list, surname_list, location_list) -> dict:
        person_location = {'name': choice(name_list),
                           'surname': choice(surname_list),
                           'location': choice(location_list)}
        return person_location

    print(f'Task_3:', generate_person_location(name, surname, location))
    print(f'Task_3:', generate_person_location(name, surname, location))



