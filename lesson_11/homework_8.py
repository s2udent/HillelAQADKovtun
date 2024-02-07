from random import randint
# Task 1

def get_func_name(func):
    def inner(*args):
        print(func.__name__)
        results = func(*args)
        return results
    return inner


@get_func_name
def get_sum(*args):
    return sum(args)


@get_func_name
def get_multiplication(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(get_sum(2, 2, 2))
print(get_multiplication(1, 2, 3, 4, 5))

# Task 2

test_list = [randint(1, 10) for x in range(1, 101)]
print(test_list)

test_dict = {}

for num in test_list:
    if num in test_dict:
        test_dict[num] += 1
    else:
        test_dict[num] = 1


for k, v in sorted(test_dict.items()):
    print(f'Число {k}, зустрічається {v} разів')
