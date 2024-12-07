from functools import cmp_to_key

lines = [line.strip() for line in open("data/day05.txt", "r")]
RULES_BEFORE = {}
RULES_AFTER = {}
PAGES = []

for line in lines:
	if line.find("|") != -1:
		rule = line.split('|')
		p0 = int(rule[0])
		p1 = int(rule[1])

		if p0 in RULES_BEFORE:
			RULES_BEFORE[p0].append(p1)
		else:
			RULES_BEFORE[p0] = [p1]

		if p1 in RULES_AFTER:
			RULES_AFTER[p1].append(p0)
		else:
			RULES_AFTER[p1] = [p0]
	elif len(line) > 0:
		PAGES.append([int(page) for page in line.split(",")])

def find_valid_invalid():
	valid = []
	invalid = []

	for pages in PAGES:
		valid_order = True

		for i in range(len(pages)):
			page = pages[i]

			if page in RULES_BEFORE:
				for n_i in range(i + 1, len(pages)):
					next_page = pages[n_i]
					if not next_page in RULES_BEFORE[page]:
						valid_order = False

			if page in RULES_AFTER:
				for p_i in range(i):
					prev_page = pages[p_i]
					if not prev_page in RULES_AFTER[page]:
						valid_order = False


		if valid_order:
			valid.append(pages)
		else:
			invalid.append(pages)
	
	return valid, invalid

def solve_part1():
	result = 0

	valid, _ = find_valid_invalid()

	for pages in valid:
		result += pages[int((len(pages) - 1) / 2)]

	return result

def solve_part2():
	result = 0

	def compare(a, b):
		if a in RULES_BEFORE and b in RULES_BEFORE[a]:
			return -1
		elif a in RULES_AFTER and b in RULES_AFTER[a]:
			return 1
		else:
			return 0

	_, invalid = find_valid_invalid()

	for pages in invalid:
		sorted_pages = sorted(pages, key=cmp_to_key(compare))
		result += sorted_pages[int((len(pages) - 1) / 2)]

	return result

print(solve_part1())
print(solve_part2())
