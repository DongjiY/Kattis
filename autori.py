import sys

acronym = " "
phrase = sys.stdin.readline().split("-")
for x in phrase:
    acronym += x[0]
print(acronym)