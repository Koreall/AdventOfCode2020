lines = []
with open("d8-input.txt", 'r') as f:
	for line in f:
		lines.append(line.strip())

## PART 1 ##
LEN = len(lines)
def execution():
	accumulator = 0
	ip = 0
	executed = set()
	while ip < LEN:
		if ip in executed:
			break
		executed.add(ip)
		instr, value = lines[ip].split()
		if instr == "acc":
			accumulator += int(value)
			ip += 1
		elif instr == "jmp":
			ip += int(value)
		else:
			ip += 1
	else:
		return accumulator,ip, True
	return accumulator,ip, False

print("## DAY 8 ##")
acc, eip, term = execution()
print("\t- Part 1 : Your program loops at address {} with value: {}".format(eip, acc))


## PART 2 ##
for i, line in enumerate(lines):
	instr, value = line.split()
	if instr == "jmp":
		lines[i] = "nop "+value
	elif instr == "nop":
		lines[i] = "jmp "+value
	else:
		continue

	acc, eip, term = execution()
	if term:
		print("\t- Part 2 : The program terminated with value: {}".format(acc))
		break
	lines[i] = ' '.join([instr,value])

input()