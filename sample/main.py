from npc import NPC
from itertools import groupby


npc = NPC()

print(f"{npc.name.full()} is a {npc.sexuality.name} {npc.gender.name}")
print(f"{npc.gender.pronoun.capitalize()} was born on "\
    f"{npc.birthday.strftime('%b %d %Y')}")
print(f"{npc.gender.pronoun.capitalize()} is now {npc.age} years old")

def groupBeliefs(group):
    regroup = list(belief.name for belief in group)
    return regroup[0] if len(regroup) == 1\
        else ' and '.join([', '.join(regroup[:-1]), regroup[-1]])

print(f"{npc.gender.pronoun.capitalize()} has the following beliefs:")
for key, group in groupby(npc.beliefSystem.beliefs, lambda x: x.group):
    print(f"* {key} {groupBeliefs(group)}")
