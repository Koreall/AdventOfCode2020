lines = []
with open("d7-input.txt", 'r') as f:
	for line in f:
		lines.append(line.strip())

## Part 1 ##
import re
class Bag:
	def __init__(self, color):
		self.color = color
		self.parents = []
		self.children = []

	def subBag(self, child, nb):
		self.children.append((child, nb))
		child.parents.append(self)


Bags = {}
bagFmt = re.compile(r"[a-zA-Z ]*?(\d*) ?([a-zA-Z ]*?) bag")
for line in lines:
	grps = bagFmt.findall(line)
	owner = grps[0][1]
	if not owner in Bags:
		Bags[owner] = Bag(owner)
	for nb, color in grps[1:]:
		if not nb:
			continue #Bag contains none other
		if not color in Bags:
			Bags[color] = Bag(color)
		Bags[owner].subBag(Bags[color], int(nb))

print("## DAY 7 ##")
containers = set()
search_space = [Bags["shiny gold"],]
while search_space:
	b = search_space.pop(0)
	search_space += [x for x in b.parents if x not in containers]
	containers.update(b.parents)

print("\t- Part 1 : {} bags contain the shiny gold one.".format(len(containers)))

## Part 2 ##
size_of_bags = {}
total_contained = 0
def contained(bag):
	if not bag.children:
		return 1

	#if bag.color in size_of_bags:
	#	return size_of_bags[bag.color]

	score = 1 #for the bag itself
	for b, nb in bag.children:
		size_of_bags[b.color] = contained(b)
		score += nb * contained(b)#size_of_bags[b.color]

	return score

total_contained = contained(Bags["shiny gold"]) - 1 #We don't count the shiny bag

print("\t- Part 2 : The shiny gold bag contains {} bags".format(total_contained))
input()