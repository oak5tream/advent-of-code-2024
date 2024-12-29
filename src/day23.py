from heapq import heappop, heappush
import re

L = set(tuple(sorted(x)) for x in re.findall(r"(..)\-(..)", open("data/day23.txt").read()))

def solve_part1():
	cpus = {cpu for connection in L for cpu in connection}
	connections = {}

	for cpu in cpus:
		if not cpu in connections:
			connections[cpu] = []

		for (a, b) in L:
			if a == cpu:
				connections[cpu].append(b)
			elif b == cpu:
				connections[cpu].append(a)

	lan = {}

	for k, v in connections.items():
		for c0 in v:
			for c1 in connections[c0]:
				if c1 in connections[k]:
					if k.startswith("t") or c0.startswith("t") or c1.startswith("t"):
						cons = [k, c0, c1]
						lan[''.join(sorted(cons))] = True

	return len(lan.keys())

def solve_part2():
	cpus = {cpu for connection in L for cpu in connection}
	connections = []
	
	for cpu in cpus:
		con = set()
		con.add(cpu)

		for (a, b) in L:
			if a == cpu:
				con.add(b)
			elif b == cpu:
				con.add(a)

		connections.append(con)

	heap_id = 0
	queue = [(heap_id, connection) for connection in connections]

	while queue:
		_, connection = heappop(queue)

		if all((a, b) in L for a in connection for b in connection if a < b):
			return ','.join(sorted(connection))
    
		for c in connection:
			heap_id += 1
			heappush(queue, (heap_id, connection - {c}))

	return 0

print(solve_part1())
print(solve_part2())
