from itertools import islice
from collections import deque

def mix(a, b):
	return a ^ b

def prune(a):
	return a % 16777216

def evolve(a):
	b = prune(mix(a, a * 64))
	c = prune(mix(b // 32, b))
	return prune(mix(c, c * 2048))

def evolve_n(a, n):
	secrets = [a]
	for _ in range(n):
		a = evolve(a)
		secrets.append(a)
	return a, secrets

def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def main():
	with open("input", "r") as file:
		lines = file.readlines()
	total = 0
	buyers = []
	for line in lines:
		if len(line.strip()) == 0:
			continue
		num = int(line.strip())
		secret, history = evolve_n(num, 2000)
		total += secret
		buyers.append([h % 10 for h in history])
	# Part 1
	print(total)
    # Part 2

	all_buyers = []
	possible_changes = set()
	for history in buyers:
		this_buyer = {}
		diff = [history[i-1] - history[i]  for i in range(1, len(history))]
		for i, changes in enumerate(sliding_window(diff, 4)):
			if changes in this_buyer:
				continue
			this_buyer[changes] = history[i+4]
			possible_changes.add(changes)
		all_buyers.append(this_buyer)

	max_bananas = 0
	print(len(possible_changes))
	for sequence in possible_changes:
		bananas = 0
		for buyer in all_buyers:
			if sequence in buyer:
				bananas += buyer[sequence]
		max_bananas = max(max_bananas, bananas)

	print(max_bananas)


if __name__ == "__main__":
	main()