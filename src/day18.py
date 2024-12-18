from heapq import heappop, heappush

L = []
X_MAX = 0
Y_MAX = 0
NOT_FOUND = 1000000000

for line in open("data/day18.txt", "r"):
	x, y = map(int, line.strip().split(","))
	L.append(x + y  * 1j)

	X_MAX = max(X_MAX, x + 1)
	Y_MAX = max(Y_MAX, y + 1)

def print_grid(grid):
	for y in range(Y_MAX):
		output = ""

		for x in range(X_MAX):
			output += grid[x + y * 1j]

		print(output)

def get_num_steps(grid, start, end): # Bad name. Find end?
	queue = []
	heap_id = 1

	heappush(queue, (0, start, 0))
	min_steps = NOT_FOUND 
	visited = {}

	while queue:
		(_, pos, steps) = heappop(queue)

		if pos == end:
			min_steps = min(min_steps, steps)
			continue

		if pos in visited and visited[pos] <= steps:
			continue

		visited[pos] = steps

		for dir in [-1j, 1 + 0 * 1j, 1j, -1 + 0 * 1j]:
			if pos + dir in grid and grid[pos + dir] == '.': # LAST ONE JUST FOR TESTING SPEED
				heap_id += 1
				heappush(queue, (heap_id, pos + dir, steps + 1))

	return min_steps

def solve_part1():
	grid = {}

	for i in range(1024):
		grid[L[i]] = '#'

	for y in range(Y_MAX):
		for x in range(X_MAX):
			pos = x + y * 1j
			if pos not in grid:
				grid[pos] = '.'

	return get_num_steps(grid, 0 + 0 * 1j, ((X_MAX - 1) + (Y_MAX - 1) * 1j))

def solve_part2():
	m, n = 1025, len(L)

	while True:
		grid = {}
		num_bytes = (m + n) // 2
		steps = 0

		for i in range(num_bytes):
			grid[L[i]] = '#'

		for y in range(Y_MAX):
			for x in range(X_MAX):
				pos = x + y * 1j
				if pos not in grid:
					grid[pos] = '.'

		steps = get_num_steps(grid, 0 + 0 * 1j, ((X_MAX - 1) + (Y_MAX - 1) * 1j))

		if steps == NOT_FOUND:
			n = num_bytes
		else:
			m = num_bytes

			if n - m == 1:
				return str(int(L[m].real)) + "," + str(int(L[m].imag))

print(solve_part1())
print(solve_part2())
