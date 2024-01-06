import math
# Task 1

name = 'Dmytro'
surname = 'Kovtun'

full_name = name + ' ' + surname

print(full_name)

print(full_name.lower(), full_name.upper(), full_name.title())

name = '  \t Dmytro\n '
surname = '\n Kovtun  \t'

print(name + ' ' + surname)

name = name.strip()
surname = surname.strip()

print(name + ' ' + surname)

# Task 2
radius = 5

# circumference С = 2piR
# area of the circle S = piR^2
print(f'''The circumference of the circle with radius: {radius}
is {2*math.pi*radius} and the area is: {math.pi*radius**2}''')

# Task 3

usd_rate = 38.50
uah_to_usd = 1000/usd_rate
uah_to_usd = round(uah_to_usd, 2)
print(f'Current currency exchange rate is: {uah_to_usd}')


