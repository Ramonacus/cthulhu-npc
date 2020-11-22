import random

# Returns a function to randomly select an attribute from a list based on weights
def generate(options, w):
    if len(options) != len(w):
        raise Exception("Options and weights differ in length")

    def callback(name=None):
        if name is None:
            name = random.choices(options, weights=w)[0]
        elif name not in options:
            # If passing an override, it must still be amongst the valid values
            raise Exception("Invalid option")
        return name

    return callback
