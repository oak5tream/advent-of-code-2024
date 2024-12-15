import pprint


def parse_input(wide):
	grid = {}
	start_pos = 0
	steps = []
	max_pos = [0, 0]

	for y, line in enumerate(open("data/day15.txt", "r")):
		if line[0] == '#':
			for x, c in enumerate(list(line.strip())):
				pos = x + y * 1j if not wide else x * 2 + y * 1j

				if c == '#':
					grid[pos] = c

					if wide:
						grid[pos + 1] = c
				elif c == 'O':
					if wide:
						grid[pos] = '['
						grid[pos + 1] = ']'
					else:
						grid[pos] = c
				elif c == '@':
					start_pos  = pos
				
				max_pos[0] = max(max_pos[0], x + 1)
		elif line.strip() == "":
			max_pos[1] = y
		else:
			step = 0

			for c in list(line.strip()):
				if c == '^':
					step = 0 - 1j
				elif c == '>':
					step = 1
				elif c == 'v':
					step = 0 + 1j
				elif c == '<':
					step = -1
				else:
					print("Error in input! Unknown direction", c)

				steps.append(step)

	if wide:
		max_pos[0] *= 2

	return grid, start_pos, steps, max_pos

def print_grid(grid, pos, max_pos):
	output = ""

	for y in range(max_pos[1]):
		output = ""

		for x in range(max_pos[0]):
			coord = x + y * 1j

			if coord == pos:
				output += '@'
			elif coord in grid:
				output += grid[coord]
			else:
				output += "."

		print(output)
	
def push(grid, pos, step):
	next_step = pos + step
	did_push = False

	if next_step not in grid:
		did_push = True
	elif grid[next_step] == 'O':
		if push(grid, next_step, step):
			did_push = True

	if did_push:
		grid[next_step] = grid[pos]
		del grid[pos]

	return did_push

def move(grid, pos, step):
	next_step = pos + step
	did_move = False

	if next_step not in grid:
		did_move = True
	elif grid[next_step] == 'O':
		did_move = push(grid, next_step, step)

	return did_move

def get_gps_sum(grid, max_pos):
	result = 0

	for y in range(max_pos[1]):
		for x in range(max_pos[0]):
			coord = x + y * 1j

			if coord in grid and grid[coord] == 'O':
				result += 100 * y + x
	
	return result

def solve(wide):
	grid, start_pos, steps, max_pos = parse_input(wide)

	pos = start_pos

	print_grid(grid, pos, max_pos)
	
	i = 0
	for step in steps:
		i += 1
		if move(grid, pos, step):
			pos += step

#		print("State", i)
#		print_grid(grid, pos, max_pos)

	return get_gps_sum(grid, max_pos)

print(solve(False))
#print(solve(True))
