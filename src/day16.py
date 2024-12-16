from heapq import heappop, heappush

G = {}
START_POS = 0
END_POS = 0
X_MAX = 0
Y_MAX = 0

for y, line in enumerate(open("data/day16.txt", "r")):
	for x, c in enumerate(list(line.strip())):
		coord = x + y * 1j

		if c == 'S':
			START_POS = coord
		elif c == 'E':
			END_POS = coord
		elif c == '#':
			G[coord] = c

		X_MAX = max(X_MAX, x + 1)
	Y_MAX = max(Y_MAX, y + 1)

def print_grid(pos):
	output = ""

	for y in range(Y_MAX):
		output = ""

		for x in range(X_MAX):
			coord = x + y * 1j

			if coord == pos:
				output += "X"
			elif coord == START_POS:
				output += "S"
			elif coord == END_POS:
				output += "E"
			elif coord in G:
				output += G[coord]
			else:
				output += " "

		print(output)

def solve(pos, dir, num_with_score = -1):
	queue = []
	heap_id = 0
	path = [pos]

	heappush(queue, (heap_id, pos, dir, 0, path))
	min_score = 1000000000
	visited = {}
	best_tiles = {}

	while queue:
		(_, pos, dir, score, path) = heappop(queue)

		if pos == END_POS:
			path.append(pos)

			if num_with_score and num_with_score == score:
				for p in path:
					best_tiles[p] = True

			min_score = min(min_score, score)
			continue

		if (pos, dir) in visited and visited[(pos, dir)] < score:
			continue

		visited[(pos, dir)] = score

		for d in [dir, dir * 1j, dir * -1j]:
			if pos + d not in G:
				heap_id += 1
				heappush(queue, (heap_id, pos + d, d, score + 1 if dir == d else score + 1001, path + [pos]))

	return min_score, len(best_tiles.keys())
				
min_score, _ = solve(START_POS, 1 + 0 * 1j)
print(min_score)

_, num_best_tiles = solve(START_POS, 1 + 0 * 1j, min_score)
print(num_best_tiles)
