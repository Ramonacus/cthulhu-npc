from npc import NPC
from itertools import groupby
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--gender', nargs='?',
    help='Female, male or non-binary')
parser.add_argument('--expression', nargs='?',
    help='Gender expression, accepted values are: cis or trans')
parser.add_argument('--sexuality', nargs='?',
    help='Heterosexual, homosexual or bisexual')
parser.add_argument('--age', nargs='?', help='In years, defaults to a 12 to 60 range')

args = parser.parse_args()


npc = NPC(
    gender_name=args.gender,
    gender_expression=args.expression,
    sexuality=args.sexuality,
    max_age=int(args.age or 60),
    min_age=int(args.age or 12)
)

print(f"{npc.name.full} is a {npc.sexuality.name} {npc.gender.name}")
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
