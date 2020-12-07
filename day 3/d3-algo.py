Lines = []
with open("d3-input.txt", 'r') as f:
	for line in f:
		Lines.append(line.strip())

def slopes(x,y):
	position = [0,0]
	n_trees = 0
	while position[1] < len(Lines):
		n_trees += Lines[position[1]][position[0]] == "#"
		position = (position[0]+x)%len(Lines[0]), position[1]+y
	return n_trees


## PART 1
print("## Day 3 - Part 1 ##")
print("\tYou've encountered {} trees".format(slopes(3,1)))

## PART 2
print("## Day 3 - Part 2 ##")
from functools import reduce
print("\tScore:",reduce(lambda x, y: x*y, [slopes(i,1) for i in [1,3,5,7]] + [slopes(1,2)])))
input()