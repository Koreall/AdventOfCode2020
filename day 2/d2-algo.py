Lines = []
with open("d2-input.txt", 'r') as f:
	for l in f:
		Lines.append(l)

## Input processing ##
import re
expr = re.compile(r"(\d+)-(\d+) (.): (.+)")
for i in range(len(Lines)):
	Lines[i] = expr.match(Lines[i]).groups()

## Part 1 ##
valids = 0
for i, l in enumerate(Lines):
	if l[3].count(l[2]) in range(int(l[0]),int(l[1])+1):
		valids += 1

print("## Day 2 - Part 1:\n\tValids:",valids)
input()

print()
## Part 2 ##
valids = 0
for i, l in enumerate(Lines):
	if (l[3][int(l[0])-1] == l[2]) + (l[3][int(l[1])-1] == l[2]) == 1:
		valids += 1

print("## Day 2 - Part 2:\n\tValids:",valids)
input()