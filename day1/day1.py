# part 1
with open("input.txt") as f:
	lines = f.readlines()
	cur = None
	acc = 0
	for line in lines:
		if cur:
			if int(line) > cur:
				acc += 1
		cur = int(line)
	print("part 1: ", acc)

# part 2
with open("input.txt") as f:
	lines = list(map(lambda x: int(x), f.readlines()))
	threesum = lines[0] + lines[1] + lines[2]
	acc = 0
	for i in range(0, len(lines)-3):
		newsum = threesum - lines[i] + lines[i+3]
		if newsum > threesum:
			acc += 1
		threesum = newsum
	print("part 2: ", acc)

