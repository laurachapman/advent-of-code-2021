from collections import defaultdict

# part 1
with open("input.txt") as f:
	lines = f.readlines()
	fish = list(map(lambda x: int(x), lines[0].split(",")))
	for i in range(0, 80):
		newfish = []
		for f in fish:
			if f == 0:
				newfish.append(6)
				newfish.append(8)
			else:
				newfish.append(f-1)
		fish = newfish
	print("part 1: ", len(newfish))

# part 2
def emptyFishDict():
	fishCount = dict()
	for i in range(0, 9):
		fishCount[i] = 0
	return fishCount

with open("input.txt") as f:
	lines = f.readlines()
	fish = list(map(lambda x: int(x), lines[0].split(",")))
	fishCount = emptyFishDict()
	for f in fish:
		fishCount[f] += 1
	for i in range(0, 256):
		d = emptyFishDict()
		for fishy in fishCount.keys():
			if fishy == 0:
				d[6] += fishCount[0]
				d[8] += fishCount[0]
			else:
				d[fishy - 1] += fishCount[fishy]
		fishCount = d
	res = sum(fishCount.values())
	print("part 2: ", res)

