from random import choice
'''
For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years
'''


def dog_to_human_years(h_age):
    if h_age < 0:
        print("Age must be a positive number.")
        exit()
    elif h_age <= 2:
        d_age = h_age * 10.5
    else:
        d_age = 21 + (h_age - 2) * 4
    return f"The dog's age in dog's years is {d_age}"


if __name__ == "__main__":

    def random_greeting(): # this func can not be imported anywhere
        greeting_list = ["Hello", "Hi", "Hey", "Yo!", "What’s up?", "Sup", "Heyyy", "Hiya!"]
        return choice(greeting_list)

    print(dog_to_human_years(int(input("Input a full dog's age in human years: "))))
    print(random_greeting())
