L = [int(c.strip()) for c in open("data/day22.txt", "r")]

def get_next(n):
	b24 = 16777216
	n = (n ^ (n * 64)) % b24
	n = (n ^ (n // 32)) % b24
	n = (n ^ (n * 2048)) % b24

	return n

def solve():
	part1 = 0
	all_pc = []

	for n in L:
		pc = []

		for i in range(2000):
			p_n = n
			n = get_next(n)

			if i < 1999:
				pc.append({'p': n % 10, 'c': (n % 10) - (p_n % 10)})

		part1 += n

		all_pc.append(pc)

	sequences = {}
	for pc in all_pc:
		seen = {}

		for i in range(3, len(pc)):
			k = (pc[i - 3]['c'], pc[i - 2]['c'], pc[i - 1]['c'], pc[i]['c'])
			v = pc[i]['p']

			if not k in seen:
				seen[k] = True
				sequences[k] = sequences[k] + v if k in sequences else v

	return part1, max(sequences.values())

part1, part2 = solve()

print(part1)
print(part2)
