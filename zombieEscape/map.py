from zombieEscape import scenes
import random

game_length = 3


class Map(object):
    def __init__(self):
        self.scenes = [scenes.Apartment(), scenes.CarDealership(),
                       scenes.Thaddeus(), scenes.Market()]
        self.names = []

    def create(self):
        """Builds the game map"""
        random.shuffle(self.scenes)
        # shuffles the list of scenes
        while len(self.scenes) > game_length:
            self.scenes.pop()
        for scene in self.scenes:
            self.names.append(scene.name)

        self.current = self.scenes[0]
