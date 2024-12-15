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
	
def push(grid, pos, step, wide, updated):
	next_pos = pos + step
	did_push = False

	def store_updated(grid, pos, updated):
		if not pos in updated:
			updated[pos] = grid[pos] if pos in grid else 1000 + 1000 * 1j

	if wide and step.real == 0:
		left_next_pos = next_pos if grid[pos] == '[' else next_pos - 1
		right_next_pos = next_pos if grid[pos] == ']' else next_pos + 1

		if left_next_pos not in grid and right_next_pos not in grid:
			did_push = True
		elif left_next_pos in grid and grid[left_next_pos] == '[':
			if push(grid, left_next_pos, step, wide, updated):
				did_push = True
		elif left_next_pos in grid and grid[left_next_pos] == ']' and not right_next_pos in grid:
			if push(grid, left_next_pos, step, wide, updated):
				did_push = True
		elif not left_next_pos in grid and right_next_pos in grid and grid[right_next_pos] == '[':
			if push(grid, right_next_pos, step, wide, updated):
				did_push = True
		elif left_next_pos in grid and grid[left_next_pos] == ']' and right_next_pos in grid and grid[right_next_pos] == '[':
			if push(grid, left_next_pos, step, wide, updated) and push(grid, right_next_pos, step, wide, updated):
				did_push = True
	else:
		if next_pos not in grid:
			did_push = True
		elif grid[next_pos] in ['O', '[', ']']:
			if push(grid, next_pos, step, wide, updated):
				did_push = True

	if did_push:
		if wide and step.real == 0:
			left_pos = pos if grid[pos] == '[' else pos - 1
			right_pos = pos if grid[pos] == ']' else pos + 1
			left_next_pos = next_pos if grid[pos] == '[' else next_pos - 1
			right_next_pos = next_pos if grid[pos] == ']' else next_pos + 1

			store_updated(grid, left_pos, updated)
			store_updated(grid, right_pos, updated)
			store_updated(grid, left_next_pos, updated)
			store_updated(grid, right_next_pos, updated)

			grid[left_next_pos] = grid[left_pos]
			grid[right_next_pos] = grid[right_pos]
			del grid[left_pos]
			del grid[right_pos]
		else:
			store_updated(grid, pos, updated)
			store_updated(grid, pos, updated)

			grid[next_pos] = grid[pos]
			del grid[pos]

	return did_push

def move(grid, pos, step, wide):
	next_pos = pos + step
	did_move = False

	if next_pos not in grid:
		did_move = True
	elif grid[next_pos] in ['O', '[', ']']:
		updated = {}
		did_move = push(grid, next_pos, step, wide, updated)

		# Revert everything if we didn't move next_pos, but some underlying boxes did
		if not did_move and len(updated.keys()) > 0:
			for k, v in updated.items():
				if v == 1000 + 1000 * 1j:
					del grid[k]
				else:
					grid[k] = v

	return did_move

def get_gps_sum(grid, max_pos, wide):
	result = 0

	for y in range(max_pos[1]):
		for x in range(max_pos[0]):
			coord = x + y * 1j
			box = '[' if wide else 'O'

			if coord in grid and grid[coord] == box:
				result += 100 * y + x
	
	return result

def solve(wide):
	grid, start_pos, steps, max_pos = parse_input(wide)

	pos = start_pos

	for step in steps:
		if move(grid, pos, step, wide):
			pos += step

	return get_gps_sum(grid, max_pos, wide)

print(solve(False))
print(solve(True))
