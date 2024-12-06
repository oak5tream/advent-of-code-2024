L = [c.split() for c in open("data/day01.txt", "r")]

def solve_part1():
	a1 = sorted([int(a[0]) for a in L])
	a2 = sorted([int(a[1]) for a in L])

	result = 0

	for i in range(len(a1)):
		result += abs(a1[i] - a2[i])

	return result

def solve_part2():
	a1 = [int(a[0]) for a in L]
	a2 = [int(a[1]) for a in L]

	c = {}
	for x in a2:
		c[x] = c[x] + 1 if x in c else 1

	result = 0

	for a in a1:
		result += a * c[a] if a in c else 0

	return result


print(solve_part1())
print(solve_part2())
