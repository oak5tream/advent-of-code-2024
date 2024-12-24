import functools
from heapq import heappop, heappush

L = [list(c.strip()) for c in open("data/day21_test.txt", "r")]

KP_NUM = dict([
	(0 + 0 * 1j, '7'), (1 + 0 * 1j, '8'), (2 + 0 * 1j, '9'),
	(0 + 1 * 1j, '4'), (1 + 1 * 1j, '5'), (2 + 1 * 1j, '6'),
	(0 + 2 * 1j, '1'), (1 + 2 * 1j, '2'), (2 + 2 * 1j, '3'),
	(1 + 3 * 1j, '0'), (2 + 3 * 1j, 'A')
	])

KP_NUM_VAL = {}

for k, v in KP_NUM.items():
	KP_NUM_VAL[v] = k

KP_DIR = dict([
	(1 + 0 * 1j, '^'), (2 + 0 * 1j, 'A'),
	(0 + 1 * 1j, '<'), (1 + 1 * 1j, 'v'), (2 + 1 * 1j, '>')
	])

KP_DIR_VAL = {}

KP_DIR_MAP = {
	('A', '0'): "<",
	('0', 'A'): ">",
	('A', '1'): "^<<",
	('1', 'A'): ">>v",
	('A', '2'): "<^",
	('2', 'A'): "v>",
	('A', '3'): "^",
	('3', 'A'): "v",
	('A', '4'): "^^<<",
	('4', 'A'): ">>vv",
	('A', '5'): "<^^",
	('5', 'A'): "vv>",
	('A', '6'): "^^",
	('6', 'A'): "vv",
	('A', '7'): "^^^<<",
	('7', 'A'): ">>vvv",
	('A', '8'): "<^^^",
	('8', 'A'): "vvv>",
	('A', '9'): "^^^",
	('9', 'A'): "vvv",
	('0', '1'): "^<",
	('1', '0'): ">v",
	('0', '2'): "^",
	('2', '0'): "v",
	('0', '3'): "^>",
	('3', '0'): "<v",
	('0', '4'): "^<^",
	('4', '0'): ">vv",
	('0', '5'): "^^",
	('5', '0'): "vv",
	('0', '6'): "^^>",
	('6', '0'): "<vv",
	('0', '7'): "^^^<",
	('7', '0'): ">vvv",
	('0', '8'): "^^^",
	('8', '0'): "vvv",
	('0', '9'): "^^^>",
	('9', '0'): "<vvv",
	('1', '2'): ">",
	('2', '1'): "<",
	('1', '3'): ">>",
	('3', '1'): "<<",
	('1', '4'): "^",
	('4', '1'): "v",
	('1', '5'): "^>",
	('5', '1'): "<v",
	('1', '6'): "^>>",
	('6', '1'): "<<v",
	('1', '7'): "^^",
	('7', '1'): "vv",
	('1', '8'): "^^>",
	('8', '1'): "<vv",
	('1', '9'): "^^>>",
	('9', '1'): "<<vv",
	('2', '3'): ">",
	('3', '2'): "<",
	('2', '4'): "<^",
	('4', '2'): "v>",
	('2', '5'): "^",
	('5', '2'): "v",
	('2', '6'): "^>",
	('6', '2'): "<v",
	('2', '7'): "<^^",
	('7', '2'): "vv>",
	('2', '8'): "^^",
	('8', '2'): "vv",
	('2', '9'): "^^>",
	('9', '2'): "<vv",
	('3', '4'): "<<^",
	('4', '3'): "v>>",
	('3', '5'): "<^",
	('5', '3'): "v>",
	('3', '6'): "^",
	('6', '3'): "v",
	('3', '7'): "<<^^",
	('7', '3'): "vv>>",
	('3', '8'): "<^^",
	('8', '3'): "vv>",
	('3', '9'): "^^",
	('9', '3'): "vv",
	('4', '5'): ">",
	('5', '4'): "<",
	('4', '6'): ">>",
	('6', '4'): "<<",
	('4', '7'): "^",
	('7', '4'): "v",
	('4', '8'): "^>",
	('8', '4'): "<v",
	('4', '9'): "^>>",
	('9', '4'): "<<v",
	('5', '6'): ">",
	('6', '5'): "<",
	('5', '7'): "<^",
	('7', '5'): "v>",
	('5', '8'): "^",
	('8', '5'): "v",
	('5', '9'): "^>",
	('9', '5'): "<v",
	('6', '7'): "<<^",
	('7', '6'): "v>>",
	('6', '8'): "<^",
	('8', '6'): "v>",
	('6', '9'): "^",
	('9', '6'): "v",
	('7', '8'): ">",
	('8', '7'): "<",
	('7', '9'): ">>",
	('9', '7'): "<<",
	('8', '9'): ">",
	('9', '8'): "<",
	('<', '^'): ">^",
	('^', '<'): "v<",
	('<', 'v'): ">",
	('v', '<'): "<",
	('<', '>'): ">>",
	('>', '<'): "<<",
	('<', 'A'): ">>^",
	('A', '<'): "v<<",
	('^', 'v'): "v",
	('v', '^'): "^",
	('^', '>'): "v>",
	('>', '^'): "<^",
	('^', 'A'): ">",
	('A', '^'): "<",
	('v', '>'): ">",
	('>', 'v'): "<",
	('v', 'A'): "^>",
	('A', 'v'): "<v",
	('>', 'A'): "^",
	('A', '>'): "v"
	}

for k, v in KP_DIR.items():
	KP_DIR_VAL[v] = k

def print_keypads():
	print("NUMERIC")
	for y in range(4):
		output = ""

		for x in range(3):
			coord = x + y * 1j
			output += KP_NUM[coord] if coord in KP_NUM else " "

		print(output)

	print("DIRECTIONAL")
	for y in range(2):
		output = ""

		for x in range(3):
			coord = x + y * 1j
			output += KP_DIR[coord] if coord in KP_DIR else " "

		print(output)


#print_keypads()

def get_steps(grid, start, end):
	queue = []
	heap_id = 1

	heappush(queue, (0, start, 0, []))
	min_steps = 1000000000
	visited = {}
	path = []

	while queue:
		(_, pos, steps, path) = heappop(queue)

		if pos == end:
			min_steps = min(min_steps, steps)
			visited[pos] = min_steps
			return min_steps, path

		if pos in visited and visited[pos] <= steps:
			continue

		visited[pos] = steps

		for step in [-1j, 1 + 0 * 1j, 1j, -1 + 0 * 1j]:
			if pos + step in grid:
				heap_id += 1
				heappush(queue, (heap_id, pos + step, steps + 1, path + [pos + step]))


def calculate_steps(coords):
	result = {}

	for k0, v0 in coords.items():
		for k1, v1 in coords.items():
			if k0 == k1:
				continue

			result[(v0, v1)] = get_steps(coords, k0, k1)

	return result

def get_direction(p0, p1):
	if p0.real < p1.real:
		return '>'
	elif p0.real > p1.real:
		return '<'
	elif p0.imag < p1.imag:
		return 'v'
	elif p0.imag > p1.imag:
		return '^'
	else:
		print("ERROR: NO DIRECTION FOR", p0, p1)

def get_next_num_step(step, direction):
	pos = KP_NUM_VAL[step]
#	print(step, direction)

	if direction == '^':
		return KP_NUM[pos - 1j]
	elif direction == '>':
		return KP_NUM[pos + 1 + 0 * 1j]
	elif direction == 'v':
		return KP_NUM[pos + 1j]
	elif direction == '<':
		return KP_NUM[pos - 1 + 0 * 1j]

def get_next_dir_step(step, direction):
	pos = KP_DIR_VAL[step]
#	print(step, direction)

	if direction == '^':
		return KP_DIR[pos - 1j]
	elif direction == '>':
		return KP_DIR[pos + 1 + 0 * 1j]
	elif direction == 'v':
		return KP_DIR[pos + 1j]
	elif direction == '<':
		return KP_DIR[pos - 1 + 0 * 1j]

def to_cache(p):
	return ''.join(p)

def from_cache(p):
	return list(p)

#@functools.lru_cache()
def press_dir_pad(kp_dir, level, button, cache):
#	kp_dir = from_cache(kp_dir_str)
#def press_dir_pad(kp_dir, kp_dir_steps, level, button, output, cache):
	kp_dir_cache = ''.join(kp_dir)
#	kp_dir_cache = kp_dir_cache[level:]
	if (button, level, kp_dir_cache) in cache:
		print("Cache for", button, level, kp_dir_cache)
		return cache[(button, level, kp_dir_cache)]

#	print("Directional level", level, KP_DIR_VAL[kp_dir[level]], kp_dir[level], " -> ", button, KP_DIR_VAL[button])
	num_pressed = 0

	if level == 25:
		print("PRESSING", button, kp_dir)
#		output.append(button)
		return 1

	if kp_dir[level] != button:
#		_, dir_steps = kp_dir_steps[(kp_dir[level], button)]
		
#		directions = []
		directions = list(KP_DIR_MAP[(kp_dir[level], button)])
#		print("Directions for")
#		print(kp_dir[level], button)
#		print(directions)

#		for dir_step in dir_steps:
		for direction in directions:
#			direction = get_direction(KP_DIR_VAL[kp_dir[level]], dir_step)
#			kp_dir[level] = KP_DIR[dir_step]
			kp_dir[level] = get_next_dir_step(kp_dir[level], direction)
#			print("KP_DIR", kp_dir[level])
#			directions.append(direction)
#			print(direction)
		
#		for direction in sorted(directions):
			num_pressed += press_dir_pad(kp_dir, level + 1, direction, cache)

	num_pressed += press_dir_pad(kp_dir, level + 1, 'A', cache)

#	kp_dir_cache = ''.join(kp_dir)
#	kp_dir_cache = kp_dir_cache[level:]
#	print("Cache", kp_dir_cache, "level", level)
	cache[(button, level, kp_dir_cache)] = num_pressed

	return num_pressed

def solve_part1():
	kp_num_steps = calculate_steps(KP_NUM)
	kp_dir_steps = calculate_steps(KP_DIR)

#	print(KP_DIR_MAP[('0', '7')])

#	for k, v in kp_num_steps.items():
#		_, b = v
		
#		print(k)
#		for c in b:
#			print(c)

#	return []

#	outputs = []
	all_num_pressed = []
	cache = {}

	for codes in L:
		kp_num = 'A'
		kp_dir = ['A'] * 26
#		output = []
		num_pressed = 0
		
		for i, code in enumerate(codes):
#			print("Numerical   ", KP_NUM_VAL[kp_num], kp_num, " -> ", code, KP_NUM_VAL[code])
			print("Code", i, code)
#			_, numeric_steps = kp_num_steps[(kp_num, code)]
			directions = list(KP_DIR_MAP[(kp_num, code)])

#			directions = []

#			for numeric_step in numeric_steps:
			for direction in directions:
#				print("NUMERIC STEP")
#				direction = get_direction(KP_NUM_VAL[kp_num], numeric_step)
#				kp_num = KP_NUM[numeric_step]
#				print(direction)
#				directions.append(direction)
				kp_num = get_next_num_step(kp_num, direction)
				num_pressed_temp = press_dir_pad(kp_dir, 0, direction, cache)
				num_pressed += num_pressed_temp

				print("Direction", direction)
				print(kp_dir)
				print("num_pressed", num_pressed_temp)

#			for direction in sorted(directions):
#				press_dir_pad(kp_dir, kp_dir_steps, 0, direction, output)

			num_pressed += press_dir_pad(kp_dir, 0, 'A', cache)

		all_num_pressed.append(num_pressed)
#		outputs.append(output)

#	print("RESULT")
#	a = [
#			"<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
#			"<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
#			"<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
#			"<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
#			"<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"]

#	for i in range(len(result)):
#		print("Got num", len(result[i]), "expected", len(a[i]))
#		print("Got string:      " + "".join(result[i]))
#		print("Expected string: " + a[i])

	result = 0

	for i in range(len(L)):
		result += int("".join(L[i]).replace("A", "")) * all_num_pressed[i]#len(outputs[i])

	return result


#	print(code)
#	print(kp_num_steps[('7', '8')])
#	print(kp_dir_steps)

#	print("DIR TEST")
#	print("RIGHT", get_direction(1 + 1 * 1j, 2 + 1 * 1j))
#	print("DOWN", get_direction(1 + 1 * 1j, 1 + 2 * 1j))
#	print("LEFT", get_direction(2 + 1 * 1j, 1 + 1 * 1j))
#	print("UP", get_direction(1 + 1 * 1j, 1 + -1 * 1j))

#	min_steps, path = get_steps(KP_NUM, 0 + 2 + 3 * 1j, 0 + 0 * 1j)
#	print("min_steps", min_steps)
#	print("path", path)

print(solve_part1())

#t_str = "1234"
#level = 1
#print(t_str[level:])
#kp_dir_cache = kp_dir_cache[:level]
