import random


# Returns a function to select an attribute from a list based on weights
def generate(options, w):
    if len(options) != len(w):
        raise Exception("The number of weights does not match the population")

    def callback(name=None):
        if name is None:
            name = random.choices(options, weights=w)[0]
        elif name not in options:
            # If passing an override, it must still be amongst the valid values
            raise Exception("Invalid option")
        return name

    return callback
