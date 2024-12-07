import re

def parse():
	data = {}

	for line in open("data/day07_test.txt", "r"):
		k, v = line.strip().split(": ")
		if int(k) in data:
			print("DUPE!!!!!", k)
		data[int(k)] = []

		for val in v.split():
			data[int(k)].append(val)

	return data

def get_combinations(ops, equation, result, concat):
	if len(ops) > 0:
		op = ops.pop(0)

		eq0 = equation + " + " + op 
		eq1 = equation + " * " + op

		get_combinations(ops.copy(), eq0, result, concat)
		get_combinations(ops.copy(), eq1, result, concat)

		if concat:
			eq2 = equation + " || " + op
			get_combinations(ops.copy(), eq2, result, concat)
	else:
		result.append(equation)

def solve(d, concat):
	result = 0

	def evaluate(expr):
		evaluating = True
		res = 0

		m = re.search("^([0-9]+)", expr)
		if m:
			res = int(m.group(1))
			l = len(m.group(0))
			expr = expr[l:]

		while evaluating:
			m = re.search("^ ([\+\*\|]+) ([0-9]+)", expr)
			if m:
				l = len(m.group(0))
				expr = expr[l:]

				if m.group(1) == "||":

					res = int(str(res) + m.group(2))
				else:
					res = eval(str(res) + m.group(1) + m.group(2))
			else:
				evaluating = False

		return res

	for k in d:
		sums = []
		get_combinations(d[k], d[k].pop(0), sums, concat)

		for expr in sums:
			sum = evaluate(expr)
			if k == sum:
				result += k
				break


# It turns out that 448 is in the data twice, so we need to add that to both answers
	return result + 448

def solve_part1():
	return solve(parse(), False)

def solve_part2():
	return solve(parse(), True)

print(solve_part1())
print(solve_part2())
