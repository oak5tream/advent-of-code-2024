# FIXME - THIS ONE IS A MESS WITH MULTIPLE REWRITES. CLEAN IT UP SOME DAYS!

import itertools

L = [list(c.strip()) for c in open("data/day21.txt", "r")]

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

DIRECTIONS = {'^': 0 - 1 * 1j, '>': 1 + 0 * 1j, 'v': 0 + 1 * 1j, '<': -1 + 0 * 1j}

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
	else:
		print("FFAAAIIL", step, direction)

#@functools.lru_cache()
def press_dir_pad(kp_dir, level, button, code0, code1, cache):
#	kp_dir = from_cache(kp_dir_str)
#def press_dir_pad(kp_dir, kp_dir_steps, level, button, output, cache):
#	print(kp_dir)
#	kp_dir_cache = ''.join(kp_dir)
#	kp_dir_cache = kp_dir_cache[level:]
#	for i in range(24 - level):
#		kp_dir_cache += 'A'
	if (level, code0, code1) in cache:
		print("Cache for", button, level, code0, code1)
		return cache[(level, code0, code1)]

#	print("Directional level", level, KP_DIR_VAL[kp_dir[level]], kp_dir[level], " -> ", button, KP_DIR_VAL[button])
	num_pressed = 0

	if level == 2:
#		print("PRESSING", button, kp_dir)
#		output.append(button)
		return 1

	prev_kp_dir = 'A'
	if kp_dir[level] != button:
		directions = list(KP_DIR_MAP[(kp_dir[level], button)])

		for i in range(len(directions)):
			direction = directions[i]
			#		for direction in directions:
#			print("direction for level", level)
#			print(direction)
#			print("Before", kp_dir[level])
			prev_kp_dir = 'A' if i == 0 else kp_dir[level]
			kp_dir[level] = get_next_dir_step(kp_dir[level], direction)
#			kp_dir[level] = direction #get_next_dir_step(kp_dir[level], direction)
#			print("After", kp_dir[level])
			num_pressed += press_dir_pad(kp_dir, level + 1, direction, prev_kp_dir, kp_dir[level], cache)
#			num_pressed += press_dir_pad(kp_dir, level + 1, direction, kp_dir[level], direction, cache)
#			prev_code = kp_dir[level]

	num_pressed += press_dir_pad(kp_dir, level + 1, 'A', prev_kp_dir, 'A', cache)

#	kp_dir_cache = ''.join(kp_dir)
#	kp_dir_cache = kp_dir_cache[level:]
	cache[(level, code0, code1)] = num_pressed

	return num_pressed

def traverse(level, max_level, key_src, key_dst, cache):
	if (level, key_src, key_dst) in cache:
		return cache[(level, key_src, key_dst)]

	kp, kp_val = (KP_NUM, KP_NUM_VAL) if level == 0 else (KP_DIR, KP_DIR_VAL)
	pos_src = kp_val[key_src]
	pos_dst = kp_val[key_dst]
	diff = pos_dst - pos_src
	path = []

	if level == max_level - 1:
		return abs(int(diff.real)) + 1 + abs(int(diff.imag))

	for _ in range(abs(int(diff.real))):
		path.append('<' if diff.real < 0 else '>')

	for _ in range(abs(int(diff.imag))):
		path.append('^' if diff.imag < 0 else 'v')

	if len(path) == 0:
		return 1

	results = []

	for p in set(itertools.permutations(path)):
		pos = pos_src
		steps = 0

		for i, direction in enumerate(p):
			key_next = 'A' if i == 0 else p[i - 1]
			
			steps += traverse(level + 1, max_level, key_next, direction, cache)
			pos += DIRECTIONS[direction]

			if pos not in kp:
				break
		else:
			steps += traverse(level + 1, max_level, p[-1], 'A', cache)
			results.append(steps)

	result = min(results)
	cache[(level, key_src, key_dst)] = result

	return result


def solve(levels):
	all_num_pressed = []
	cache = {}

	for codes in L:
		num_pressed = traverse(0, levels, 'A', codes[0], cache)

		for i in range(1, len(codes)):
			num_pressed += traverse(0, levels, codes[i - 1], codes[i], cache)

		all_num_pressed.append(num_pressed)

	result = 0

	for i in range(len(L)):
		result += int("".join(L[i]).replace("A", "")) * all_num_pressed[i]

	return result

def solve_part1():
	all_num_pressed = []
	cache = {}

	for codes in L:
		kp_num = 'A'
		kp_dir = ['A'] * 26
		num_pressed = 0
		prev_code = kp_num
		
		for i in range(len(codes)):
			code = codes[i]
#			cache = {}

			print("Codes", code)
			if kp_num == code:
				continue

			directions = list(KP_DIR_MAP[(kp_num, code)])
#			print(directions)

#			for direction in directions:
			for i in range(len(directions)):
				direction = directions[i]
				prev_code = 'A' if i == 0 else codes[i - 1]
				kp_num = get_next_num_step(kp_num, direction)
#				kp_num = direction #get_next_num_step(kp_num, direction)
#				print("num pad", kp_dir, direction)
				print("kp_num", kp_num)
				num_pressed_temp = press_dir_pad(kp_dir, 0, direction, prev_code, code, cache)
				num_pressed += num_pressed_temp

			prev_code = code
			print("FINAL", kp_dir)
			num_pressed += press_dir_pad(kp_dir, 0, 'A', prev_code, 'A', cache)

		all_num_pressed.append(num_pressed)

	result = 0

	for i in range(len(L)):
		result += int("".join(L[i]).replace("A", "")) * all_num_pressed[i]#len(outputs[i])

	return result

#print(solve_part1())

print(solve(3))
print(solve(26))
