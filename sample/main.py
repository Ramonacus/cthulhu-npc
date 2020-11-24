from npc import NPC


npc = NPC()

print(f"{npc.name.full()} is a {npc.sexuality.name} {npc.gender.name}")
print(f"{npc.gender.pronoun.capitalize()} was born on {npc.birthday.strftime('%b %d %Y')}")
print(f"{npc.gender.pronoun.capitalize()} is now {npc.age} years old")
for belief in npc.beliefSystem.beliefs:
    print(f"{belief.name} value is {belief.value}")