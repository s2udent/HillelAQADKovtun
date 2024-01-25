
if __name__ == '__main__':
    # Task 1

    num_list1 = [3, 7, 5, 6, 1]
    num_list2 = [10, 5, 8, 7, 3]

    intersection_lambda = lambda list1, list2: list(set(list1).intersection(set(list2)))

    print(intersection_lambda(num_list1, num_list2))

    # Task 2

    test_str = '-55366'

    str_is_digit_labda = lambda string: string.isdigit() or string.startswith('-') and string.split('-')[1].isdigit()

    print(str_is_digit_labda(test_str))

    # Task 3

    num_list10 = [1, 7, 5, 6]
    num_list11 = [10, 5, 8, 7, 3, 14, 16]
    num_list12 = [10, 5, 8, 7, 3, 5, 8, 99, 90, 76]
    num_list13 = [10, 5, 8, 7, 3, 5, 8, 99, 90, 76, 55, 66]

    max_min_len_lamblda = lambda *args: (item for item in args if (len(item)) in
                                         [min(list((len(arg) for arg in args))), max(list((len(arg) for arg in args)))])

    '''функція приймає довільну кількість списків,
    повертає список з найкоротшим та найдовшим з усіх переданних.'''

    print(list(max_min_len_lamblda(num_list10, num_list11, num_list12, num_list13)))
