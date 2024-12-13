import re
import z3

L = []
claw = {}

for i, line in enumerate(open("data/day13.txt", "r")):
	if i % 4 == 0:
		m = re.search("X\+([0-9]+).*Y\+([0-9]+)", line)
		if m:
			claw["a"] = {"x": int(m.group(1)), "y": int(m.group(2))}
		else:
			print("Error parsing button A")
	elif i % 4 == 1:
		m = re.search("X\+([0-9]+).*Y\+([0-9]+)", line)
		if m:
			claw["b"] = {"x": int(m.group(1)), "y": int(m.group(2))}
		else:
			print("Error parsing button B")
	elif i % 4 == 2:
		m = re.search("X=([0-9]+).*Y=([0-9]+)", line)
		if m:
			claw["price"] = {"x": int(m.group(1)), "y": int(m.group(2))}
		else:
			print("Error parsing price")

		L.append(claw)
		claw = {}

def solve(price_offset):
	result = 0

	for claw in L:
		m, n = z3.Int('m'), z3.Int('n')

		s = z3.Optimize()

		s.add(m >= 0)
		s.add(n >= 0)
		s.add(m * claw["a"]["x"] + n * claw["b"]["x"] == claw["price"]["x"] + price_offset)
		s.add(m * claw["a"]["y"] + n * claw["b"]["y"] == claw["price"]["y"] + price_offset)

		minimize = s.minimize(3 * m + n)
		
		s.check()
		s.lower(minimize)
		
		answer = s.model()

		if answer[m] != None:
			result += 3 * answer[m].as_long() + answer[n].as_long()
		
	return result

def solve_part1():
	return solve(0)

def solve_part2():
	return solve(10000000000000)

print(solve_part1())
print(solve_part2())
