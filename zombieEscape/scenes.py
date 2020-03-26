class Scene(object):
    def help(self):
        return "Here is all the commands you can enter in the field "


class Apartment(Scene):
    def __init__(self):
        self.message = ' '
        self.name = 'Apartment'

    def enter(self):
        return """You enter an old abandoned appartment where it looks as if there was a fire. You suddenly encounter a walker but it is melted into the carpet
    you have a choice to make: 1. kill the walker or 2. dont kill the walker """

    def choice(self, word):
        if word == 'die':
            return 'die'
        elif word == '1':
            self.message = 'You decide to kill the walker to end his suffering '
            return 'next'
        elif word == '2':
            self.message = 'You decide to let the walker suffer like the monster it is. You hear faint growls crying out as you walk away'
            return 'next'
        else:
            return 'error'


class Thaddeus(Scene):
    def __init__(self):
        self.message = ' '
        self.name = 'Thaddeus'

    def enter(self):
        return """welcome to Thaddeus Stevens. The campus is in complete dissaray and trash is everywhere along with a hoard of walkers. You slowly sneak through the campus trying
    to avoid detection when you come across a bunch of looters looking for any supplies they can find. They spot you and call out to you for help. They are asking for meds because her sister
    is sick with a fever and they need antibiotics. You have a choice to make: 1. give them your meds, 2. run away from them, 3. rob them"""

    def choice(self, word):
        if word == '1':
            self.message = "'Wow that was easy! Come on out boys' the looter shouts. You see two men with sawed offs come out the shadow and before you have time to respond you get shot. If it makes you feel better they later died due to attracting walkers. "
            return 'die'
        elif word == '2':
            self.message = "'DAMMIT HE DIDN'T BELEIEVE ME START FIRING' she shouts and 2 men with rifles start taking pot shots at you but luckily they miss and the noise attracts the walkers to their location. Luckily you made it out unharmed"
            return 'next'
        elif word == '3':
            self.message = " In your most intimidating voice you demand that she hands you all of HER supplies and you pull out your gun. She chuckles at your attempt and then a man comes from behind you and chokes you out and everything goes black."
            return 'die'
        else:
            return 'error'


class CarDealership(Scene):
    def __init__(self):
        self.name = 'CarDealership'
        self.message = ' '

    def enter(self):
        return """welcome to the car dealership! You see a bright red convertible with a large price tag that reads $18,000. Next to that vechicle you see a beat up van that has
    grafiti on it that reads "FREE CANDY". You also see that the door to the dealership is open. You decide to peer into the managers office where you see all the car keys hanging
    up on display. There is a large crowd of walkers heading your way and they seem to have noticed you and are NOW HEADING YOUR WAY! You have to make a choice:
    1. Ride off in the fast convertible
    2. Take the beat up van
    3. Try to hide from the zombies """

    def choice(self, word):
        if word == '1':
            self.message = 'You died from a zombie lurking in the backseat and when you hop in you feel a bite in your neck and everything goes hazy.'
            return 'die'
        elif word == '2':
            self.message = "You hop in the van and it is slow to start but it eventually starts and you run over 3 zombies and you go back on the road to continue your adventure"
            return 'next'
        elif word == 'loot':
            return 'loot'
        elif word == '3':
            self.message = 'You climb to the roof of the dealership but the zombies don\'t give up and they stay around the building. Days go by and they haven\' left yet. You die due to starvation'
            return 'die'
        else:
            return word


class Market(Scene):
    def __init__(self):
        self.name = 'Market'
        self.message = ' '

    def enter(self):
        return """'Welcome to the Market!' a vendor says and then you notice that they whole location was turned into a trader camp where fellow survivors can trade their supplies. You see a fragile old lady running a stand by herself.
    She is in the corner of the building and someone could rob her easily. You have a choice to make: 1. Rob the lady or 2. let her be and leave the camp"""

    def choice(self, word):
        if word.upper() == '1':
            self.message = "The old lady sees the look on your face and knows that you want to rob her. She quickly pulls out her pistol and blasts you between the eyes."
            return 'die'
        elif word.upper() == '2':
            self.message = 'You decide not to rob the sweet innocent old lady adn you give her a smile before you exit through the doors.'
            return 'next'
        elif word.upper() == 'LOOT':
            return 'loot'
        else:
            return 'error'
