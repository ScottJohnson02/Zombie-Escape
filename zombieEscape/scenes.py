class Scene(object):
    def help(self):
        return "Here is all the commands you can enter in the field "


class Apartment(Scene):
    def enter(self):
        return "welcome to the apartment"


class Thaddeus(Scene):
    def enter(self):
        return "welcome to Thaddeus Stevens"


class CarDealership(Scene):
    def enter(self):
        return "welcome to the car dealership"


class Market(Scene):
    def enter(self):
        return "welcome to the Market"
