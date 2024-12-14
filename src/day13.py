import numpy as np
import re
import z3

L = []
claw = {}

for i, line in enumerate(open("data/day13_test.txt", "r")):
	if i % 4 == 0:
		m = re.search("X\+([0-9]+).*Y\+([0-9]+)", line)
		if m:
			claw["a"] = {"x": int(m.group(1)), "y": int(m.group(2))}
	elif i % 4 == 1:
		m = re.search("X\+([0-9]+).*Y\+([0-9]+)", line)
		if m:
			claw["b"] = {"x": int(m.group(1)), "y": int(m.group(2))}
	elif i % 4 == 2:
		m = re.search("X=([0-9]+).*Y=([0-9]+)", line)
		if m:
			claw["price"] = {"x": int(m.group(1)), "y": int(m.group(2))}

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

# numpy test from #adventofcode
def solve_system():
	result = 0

	for claw in L:
		m = np.array([[claw["a"]["x"], claw["b"]["x"]], [claw["a"]["y"], claw["b"]["y"]]])
		v = np.array([claw["price"]["x"], claw["price"]["y"]])
		x, y = np.linalg.solve(m, v)
		x = round(x)
		y = round(y)

		if (claw["a"]["x"] * x + claw["b"]["x"] * y == claw["price"]["x"]) and (claw["a"]["y"] * x + claw["b"]["y"] * y == claw["price"]["y"]):
			result += int(3 * x + y)
	    
	return result

def solve_part1():
#	solve_system()
	return solve(0)

def solve_part2():
	return solve(10000000000000)

print(solve_part1())
print(solve_part2())
