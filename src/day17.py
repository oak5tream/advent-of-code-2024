def parse_input():
	reg = [0] * 3
	prg = ""

	for i, line in enumerate(open("data/day17.txt", "r")):
		if line.strip() != "":
			val = line.strip().split(": ")[1]

			if i < 3:
				reg[i] = int(val)
			elif i == 4:
				prg = list(map(int, val.split(",")))

	return reg, prg

def run(reg, prg):
	pc = 0
	running = True
	output = []

	def get_combo_operand(val, reg):
		if val == 4:
			val = reg[0]
		elif val == 5:
			val = reg[1]
		elif val == 6:
			val = reg[2]
		elif val == 7:
			print("ERROR: Unused combo operand 7")

		return val

	while running:
		opcode = prg[pc]
		operand = int(prg[pc + 1])

		if opcode == 0: # adv
			reg[0] //= 2 ** get_combo_operand(operand, reg)
		elif opcode == 1: # bxl
			reg[1] = reg[1] ^ operand
		elif opcode == 2: # bst
			reg[1] = get_combo_operand(operand, reg) & 7
		elif opcode == 3: # jnz
			pc = operand - 2 if reg[0] > 0 else pc
		elif opcode == 4: # bxc
			reg[1] ^= reg[2]
		elif opcode == 5: # out
			output.append(get_combo_operand(operand, reg) & 7)
		elif opcode == 6: # bdv
			reg[1] = reg[0] // 2 ** get_combo_operand(operand, reg)
		elif opcode == 7: # cdv
			reg[2] = reg[0] // 2 ** get_combo_operand(operand, reg)
		else:
			running = False
		
		pc += 2

		if pc >= len(prg):
			running = False

	return output

def solve_part1():
	reg, prg = parse_input()

	return ",".join(map(str, run(reg, prg)))

def solve_part2():
	_, prg = parse_input()
	factors = [0] * len(prg)

	reg_a = 0
	while True:
		reg_a = 0

		for i, f in enumerate(factors):
			reg_a += (8 ** i) * f

		output = run([reg_a, 0, 0], prg)

		if output == prg:
			return reg_a

		for i in reversed(range(len(prg))):
			if len(output) < i:
				factors[i] += 1
				break

			if output[i] != prg[i]:
				factors[i] += 1
				break

print(solve_part1())
print(solve_part2())
