L = []

for line in open("data/day11.txt", "r"):
	L = list(map(int, line.strip().split()))

def get_num_buckets(buckets):
	result = 0
	
	for k in buckets.keys():
		result += buckets[k]

	return result

def solve(blinks):
	buckets = {}

	for val in L:
		buckets[val] = 1

	get_num_buckets(buckets)

	def add_to_bucket(buckets, dst, num):
		if dst not in buckets:
			buckets[dst] = 0

		buckets[dst] += num

	for _ in range(blinks):
		new_buckets = buckets.copy()

		for k in buckets.keys():
			if k == 0:
				add_to_bucket(new_buckets, 1, buckets[0])
				new_buckets[0] -= buckets[0]

			elif len(str(k)) % 2 == 0:
				str_k = str(k)
				half = int(len(str_k) / 2)
				l_k = str(k)[half:]
				r_k = str(k)[:half]
				
				add_to_bucket(new_buckets, int(l_k), buckets[k])
				add_to_bucket(new_buckets, int(r_k), buckets[k])
				new_buckets[k] -= buckets[k]
			else:
				add_to_bucket(new_buckets, k * 2024, buckets[k])
				new_buckets[k] -= buckets[k]

		buckets = new_buckets.copy()

	return get_num_buckets(buckets)

print(solve(25))
print(solve(75))
