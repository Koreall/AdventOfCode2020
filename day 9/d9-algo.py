lines = []
for line in open("d9-input.txt", 'r'):
	lines.append(line.strip())

## PART 1 ##
numbers = [int(lines[i]) for i in range(25)]

for k in range(25,len(lines)):
	n = int(lines[k])
	for i in range(24):
		for j in range(i+1, 25):
			if numbers[i]+numbers[j] == n:
				numbers.pop(0)
				numbers.append(n)
				break
		else:
			continue
		break
	else:
		break

print("## DAY 9 ##")
print("\t- Part 1: {} isn't the sum of 25 consecutive numbers before him".format(lines[k]))

## Part 2 ##
to_find = n

for i in range(len(lines)):
	S = 0
	for j in range(i,len(lines)-1):
		S += int(lines[j])
		if S >= to_find:
			break

	if S == to_find:
		break

L = [int(lines[k]) for k in range(i,j+1)]

print("\t- Part 2: The som of the min and max is:", min(L)+max(L)) 

## END ##
input()