D = []

for line in open("data/day09.txt", "r"):
	D = list(map(int, line.strip()))

def init_mem():
	mem = []

	file_block = True
	file_index = 0

	for d in D:
		if file_block:
			mem.extend([file_index] * d)
			file_index += 1
		else:
			mem.extend([-1] * d)

		file_block = not file_block

	return mem, file_index - 1

def get_checksum(mem):
	result = 0

	for i, m in enumerate(mem):
		if m > -1:
			result += i * m

	return result

def solve_part1():
	mem, _ = init_mem()

	defrag_complete = False

	while not defrag_complete:
		last_block_index = -1

		for i in reversed(range(len(mem))):
			if mem[i] != -1:
				last_block_index = i
				break

		first_empty_index = mem.index(-1)

		if last_block_index < first_empty_index:
			defrag_complete = True
		else:
			mem[first_empty_index] = mem[last_block_index]
			mem[last_block_index] = -1

	return get_checksum(mem)

def solve_part2():
	mem, max_file_id = init_mem()

	def get_block(mem, file_id):
		start_index = -1
		end_index = -1
		length = -1

		for i in reversed(range(len(mem))):
			if end_index == -1:
				if mem[i] == file_id:
					end_index = i
			elif mem[i] != file_id:
				start_index = i + 1
				length = end_index - start_index + 1

				return start_index, length

		return -1, -1

	def get_first_empty_slot(mem, length):
		empty_index = -1
		empty_length = -1

		for i in range(len(mem)):
			if empty_length == length:
				return empty_index

			if empty_index == -1:
				if mem[i] == -1:
					empty_index = i
					empty_length = 1
			else:
				if mem[i] == -1:
					empty_length += 1
				else:
					empty_index = -1

		return -1

	file_id = max_file_id

	while file_id >= 0:
		start_index, length = get_block(mem, file_id)

		empty_index = get_first_empty_slot(mem, length)
		
		if empty_index != -1 and start_index > empty_index:
			for i in range(empty_index, empty_index + length):
				mem[i] = file_id

			for i in range(start_index, start_index + length):
				mem[i] = -1

		file_id -= 1

	return get_checksum(mem)

print(solve_part1())
print(solve_part2())
