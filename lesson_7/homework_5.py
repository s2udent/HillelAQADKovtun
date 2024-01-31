
if __name__ == '__main__':
    # Task 1

    num_list1 = [3, 7, 5, 6, 1]
    num_list2 = [10, 5, 8, 7, 3]

    intersection_lambda = lambda list1, list2: list(set(list1).intersection(set(list2)))

    print(intersection_lambda(num_list1, num_list2))

    # Task 2

    test_str = '-55366'
    test_str_with_float = '-36.6'

    str_is_digit_labda = lambda string: (((string.split('.')[0].split('-')[1].isdigit()
                                          and (string.split('.')[1].isdigit()))
                                          if string.split('.')[0].startswith('-')
                                          else (string.split('.')[0].isdigit() and string.split('.')[1].isdigit()))
                                         if '.' in string
                                         else (string.isdigit() or string.startswith('-')
                                               and string.split('-')[1].isdigit()))

    print(str_is_digit_labda(test_str))
    print(str_is_digit_labda(test_str_with_float))

    '''
    more understandable view of lambda above
    
    if '.' in test_float:
        float_list = test_float.split('.')
        if float_list[0].startswith('-'):
            print(float_list[0].split('-')[1].isdigit() and float_list[1].isdigit())
        else:
            print(float_list[0].isdigit() and float_list[1].isdigit())
    else:
        print(test_float.isdigit() or test_float.startswith('-') and test_float.split('-')[1].isdigit())'''


    # Task 3

    num_list10 = [1, 7, 5, 6]
    num_list11 = [10, 5, 8, 7, 3, 14, 16]
    num_list12 = [10, 5, 8, 7, 3, 5, 8, 99, 90, 76]
    num_list13 = [10, 5, 8, 7, 3, 5, 8, 99, 90, 76, 55, 66]

    max_min_len_lamblda = lambda *args: list(item for item in args if (len(item)) in
                                         [min(list((len(arg) for arg in args))), max(list((len(arg) for arg in args)))])

    '''функція приймає довільну кількість списків,
    повертає список з найкоротшим та найдовшим з усіх переданних.'''

    print(max_min_len_lamblda(num_list10, num_list11, num_list12, num_list13))
