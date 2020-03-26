class Scene(object):
    def help(self):
        return "Here is all the commands you can enter in the field "


class Apartment(Scene):
    def __init__(self):
        self.name = 'Apartment'

    def enter(self):
        return "welcome to the apartment"

    def choice(self, word):
        if word == 'die':
            return 'die'
        elif word == 'next':
            return 'next'
        elif word == 'loot':
            return 'loot'
        else:
            return 'error'


class Thaddeus(Scene):
    def __init__(self):
        self.name = 'Thaddeus'

    def enter(self):
        return "welcome to Thaddeus Stevens"

    def choice(self, word):
        if word == 'die':
            return 'die'
        elif word == 'next':
            return 'next'
        elif word == 'loot':
            return 'loot'
        else:
            return 'error'


class CarDealership(Scene):
    def __init__(self):
        self.name = 'CarDealership'

    def enter(self):
        return "welcome to the car dealership"

    def choice(self, word):
        if word == 'die':
            return 'die'
        elif word == 'next':
            return 'next'
        elif word == 'loot':
            return 'loot'
        else:
            return 'error'


class Market(Scene):
    def __init__(self):
        self.name = 'Market'

    def enter(self):
        return "welcome to the Market"

    def choice(self, word):
        if word.upper() == 'DIE':
            return 'die'
        elif word.upper() == 'NEXT':
            return 'next'
        elif word.upper() == 'LOOT':
            return 'loot'
        else:
            return 'error'
