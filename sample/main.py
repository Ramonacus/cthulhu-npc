import datetime
import random
from attributes import gender, sexuality, name


campaignDate = datetime.date(1920, 12, 31)


class NPC:
    """ Procedurally generates a NPC.
    Should add config to everything in the future. """

    def __init__(self):
        # Define sexual traits and name
        self.gender = gender.Gender()
        self.sexuality = sexuality.Sexuality()
        self.name = name.generate(self.gender.name)

        # Define age in relationship with campaign setting
        currentDate = campaignDate or datetime.date.today()
        ageRange = random.randrange(365.25 * 80)
        self.birthday = currentDate - datetime.timedelta(days=ageRange)

    @property
    def age(self):
        dob = self.birthday
        current = campaignDate or datetime.date.today()
        years = current.year - dob.year
        if (current.month < dob.month or
            current.month == dob.month and
            current.day < dob.day):
            # The date of birth is later during the year, decrease the age by 1
            years -= 1
        return years


npc = NPC()

print(f"{npc.name.full()} is a {npc.sexuality.name} {npc.gender.name}")
print(f"{npc.gender.pronoun.capitalize()} was born on {npc.birthday.strftime('%b %d %Y')}")
print(f"{npc.gender.pronoun.capitalize()} is now {npc.age} years old")
