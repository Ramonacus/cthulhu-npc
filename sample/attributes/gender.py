from attributes import weighted_attr


class Gender:
    def __init__(self, name=None, expression=None):
        self.name = weighted_attr.generate(
            ['non-binary', 'female', 'male'],
            [0.2, 49.8, 49.8])(name)
        self.expression = weighted_attr.generate(
            ['cis', 'trans'],
            [99.4, 0.6])(expression)

    @property
    def pronoun(self):
        return "he" if self.name == 'male'\
            else "she" if self.name == 'female'\
            else "they"

    @property
    def possessive_pronoun(self):
        return "his" if self.name == 'male'\
            else "her" if self.name == 'female'\
            else "their"
