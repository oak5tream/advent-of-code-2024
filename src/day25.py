def get_input():
	keys, locks = [], []
	block = []

	def add_block(block, keys, locks):
		lock = False

		if block[0][0] == '#':
			lock = True

		lengths = []

		for x in range(len(block[0])):
			for y in range(1, len(block)):
				if lock and block[y][x] == '.':
					lengths.append(y - 1)
					break
				elif not lock and block[y][x] == '#':
					lengths.append(len(block) - y - 1)
					break

		if lock:
			locks.append(lengths)
		else:
			keys.append(lengths)

	for line in open("data/day25.txt"):
		line = line.strip()

		if line == "":
			add_block(block, keys, locks)
			block = []
		else:
			block.append(line)

	add_block(block, keys, locks)

	return keys, locks

def solve():
	keys, locks = get_input()

	result = 0

	for lock in locks:
		for key in keys:
			fit = True

			for i in range(len(lock)):
				if key[i] + lock[i] > 5:
					fit = False
			
			result += 1 if fit else 0

	return result

print(solve())
