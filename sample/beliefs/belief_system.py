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
belief_sigma = math.sqrt(3)


class BeliefSystem:
    def __init__(self):
        self.beliefs = list(map(
            lambda b: Belief(b, round(numpy.random.normal(0, belief_sigma))),
            belief_list
        ))
        self.sort(True)

    def sort(self, rev=False):
        self.beliefs.sort(key=lambda e: e.value, reverse=rev)
