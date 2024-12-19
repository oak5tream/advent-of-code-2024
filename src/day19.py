import functools

def parse_input():
	patterns = frozenset()
	designs = []

	for i, line in enumerate(open("data/day19.txt", "r")):
		if i == 0:
			patterns = frozenset(line.strip().split(", "))
		elif i > 1:
			designs.append(line.strip())

	return patterns, designs

@functools.lru_cache()
def possible_design(patterns, design):
	result = 0

	if design == "":
		return 1

	for pattern in patterns:
		if design.startswith(pattern):
			next_design = design[len(pattern):]
			result += possible_design(patterns, next_design)

	return result

def solve_part1():
	result = 0

	patterns, designs = parse_input()

	for design in designs:
		result += 1 if possible_design(patterns, design) else 0

	return result

def solve_part2():
	result = 0

	patterns, designs = parse_input()

	for design in designs:
		result += possible_design(patterns, design)

	return result

print(solve_part1())
print(solve_part2())
