from attributes import gender, sexuality, name


class NPC:
    def __init__(self):
        self.gender = gender.Gender()
        self.sexuality = sexuality.Sexuality()
        self.name = name.generate(self.gender.name)


npc = NPC()

print(f"{npc.name.full()} is a {npc.sexuality.name} {npc.gender.name}")
