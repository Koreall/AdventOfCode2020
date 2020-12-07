Lines = []
with open("d4-input.txt", 'r') as f:
	for l in f:
		Lines.append(l.strip())


## PART 1 ##
nb_complete = 0

## PART 2 ##
import re

colorMatch = re.compile(r"[#][0-9a-f]{6}")
idMatch = re.compile(r"\d{9}")
nb_valid = 0
def check(infos):
	B = len(infos["byr"]) == 4 and int(infos["byr"]) in range(1920, 2003)
	B &= len(infos["eyr"]) == 4 and int(infos["iyr"]) in range(2010, 2021)
	B &= len(infos["iyr"]) == 4 and int(infos["eyr"]) in range(2020, 2031)
	B &= bool(colorMatch.fullmatch(infos["hcl"]))
	B &= infos["ecl"] in "amb blu brn gry grn hzl oth".split()
	B &= bool(idMatch.fullmatch(infos["pid"]))
	if infos["hgt"][-2:] == "cm":
		B &= len(infos["hgt"]) == 5 and int(infos["hgt"][:-2]) in range(150,194)
	elif infos["hgt"][-2:] == "in":
		B &= len(infos["hgt"]) == 4 and int(infos["hgt"][:-2]) in range(59,77)
	else:
		B = False
	return B

## BOTH PARTS ##
D = {i:0 for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]}
for l in Lines:
	if not l:
		if all(D.values()):
			nb_complete += 1
			nb_valid += check(D)
		D = {i:0 for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]}
		continue
	for e in l.split():
		if e[:3] != "cid":
			D[e[:3]] = e[4:]

if all(D.values()):
	nb_complete += 1
	nb_valid += check(D)


print("## DAY 4 - PART 1 ##")
print("\t- Number of complete passports:",nb_complete)

print("## DAY 4 - PART 2 ##")
print("\t- Number of valid passports:",nb_valid)
input()