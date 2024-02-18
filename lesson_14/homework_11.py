from abc import ABC, abstractmethod


class Art(ABC):

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.creation_date = None
        self.__under_protection = False
        self.current_place = None
        self.estimated_price = None

    @abstractmethod
    def is_on_sale(self):
        pass

    @property
    def is_protected(self):
        return self.__under_protection

    @is_protected.setter
    def is_protected(self, protected):
        self.__under_protection = protected


class Paintings(Art):

    def __init__(self, name, author, creation_date):
        super().__init__(name, author)
        self.creation_date = creation_date

    def is_on_sale(self):
        if self.is_protected:
            print('It is a legacy thing, not for sale')
        elif self.estimated_price:
            print(f'{self.name} item can be sold for ${self.estimated_price}')
        else:
            print('Sorry, no information available at this time..')

    def __make_a_frame(self):
        print('Creating a frame for the painting')

    def __cut_the_glass(self):
        print('Preparing the glass')

    def place_under_glass(self):
        self.__make_a_frame()
        self.__cut_the_glass()
        print(f'{self.name} is being placed to the frame, under the glass')


class Sculptures(Art):
    def __init__(self, name, author):
        super().__init__(name, author)

    def is_on_sale(self):
        print('Sorry sculptures an\'t be sold at this time')

    def __arranging_documentation(self):
        self.current_place = 'Moving'
        print('All docs are ready')

    def move_to_another_museum(self, place_name):
        self.__arranging_documentation()
        self.current_place = place_name
        print(f'{self.name} - Successfully moved to {place_name}')


mona_lisa = Paintings('Mona Lisa', 'Leonardo Da Vinci', 1519)
mona_lisa.is_protected = True
mona_lisa.is_on_sale()

my_entrance_wall = Paintings('My Entrance Wall', 'Sonya Moroziuk', 2020)
my_entrance_wall.estimated_price = 600
my_entrance_wall.place_under_glass()
my_entrance_wall.is_on_sale()

the_kiss_sculpture = Sculptures('The Kiss', 'Constantin Brancusi')
the_kiss_sculpture.creation_date = 1908
the_kiss_sculpture.is_on_sale()
the_kiss_sculpture.move_to_another_museum('Kyiv')
print(the_kiss_sculpture.current_place)
