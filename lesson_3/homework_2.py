import random

# Task 1

min = random.randint(0, 59)  # В змінній min лежить число

if min < 15:
    print(f'Num is in the 1st quarter: {min}')
elif 15 <= min < 30:
    print(f'Num is in the 2nd quarter: {min}')
elif 30 <= min < 45:
    print(f'Num is in the 3rd quarter: {min}')
else:
    print(f'Num is in the 4th quarter: {min}')

# Task 2

birth_month = input('Please, enter your birthday month number: ')

if birth_month.isdigit():
    birth_month = int(birth_month)
    if birth_month in [12, 1, 2]:
        print('Зима - За вікном падав сніг.')
    elif birth_month in [3, 4, 5]:
        print('Весна - Все довкола розцвітало.')
    elif birth_month in [6, 7, 8]:
        print('Літо - Діти насолоджувались літніми канікулами.')
    elif birth_month in [9, 10, 11]:
        print('Осінь - Все довкола загоралось яскравими фарбами.')
    else:
        print('Your number is not in range 1-12')
else:
    print('Try entering another number')

# Task 3

generated_num = random.randint(100, 999)
string_num = str(generated_num)
list_num = [int(string_num[0]), int(string_num[1]), int(string_num[2])]
if sum(list_num) % 3 == 0 and list_num[2] % 2 == 0:
    print(f'Число {generated_num} ділиться на 6')
else:
    print(f'Число {generated_num} не ділиться на 6')

# Task 4

x = input('Enter X coordinate')
y = input('Enter Y coordinate')
x, y = float(x), float(y)

if x == 0 or y == 0:
    if x == 0 and y == 0:
        print(f'Точка {x, y} знаходиться на початку координат')
    elif x == 0:
        print(f'Точка {x, y} знаходиться на осі Х')
    else:
        print(f'Точка {x, y} знаходиться на осі Y')
elif x > 0:
    if y > 0:
        print(f'Точка {x, y} знаходиться у I чверті')
    else:
        print(f'Точка {x, y} знаходиться у IV чверті')
else:
    if y > 0:
        print(f'Точка {x, y} знаходиться у II чверті')
    else:
        print(f'Точка {x, y} знаходиться у III чверті')

