import math

def parse_input():
	p, v = [], []
	for line in open("data/day14.txt", "r"):
		pv = line.strip().split(" ")
		p.append(list(map(int, pv[0].replace("p=", "").split(","))))
		v.append(list(map(int, pv[1].replace("v=", "").split(","))))

	return p, v

def print_grid(grid, width, height):
	for y in range(height):
		output = ""
		
		for x in range(width):
			num = grid[y][x]
			output += str(num) if num > 0 else "."

		print(output)

def solve_part1(width, height):
	p, v = parse_input()

	grid = [[0] * width for _ in range(height)]

	for _ in range(100):
		grid = [[0] * width for _ in range(height)]

		for i in range(len(p)):
			p[i][0] = (p[i][0] + v[i][0]) % width
			p[i][1] = (p[i][1] + v[i][1]) % height
			grid[p[i][1]][p[i][0]] += 1

	h_w = int((width - 1) / 2)
	h_h = int((height - 1) / 2)
	quadrants = [0, 0, 0, 0]

	for y in range(height):
		for x in range(width):
			if x < h_w and y < h_h:
				quadrants[0] += grid[y][x]
			elif x > h_w and y < h_h:
				quadrants[1] += grid[y][x]
			elif x < h_w and y > h_h:
				quadrants[2] += grid[y][x]
			elif x > h_w and y > h_h:
				quadrants[3] += grid[y][x]

	return math.prod(quadrants)

def solve_part2(width, height):
	p, v = parse_input()

	for n in range(10000):
		grid = [[0] * width for _ in range(height)]

		for i in range(len(p)):
			p[i][0] = (p[i][0] + v[i][0]) % width
			p[i][1] = (p[i][1] + v[i][1]) % height
			grid[p[i][1]][p[i][0]] += 1

		for y in range(height):
			num_consecutive = 0
			
			for x in range(width):
				num_consecutive += 1

				if grid[y][x] == 0:
					num_consecutive = 0

				if num_consecutive > 15:
					print_grid(grid, width, height)
					return n + 1

print(solve_part1(101, 103))
print(solve_part2(101, 103))
