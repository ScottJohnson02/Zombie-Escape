class Scene(object):
    def help(self):
        return "Here is all the commands you can enter in the field "


class Apartment(Scene):
    def __init__(self):
        self.name = 'Apartment'

    def enter(self):
        return "welcome to the apartment"


class Thaddeus(Scene):
    def __init__(self):
        self.name = 'Thaddeus'

    def enter(self):
        return "welcome to Thaddeus Stevens"


class CarDealership(Scene):
    def __init__(self):
        self.name = 'CarDealership'

    def enter(self):
        return "welcome to the car dealership"


class Market(Scene):
    def __init__(self):
        self.name = 'Market'

    def enter(self):
        return "welcome to the Market"
