import numpy as np
Numbers = []
with open("d1-input.txt", 'r') as f:
	for l in f:
		Numbers.append(int(l.strip()))

## PART 1
print("## Day 1 - Part 1 ##")
for i in range(len(Numbers)):
	for j in range(len(Numbers)):
		if i != j and Numbers[i] + Numbers[j] == 2020:
			print("Solution found : a = {} and b = {}. a + b = 2020\n\t=> a * b = {}".format(Numbers[i], Numbers[j], Numbers[i] * Numbers[j]))
			break
	else:
		continue
	break

input()

## PART 2
print("\n## Day 1 - Part 2 ##")
for i in range(len(Numbers)):
	for j in range(len(Numbers)):
		if Numbers[i] + Numbers[j]>2020:
			continue
		for k in range(len(Numbers)):
			if i != j and i != k and Numbers[i] + Numbers[j] + Numbers [k] == 2020:
				print("Solution found : a = {}, b = {} and c = {}. a + b + c = 2020\n\t=> a * b * c = {}".format(Numbers[i], Numbers[j], Numbers[k], Numbers[i] * Numbers[j] * Numbers[k]))
				break
		else:
			continue
		break
	else:
		continue
	break

input()