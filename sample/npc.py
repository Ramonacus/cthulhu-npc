import datetime
import random
import attributes
import beliefs
from relationship import Relationship


# TODO fix this quirk. Create class Campaign? World?
campaignDate = datetime.date(1934, 12, 31)
currentDate = campaignDate or datetime.date.today()


class NPC:
    """ Procedurally generates a NPC.
    Should add config to everything in the future. """

    def __init__(self,
        gender_name=None,
        gender_expression=None,
        sexuality=None,
        max_age=60,
        min_age=12):
        # Define sexual traits and name
        self.gender = attributes.Gender(name=gender_name, expression=gender_expression)
        self.sexuality = attributes.Sexuality(sexuality)
        self.name = attributes.generate_name(self.gender.name)

        # Define age in relationship with campaign setting
        days_per_year = 365.25
        ageRange = random.randrange(
            round(days_per_year * min_age),
            round(days_per_year * (max_age + 1)))
        self.birthday = currentDate - datetime.timedelta(days=ageRange)

        # Belief system
        self.beliefSystem = beliefs.BeliefSystem()

        # Relationships starts as an empty list
        self.relationships = []

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

    def generate_family_at_birth(self):
        # For now I will settle for traditional families
        # TODO Monoparental? Homosexual with adopted kids?
        mother = NPC(gender_name='female', min_age=self.age+16, max_age=self.age+44)
        mother.name.other[0] = self.name.other[1]
        self.relationships.append(Relationship(mother, 'parent'))
        mother.relationships.append(Relationship(self, 'offspring'))

        father = NPC(gender_name='male', min_age=self.age+16, max_age=self.age+44)
        father.name.other[0] = self.name.other[0]
        self.relationships.append(Relationship(father, 'parent'))
        father.relationships.append(Relationship(self, 'offspring'))

    def get_relationships(self, type):
        return filter(lambda x: x.type, self.relationships)
