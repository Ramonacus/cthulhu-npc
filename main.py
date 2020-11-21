from attributes import gender, sexuality
import name_generator


class NPC:
    def __init__(self):
        self.gender = gender()
        self.sexuality = sexuality()
        self.name = name_generator.generate(self.gender)


npc = NPC()

print(f"{npc.name} is a {npc.sexuality} {npc.gender}")
