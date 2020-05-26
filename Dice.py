import random


class Dice:
    def __init__(self):
        pass

    def roll(self, sides):
        return random.randint(1, sides)

    def rollExplode(self, sides):
        result = [self.roll(sides)]
        i = 0
        while result[i] == sides:
            i += 1
            result.append(self.roll(sides))
        return result

    def toHit(self, sides):
        roll = self.rollExplode(sides)
        if sum(roll) >= 12:
            return 'hit with raise and +1   {} {}'.format(sum(roll), roll)
        if sum(roll) >= 8:
            return 'hit with raise   {} {}'.format(sum(roll), roll)
        if sum(roll) >= 4:
            return 'hit   {} {}'.format(sum(roll), roll)
        return 'miss   {} {}'.format(sum(roll), roll)

