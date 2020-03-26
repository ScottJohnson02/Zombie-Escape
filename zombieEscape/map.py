from zombieEscape import scenes
import random


game_length = 3


class Map(object):
    def __init__(self):
        # calls the scenes from scenes\.py
        self.scenes = [scenes.Apartment(), scenes.CarDealership(),
                       scenes.Thaddeus(), scenes.Market()]
        self.newmap = []
        self.names = " "

    def create(self):
        # builds the game map and sets the path for the map text on html
        self.names = " "
        self.newmap = []

        self.newmap += self.scenes
        random.shuffle(self.newmap)
        # shuffles the list of scenes
        while len(self.newmap) > game_length:
            # changes the size of the map according to game_length
            self.newmap.pop()
        for scene in self.newmap:
            # make a string with the scene names
            self.names += scene.name + ', '
