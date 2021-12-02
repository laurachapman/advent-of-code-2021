# part 1 attempt 1
# doesn't work because filter modifies in place
with open("input.txt") as f:
	lines = map(lambda x: x.split(), f.readlines())
	forward = sum(map(lambda x: int(x[1]), filter(lambda x: x[0] == "forward", lines)))
	down = sum(map(lambda x: int(x[1]), filter(lambda x: x[0] == "down", lines)))
	up = sum(map(lambda x: int(x[1]), filter(lambda x: x[0] == "up", lines)))
	ans = (down - up) * forward

# part 1 attempt 2
with open("input.txt") as f:
	lines = map(lambda x: x.split(), f.readlines())
	forward = 0
	down = 0
	up = 0
	for line in lines:
		d = line[0]
		i = int(line[1])
		if d == "forward":
			forward += i
		if d == "down":
			down += i
		if d == "up":
			up += i
	ans = (down - up) * forward
	print("part 1: ", ans)

# part 2
with open("input.txt") as f:
	lines = map(lambda x: x.split(), f.readlines())
	horizontal = 0
	depth = 0
	aim = 0
	for line in lines:
		d = line[0]
		i = int(line[1])
		if d == "forward":
			horizontal += i
			depth += aim * i
		if d == "down":
			aim += i
		if d == "up":
			aim -= i
	ans = depth * horizontal
	print("part 2: ", ans)