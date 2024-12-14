H = {}
X_MAX = 0
Y_MAX = 0

for y, line in enumerate(open("data/day08.txt", "r")):
	for x, c in enumerate(list(line.strip())):
		if c != '.':
			H[x + y * 1j] = c

		X_MAX = max(X_MAX, x + 1)
	Y_MAX = max(Y_MAX, y + 1)

def debug_print(antinodes):
	print("START DEBUG PRINT")

	for y in range(Y_MAX):
		output = ""

		for x in range(X_MAX):
			coord = x + y * 1j

			if coord in H:
				output += H[coord]
			elif coord in antinodes:
				output += antinodes[coord]
			else:
				output += "."

		print(output)
	
	print("END DEBUG PRINT")

def solve_part1():
	antinodes = {}

	for c1 in H:
		for c0 in H:
			if c0 != c1 and H[c0] == H[c1]:
				a = c1 - 2 * (c1 - c0)

				if a.real >= 0 and a.real < X_MAX and a.imag >= 0 and a.imag < Y_MAX:
					antinodes[a] = '#'

#	debug_print(antinodes)

	return len(antinodes)

def solve_part2():
	antinodes = {}

	for c1 in H:
		for c0 in H:
			if c0 != c1 and H[c0] == H[c1]:
				for i in range(-50, 50):
					a = c1 - i * (c1 - c0)

					if a.real >= 0 and a.real < X_MAX and a.imag >= 0 and a.imag < Y_MAX:
						antinodes[a] = '#'
						antinodes[c0] = '#'
						antinodes[c1] = '#'

#	debug_print(antinodes)

	return len(antinodes)

print(solve_part1())
print(solve_part2())
