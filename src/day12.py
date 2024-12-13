G = {}
X_MAX = 0
Y_MAX = 0

for y, line in enumerate(open("data/day12.txt", "r")):
	for x, c in enumerate(list(line.strip())):
		G[x + y * 1j] = c

		X_MAX = max(X_MAX, x + 1)
	Y_MAX = max(Y_MAX, y + 1)

def step_plots(pos, plant, region, plots):
	if G[pos] != plant or pos in plots[plant]:
		return
	else:
		plots[plant][pos] = region

	for delta in [-1, 1, -1j, 1j]:
		neighbour = pos + delta

		if neighbour in G:
			step_plots(neighbour, plant, region, plots)

def calculate_area(plants, region):
	area = 0

	for r in plants.values():
		if r == region:
			area += 1

	return area

def calculate_perimeter(plants, region):
	perimeter = 0

	for plant_pos, r in plants.items():
		if r == region:
			num_neighbours = 4

			for delta in [-1, 1, -1j, 1j]:
				if plant_pos + delta in plants:
					num_neighbours -= 1

			perimeter += num_neighbours

	return perimeter

def print_sides(sides, c):
	output = ""

	for y in range(Y_MAX):
		output = ""

		for x in range(X_MAX):
			coord = x + y * 1j

			if coord in sides:
				output += c
			else:
				output += " "

		print(output)
	

def calculate_sides(plants, region):
	U, R, D, L = 0, 1, 2, 3
	sides = [{}, {}, {}, {}]

	for plant_pos, r in plants.items():
		if r == region:
			if plant_pos - 1j not in plants:
				sides[U][plant_pos] = 1
			if plant_pos + 1 not in plants:
				sides[R][plant_pos] = 1
			if plant_pos + 1j not in plants:
				sides[D][plant_pos] = 1
			if plant_pos - 1 not in plants:
				sides[L][plant_pos] = 1

	num_sides = [0, 0, 0, 0]
	side_started = [False, False, False, False]

	for y in range(Y_MAX):
		for x in range(X_MAX):
			coord = x + y * 1j

			for i in [U, D]:
				if not side_started[i] and coord in sides[i]:
					side_started[i] = True
				elif side_started[i] and coord not in sides[i]:
					side_started[i] = False
					num_sides[i] += 1

		for i in [U, D]:
			if side_started[i]:
				side_started[i] = False
				num_sides[i] += 1

	for x in range(X_MAX):
		for y in range(Y_MAX):
			coord = x + y * 1j

			for i in [R, L]:
				if not side_started[i] and coord in sides[i]:
					side_started[i] = True
				elif side_started[i] and coord not in sides[i]:
					side_started[i] = False
					num_sides[i] += 1

		for i in [R, L]:
			if side_started[i]:
				side_started[i] = False
				num_sides[i] += 1

	return sum(num_sides)

def calculate_price(plants, region, deal):
	if deal:
		return calculate_area(plants, region) * calculate_sides(plants, region)
	else:
		return calculate_area(plants, region) * calculate_perimeter(plants, region)

def solve(deal):
	result = 0
	plots = {}
	region = 0

	for y in range(Y_MAX):
		for x in range(X_MAX):
			pos = x + y * 1j
			plant = G[pos]

			if plant not in plots:
				plots[plant] = {}
				step_plots(pos, plant, region, plots)
				result += calculate_price(plots[plant], region, deal)
				region += 1
			elif plant in plots and pos not in plots[plant]:
				# Found existing plant in a new plot outside of the first plot. Add it using another region.
				step_plots(pos, plant, region, plots)
				result += calculate_price(plots[plant], region, deal)
				region += 1


	return result

def solve_part1():
	return solve(False)

def solve_part2():
	return solve(True)

print(solve_part1())
print(solve_part2())
