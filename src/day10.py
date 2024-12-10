G = {}

for y, line in enumerate(open("data/day10.txt", "r")):
	for x, c in enumerate(list(line.strip())):
		if c != '.':
			G[x + y * 1j] = int(c)

def calculate_score(pos, height, paths):
	score = 0

	if G[pos] != height:
		return 0

	if height == 9:
		paths[pos] = True
		score += 1
	else:
		for delta in [-1, 1, -1j, 1j]:
			neighbour = pos + delta
			if neighbour in G:
				score += calculate_score(neighbour, height + 1, paths)

	return score

def solve():
	score_part1 = 0
	score_part2 = 0

	for pos in G:
		if G[pos] == 0:
			paths = {}
			score_part2 += calculate_score(pos, 0, paths)
			score_part1 += len(paths)

	return score_part1, score_part2

def solve_part2():
	score = 0

	for pos in G:
		if G[pos] == 0:
			score += calculate_score(pos, 0, {})

	return score

score_part1, score_part2 = solve()

print(score_part1)
print(score_part2)
