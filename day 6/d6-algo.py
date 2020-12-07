Lines = []
with open("d6-input.txt",'r') as f:
	for l in f:
		Lines.append(l.strip())

## PART 1 ##
answers = set()
score = 0
for line in Lines:
	if not line:
		score += len(answers)
		answers = set()
		continue
	for letter in line:
		answers.add(letter)

score += len(answers)

print("## DAY 6 ##")
print("\t- Part 1 : The total score is", score)

## PART 2 ##
score = 0
answers = set()
new_line = True
for line in Lines:
	if not line:
		score += len(answers)
		new_line = True
		continue
	if not new_line:
		answers = set(x for x in answers if x in line)
	else:
		answers = set(x for x in line)
		new_line = False
score += len(answers)

print("\t- Part 2 : The new score is", score)
input()