import re

def get_input():
	parsing_inputs = True
	inputs = {}
	gates = {}

	for line in open("data/day24.txt"):
		line = line.strip()

		if line == "":
			parsing_inputs = False
		elif parsing_inputs:
			a, b = line.split(': ')
			inputs[a] = int(b)
		else:
			a, b = line.split(' -> ')
			x, y, z = a.split(' ')
			gates[(x, y, z, b)] = False

	return inputs, gates

def is_complete(gates):
	for (_, _, _, out), val in gates.items():
		if out.startswith('z') and val == False:
			return False

	return True

def execute(op, v0, v1):
	result = -1

	if op == 'AND':
		result = v0 & v1
	elif op == 'OR':
		result = v0 | v1
	elif op == 'XOR':
		result = v0 ^ v1

	return result

def solve_part1():
	inputs, gates = get_input()

	while not is_complete(gates):
		for gate in gates.keys():

			if gate[0] in inputs and gate[2] in inputs:
				output = execute(gate[1], inputs[gate[0]], inputs[gate[2]])
				inputs[gate[3]] = output
				gates[gate] = True

	result = 0
	
	for k, v in inputs.items():
		if k.startswith('z') and v == 1:
			result += 2 ** int(k[-2:])

	return result

def get_gates():
	gates = []

	for line in open("data/day24.txt"):
		line = line.strip()
		m = re.search("([a-z0-9]+) ([A-Z]+) ([a-z0-9]+) -> ([a-z0-9]+)", line)
		if m:
			gates.append((m.group(1), m.group(2), m.group(3), m.group(4)))

	return gates

def solve_part2():
	result = []

	for (a, op, b, c) in get_gates():
		# Every XOR should have x or y for input, or z for output
		if op == 'XOR' and a[0] not in 'xyz' and b[0] not in 'xyz' and c[0] not in 'xyz':
			result.append(c)

		# Every z out should be XOR except for z45 (MSB)
		if op != 'XOR' and c.startswith('z') and c != 'z45':
			result.append(c)

	# Input of OR should always be input of AND except for x00 AND y00 (LSB)
	or_input = []
	and_output = []

	for (a, op, b, c) in get_gates():
		if op == 'OR':
			or_input.append(a)
			or_input.append(b)
		elif op == 'AND' and a != 'x00' and b != 'y00':
				and_output.append(c)

	or_input = sorted(set(or_input))
	and_output = sorted(set(and_output))

	result += list(set(or_input).difference(and_output))
	result += list(set(and_output).difference(or_input))
	
	return ','.join(sorted(set(result)))

print(solve_part1())
print(solve_part2())
