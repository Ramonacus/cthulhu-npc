from attributes import weighted_attr


class Sexuality:
    def __init__(self, name=None):
        self.name = weighted_attr.generate(
            ['heterosexual', 'homosexual', 'bisexual'],
            [90, 8, 2])(name)
