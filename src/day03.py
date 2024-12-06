import re

L = "".join([c.strip() for c in open("data/day03.txt", "r")]) + "do()"

def solve(line):
	result = 0

	m0 = re.findall("mul\(\d+,\d+\)", line, re.M)
	for mul in m0:
		m1 = re.search("(\d+),(\d+)", mul)
		if m1:
			result += int(m1.group(1)) * int(m1.group(2))

	return result

	
def solve_part1():
	return solve(L)

def solve_part2():
	removed = True
	memory = L

	while removed:
		dont = memory.find("don't()")
		do = memory.find("do()")

		if dont != -1 and do != -1:
			if do < dont:
				memory = memory[:do] + memory[do+4:]
			else:
				memory = memory[:dont] + memory[do+4:]
		else:
			removed = False

	return solve(memory)


print(solve_part1())
print(solve_part2())
