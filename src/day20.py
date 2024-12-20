from heapq import heappop, heappush

G = {}
X_MAX = 0
Y_MAX = 0
START_POS = 0
END_POS = 0

for y, line in enumerate(open("data/day20.txt", "r")):
	for x, c in enumerate(list(line.strip())):
		coord = x + y * 1j

		if c == 'S':
			START_POS = coord
		elif c == 'E':
			END_POS = coord
		elif c == '#':
			G[coord] = True

		X_MAX = max(X_MAX, x + 1)
	Y_MAX = max(Y_MAX, y + 1)

def print_grid():
	for y in range(Y_MAX):
		output = ""

		for x in range(X_MAX):
			coord = x + y * 1j

			if coord == START_POS:
				output += "S"
			elif coord == END_POS:
				output += "E"
			else:
				output += "#" if coord in G else "."

		print(output)

def get_path(grid, start, end):
	queue = []
	heap_id = 1

	heappush(queue, (0, start, 0))
	min_steps = 1000000000
	path = {}

	while queue:
		(_, pos, steps) = heappop(queue)

		if pos == end:
			min_steps = min(min_steps, steps)
			path[pos] = min_steps
			continue

		if pos in path and path[pos] <= steps:
			continue

		path[pos] = steps

		for step in [-1j, 1 + 0 * 1j, 1j, -1 + 0 * 1j]:
			if pos + step not in grid:
				heap_id += 1
				heappush(queue, (heap_id, pos + step, steps + 1))

	return path

def get_savings():
	path = get_path(G, START_POS, END_POS)
	checked = {}
	savings = {}

	for p0, s0 in path.items():
		for p1, s1 in path.items():
			if p0 != p1 and (p0 not in checked or checked[p0] == p1) and (p1 not in checked or checked[p1] == p0):
				continue

			checked[p0] = p1

			distance = abs(p1.real - p0.real) + abs(p1.imag - p0.imag)

			if s1 - s0 - distance > 1:
				if not distance in savings:
					savings[distance] = []

				savings[distance].append(s1 - s0)

	return savings

def solve():
	savings = get_savings()
	r0, r1 = 0, 0

	for distance, savings in savings.items():
		if distance == 2:
			for saving in savings:
				if saving - distance >= 100:
					r0 += 1

		if distance <= 20:
			for saving in savings:
				if saving - distance >= 100:
					r1 += 1
	
	return r0, r1

part1, part2 = solve()
print(part1)
print(part2)
