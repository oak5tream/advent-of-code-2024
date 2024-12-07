g = [list(c.strip()) for c in open("data/day06.txt", "r")]
G = {}
START_POS = 0 + 0j
X_MAX = len(g[0])
Y_MAX = len(g)

for y in range(len(g)):
	for x in range(len(g[0])):
		c = g[y][x]
		if c == '#' or c == '.':
			G[x + y * 1j] = c
		elif c == '^':
			G[x + y * 1j] = '.'
			START_POS = x + y * 1j

def debug_print(grid, pos, history):
	print("START DEBUG PRINT")

	for y in range(Y_MAX):
		output = ""

		for x in range(X_MAX):
			coord = x + y * 1j

			if coord == pos:
				output += "X"
			elif coord in history:
				output += "@"
			elif grid[coord] == '#':
				output += "#"
			elif grid[coord] == '.':
				output += "."

		print(output)
	
	print("END DEBUG PRINT")


def solve(grid, history = {}):
	dir = -1j
	pos = START_POS
	loop = False

	while pos + dir in grid and not loop:
		if pos in history and history[pos] == dir:
			loop = True

		history[pos] = dir

		if grid[pos + dir] == "#":
			dir *= 1j
			if pos in history and history[pos] == dir:
				loop = True

		pos += dir

	return len(history.keys()) + 1, loop

def solve_part1():
	result, _ = solve(G)
	return result

def solve_part2():
	result = 0

	for y in range(Y_MAX):
		for x in range(X_MAX):
			pos = x + y * 1j
			grid = G.copy()
			grid[pos] = '#'
	
			_, loop = solve(grid, {})

			if loop:
				result += 1

	return result

print(solve_part1())
print(solve_part2())
