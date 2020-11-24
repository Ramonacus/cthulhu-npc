import datetime
import random
import attributes
import beliefs


# TODO fix this quirk. Create class Campaign? World?
campaignDate = datetime.date(1934, 12, 31)
currentDate = campaignDate or datetime.date.today()

class NPC:
    """ Procedurally generates a NPC.
    Should add config to everything in the future. """

    def __init__(self):
        # Define sexual traits and name
        self.gender = attributes.Gender()
        self.sexuality = attributes.Sexuality()
        self.name = attributes.generate_name(self.gender.name)

        # Define age in relationship with campaign setting
        ageRange = random.randrange(365.25 * 80)
        self.birthday = currentDate - datetime.timedelta(days=ageRange)

        # Belief system
        self.beliefSystem = beliefs.BeliefSystem()

    # Get the age for the current campaignDate
    @property
    def age(self):
        dob = self.birthday
        current = campaignDate or datetime.date.today()
        years = current.year - dob.year
        if (current.month < dob.month
            or current.month == dob.month
            and current.day < dob.day):
            # The date of birth is later during the year, decrease the age by 1
            years -= 1
        return years
