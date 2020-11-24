import random
import math
from attributes.data.names import names, surnames


def generate_name(genderName):
    if names[genderName] is None:
        zippedList = zip(names.male, names.female)
        nameList = [val for pair in zippedList for val in pair]
    else:
        nameList = names[genderName]

    # Weights will range from .5 to 1.5 times the name list length,
    # wich will make the first names in the list 3 times more likely
    min_weight = math.floor(len(nameList) / 2)
    max_weight = len(nameList) + min_weight
    first = random.choices(nameList, range(max_weight, min_weight, -1))[0]

    return Name(first, random.choice(surnames), random.choice(surnames))


class Name:
    def __init__(self, first, *argv):
        self.first = first
        self.other = list(argv)

    def full(self):
        return f"{self.first} {' '.join(self.other)}"
