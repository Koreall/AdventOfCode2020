Lines = []
with open("d5-input.txt", 'r') as f:
	for l in f:
		Lines.append(l.strip())

## PART 1 ##
def getBetterOrder(v):
	return {'B':1, 'F':0, 'R':1 ,'L':0}[v]

all_seats = set(int(''.join(str(getBetterOrder(letter)) for letter in e),2) for e in Lines)

maxSeat = max(all_seats)
print("## DAY 5 ##")
print("\t- Part 1 : The greatest seat index is {}".format(maxSeat))

## PART 2 ##
minSeat = min(all_seats)
for i in range(minSeat,maxSeat):
	if i not in all_seats:
		print("\t- Part 2 : The only seat missing is {}".format(i))
		break
input()