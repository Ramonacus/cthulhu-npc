max_belief_val = 5
min_belief_val = -max_belief_val

"""
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
"""


class Belief:
    def __init__(self, name, value):
        self.value = max(min_belief_val, min(value, max_belief_val))
        self.name = name

    @property
    def group(self):
        if self.value == 5:
            return 'adores'
        if self.value >= 3:
            return 'loves'
        if self.value >= 1:
            return 'likes'
        if self.value > -1:
            return 'is neutral to'
        if self.value > -3:
            return 'dislikes'
        if self.value > -5:
            return 'hates'
        else:
            return 'abhors'

    @property
    def description(self):
        return f"%s {self.group} {self.name}"
