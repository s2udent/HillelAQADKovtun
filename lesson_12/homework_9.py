import datetime as dt

# Task 1

test_date = dt.datetime(2001, 9, 11, 3, 14, 30, 0, None)
days_num = 10
sign = True


def date_calc(datetime, daysnum, sign):
    if sign:
        return datetime + dt.timedelta(days=daysnum)
    else:
        return datetime - dt.timedelta(days=daysnum)


print(f'Task_1: {date_calc(test_date, days_num, sign)}')

# Task 2

test_birth_date = dt.datetime(1998, 11, 19, 4, 55, 50, 0, None)


def get_age(birth_date):
    time_now = dt.datetime.now()
    delta = time_now - birth_date
    t_stamp = dt.datetime.timestamp(time_now) - dt.datetime.timestamp(birth_date)
    # (рік(останні два числа, день, місяць, години, хвилини,секунди, am/pm в 12 годинному форматі)
    format_str = '%-y, %d, %m, %I, %M,%S %p'
    formatted_birth_date = test_birth_date.strftime(format_str)
    return delta, t_stamp, formatted_birth_date


print(get_age(test_birth_date))

# Task 3
try:
    with open('test.txt') as file:
        rows = file.readlines()
except FileNotFoundError as x:
    print('Ooops, file does not exist ->', x)
except Exception as x:
    print('Something went wrong ->', x)


