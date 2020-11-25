from beliefs.classes import Belief
import numpy
import math


belief_list = [
    "religion",
    "tradition",
    "wealth",
    "power",
    "knowledge",
    "homeland",
    "peace",
    "justice",
    "law",
    "sex",
    "romance",
    "family",
    "friendship",
    "honesty",
    "independence"
]
# Make -5.5 and 5 three standard deviations away
# This way 99.73% of values will be between those two
mean = 0
stdev = 5.5/3


class BeliefSystem:
    def __init__(self):
        self.beliefs = list(map(
            lambda b: Belief(b, numpy.random.normal(mean, stdev)),
            belief_list
        ))
        self.sort(True)

    def sort(self, rev=False):
        self.beliefs.sort(key=lambda e: e.value, reverse=rev)
