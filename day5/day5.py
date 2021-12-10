from collections import defaultdict
import math

# part 1
with open("input.txt") as f:
	lines = f.readlines()
	lines = map(lambda x: x.strip().split(" -> "), lines)
	lines = map(lambda x: [x[0].split(","), x[1].split(",")], lines)
	pcoverage = defaultdict(int)
	for line in lines:
		a = list(map(lambda x: int(x), line[0]))
		b = list(map(lambda x: int(x), line[1]))
		if a[0] == b[0]:
			for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
				pcoverage[tuple([a[0], i])] = pcoverage[tuple([a[0], i])] + 1
		if a[1] == b[1]:
			for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
				pcoverage[tuple([i, a[1]])] = pcoverage[tuple([i, a[1]])] + 1
	s = len(list(filter(lambda x: x > 1, pcoverage.values())))
	print("part 1: ", s)

# part 2
with open("input.txt") as f:
	lines = f.readlines()
	lines = map(lambda x: x.strip().split(" -> "), lines)
	lines = map(lambda x: [x[0].split(","), x[1].split(",")], lines)
	pcoverage = defaultdict(int)
	for line in lines:
		a = list(map(lambda x: int(x), line[0]))
		b = list(map(lambda x: int(x), line[1]))
		if a[0] == b[0]:
			for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
				pcoverage[tuple([a[0], i])] = pcoverage[tuple([a[0], i])] + 1
		elif a[1] == b[1]:
			for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
				pcoverage[tuple([i, a[1]])] = pcoverage[tuple([i, a[1]])] + 1
		else:
			# print(a, b)
			hstep = 1 if a[0] < b[0] else -1
			vstep = 1 if a[1] < b[1] else -1
			# print(hstep, vstep)
			for i in range(0, abs(a[0] - b[0]) + 1):
				# print("point: ", tuple([a[0] + (i*hstep), a[1] + (i*vstep)]))
				pcoverage[tuple([a[0] + (i*hstep), a[1] + (i*vstep)])] = pcoverage[tuple([a[0] + (i*hstep), a[1] + (i*vstep)])] + 1
	s = len(list(filter(lambda x: x > 1, pcoverage.values())))
	# for key in pcoverage.keys():
	# 	print(key, pcoverage[key])
	# for i in range(0, 10):
	# 	for j in range(0, 10):
	# 		if pcoverage[tuple([j, i])] != 0:
	# 			print(pcoverage[tuple([j, i])], end=" ")
	# 		else:
	# 			print(".", end=" ")
	# 	print()
	print("part 2: ", s)

