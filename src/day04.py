G = [list(c.strip()) for c in open("data/day04.txt", "r")]

def inside(x, y):
	return x >= 0 and x < len(G[0]) and y >= 0 and y < len(G)

def solve_part1():
	xmas = "XMAS"
	result = 0

	for y in range(len(G)):
		for x in range(len(G[0])):

			for step in [
					(-1, -1),
					(0, -1),
					(1, -1),
					(1, 0),
					(1, 1),
					(0, 1),
					(-1, 1),
					(-1, 0)
					]:

				found_xmas = True
				
				for i in range(4):
					n_x = x + step[0] * i
					n_y = y + step[1] * i

					if not inside(n_x, n_y) or G[n_y][n_x] != xmas[i]:
						found_xmas = False

				if found_xmas:
					result += 1

	return result

def solve_part2():
	result = 0

	for y in range(len(G)):
		for x in range(len(G[0])):

			in_bounds = True

			if G[y][x] == 'A':
				n_x = [x - 1, x + 1, x + 1, x - 1] 
				n_y = [y - 1, y - 1, y + 1, y + 1] 

				for i in range(4):
					if not inside(n_x[i], n_y[i]):
						in_bounds = False

				if in_bounds:
					l_mas = G[n_y[0]][n_x[0]] == 'M' and G[n_y[2]][n_x[2]] == 'S'
					l_sam = G[n_y[0]][n_x[0]] == 'S' and G[n_y[2]][n_x[2]] == 'M'
					r_mas = G[n_y[1]][n_x[1]] == 'M' and G[n_y[3]][n_x[3]] == 'S'
					r_sam = G[n_y[1]][n_x[1]] == 'S' and G[n_y[3]][n_x[3]] == 'M'

					if (l_mas or l_sam) and (r_mas or r_sam):
						result += 1


	return result

print(solve_part1())
print(solve_part2())
