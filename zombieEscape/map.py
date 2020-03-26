from zombieEscape import scenes
import random

game_length = 3


class Map(object):
    def __init__(self):
        self.scenes = [scenes.Apartment(), scenes.CarDealership(),
                       scenes.Thaddeus(), scenes.Market()]
        self.newmap = []
        self.names = " "

    def create(self):
        self.names = " "
        self.newmap = []
        """Builds the game map"""
        self.newmap += self.scenes
        random.shuffle(self.newmap)
        # shuffles the list of scenes
        while len(self.newmap) > game_length:
            self.newmap.pop()
        for scene in self.newmap:
            self.names += scene.name + ', '
