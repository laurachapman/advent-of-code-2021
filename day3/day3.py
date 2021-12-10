with open("input.txt") as f:
	lines = f.readlines()
	l = len(lines[0]) - 1
	tracker = l*[0]
	for line in lines:
		for i in range(0, len(line.strip())):
			if line[i] == "1":
				tracker[i] += 1
			else:
				tracker[i] -= 1
	gamma = int("".join(list(map(lambda i: "1" if i > 0 else "0", tracker))), 2)
	epsilon = int("".join(list(map(lambda i: "0" if i > 0 else "1", tracker))), 2)
	ans = gamma * epsilon
	print("part 1: ", ans)


def findMaxBit(lines, i, takeMax=True):
	a = "1"
	b = "0"
	if not takeMax:
		a = "0"
		b = "1"
	m = 0
	for line in lines:
		if line[i] == "1":
			m += 1
		else:
			m -= 1
	return a if m >= 0 else b

def filterByBit(lines, bit, i):
	newlines = lines.copy()
	return list(filter(lambda x: x[i] == bit, newlines))

with open("input.txt") as f:
	l = list(map(lambda x: x.strip(), f.readlines()))
	lines = l.copy()
	i = 0
	while len(lines) > 1:
		bit = findMaxBit(lines, i)
		lines = filterByBit(lines, bit, i)
		i += 1
	oxygen = lines[0]
	lines = l.copy()
	i = 0
	while len(lines) > 1:
		bit = findMaxBit(lines, i, False)
		lines = filterByBit(lines, bit, i)
		i += 1
	co2 = lines[0]
	ans = int(oxygen, 2) * int(co2, 2)
	print("part 2:", ans)

