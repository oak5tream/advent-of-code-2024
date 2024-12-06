G = [c.split() for c in open("data/day02.txt", "r")]

def is_safe(r):
	inc = r[1] > r[0]
	safe = True

	for i in range(len(r) - 1):
		c0 = (r[i + 1] > r[i] and inc) or (r[i + 1] < r[i] and not inc)
		diff = abs(r[i + 1] - r[i]) 
		c1 = diff >= 1 and diff <= 3

		if not c0 or not c1:
			safe = False
			break

	return safe
	
def solve_part1():
	result = 0

	for l in G:
		safe = is_safe(list(map(int, l)))

		if safe:
			result += 1

	return result

def solve_part2():
	result = 0

	for l in G:
		report = list(map(int, l))
		safe = is_safe(report)

		if safe:
			result += 1
		else:
			for i in range(len(report)):
				report_v2 = report.copy()
				del report_v2[i]

				if is_safe(report_v2):
					result += 1
					break

	return result

print(solve_part1())
print(solve_part2())
