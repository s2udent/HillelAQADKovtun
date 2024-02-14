
# Task 1

class Dog:

    def __init__(self, dog_name, breed, age):
        self.dog_name = dog_name
        self.breed = breed
        self.age = age

    @staticmethod
    def dog_to_human_years(h_age):
        if h_age < 0:
            print("Age must be a positive number.")
            exit()
        elif h_age <= 2:
            d_age = h_age * 10.5
        else:
            d_age = 21 + (h_age - 2) * 4
        return f"The dog's age in dog's years is {d_age}"


bulka = Dog('Bulka', 'German Shepherd', 1)
print(Dog.dog_to_human_years(2))

# Task 2


class UkrainianAirlines:
    def __init__(self, name, origin_country, most_popular_aircraft, perform_international_flights):
        self.name = name
        self.origin_country = origin_country
        self.most_popular_aircraft = most_popular_aircraft
        self.perform_international_flights = perform_international_flights

    @classmethod
    def default_values(cls, name):
        values ={'name': name,
                 'origin_country': 'Ukraine',
                 'most_popular_aircraft': 'Boeing 747',
                 'perform_international_flights': True}
        return cls(**values)


uia = UkrainianAirlines('Ukraine International Airlines',
                        'Ukraine',
                        'Boeing 777',
                        True)

sky_up = UkrainianAirlines.default_values('SkyUp')

print(sky_up.name, sky_up.origin_country, sky_up.most_popular_aircraft, sky_up.perform_international_flights)
