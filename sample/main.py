from attributes import gender, sexuality, name_generator


class NPC:
    def __init__(self):
        self.gender = gender.Gender()
        self.sexuality = sexuality.Sexuality()
        self.name = name_generator.generate(self.gender.name)


npc = NPC()

print(f"{npc.name} is a {npc.sexuality.name} {npc.gender.name}")
