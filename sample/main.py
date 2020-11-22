from attributes import gender, sexuality, name_generator


class NPC:
    def __init__(self):
        self.gender = gender.gender()
        self.sexuality = sexuality.sexuality()
        self.name = name_generator.generate(self.gender)


npc = NPC()

print(f"{npc.name} is a {npc.sexuality} {npc.gender}")
