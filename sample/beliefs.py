import numpy
import math

max_belief_value = 5
min_belief_value = -max_belief_value
belief_sigma = math.sqrt(3)
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


class Belief:
    def __init__(self, name, value=0):
        self.value = max(min_belief_value, min(max_belief_value, value))
        self.name = name


class BeliefSystem:
    def __init__(self):
        self.beliefs = list(map(
            lambda b: Belief(b, round(numpy.random.normal(0, belief_sigma))),
            belief_list
        ))
        self.sort(True)

    def sort(self, rev=False):
        self.beliefs.sort(key=lambda e: e.value, reverse=rev)
