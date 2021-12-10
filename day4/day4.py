# part 1
def isWinner(board):
	# check rows
	for row in board:
		winner = True
		for i in range(1, len(row)):
			if row[i] != row[0]:
				winner = False
				break
		if winner:
			# print("found row winner: ", board)
			return True

	# check columns
	for c in range(0, len(board[0])):
		winner = True
		for r in range(1, len(board)):
			if board[r][c] != board[0][c]:
				winner = False
				break
		if winner:
			# print("found vertical winner: ", board)
			return True

	# check diagonals
	winner = True
	for i in range(1, len(board)):
		if board[i][i] != board[0][0]:
			winner = False
			break
	if winner:
		# print("found diag 1 winner: ", board)
		return True

	winner = True
	for i in range(1, len(board)):
		if board[i][len(board) - 1 - i] != board[0][len(board) - 1]:
			winner = False
			break
	if winner: 
		# print("found diag 2 winner: ", board)
		return True

	return False

def calculateScore(board):
	return 0

def printBoard(board):
	for row in board:
		print(row)

# unit test
test_horiz = [[1,2,3,4,5],[0,0,0,0,0],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
test_vert = [[1,2,3,0,5],[6,7,8,0,10],[11,12,13,0,15],[16,17,18,0,20],[21,22,23,0,25]]
test_diag1 = [[0,2,3,4,5],[6,0,8,9,10],[11,12,0,14,15],[16,17,18,0,20],[21,22,23,24,0]]
test_diag2 = [[1,2,3,4,0],[6,7,8,0,10],[11,12,0,14,15],[16,0,18,19,20],[0,22,23,24,25]]

# isWinner(test_horiz)
# isWinner(test_vert)
# isWinner(test_diag1)
# isWinner(test_diag2)

def getWinnerSum(board):
	res = 0
	for row in board:
		for item in row:
			if item != "x":
				res += int(item)
	return res

with open("input.txt") as f:
	lines = f.readlines()
	numbers = lines[0].split(",")
	boards = list(map(lambda x: x.strip().split("\n"), "".join(lines[1::]).split("\n\n")))
	for board in boards:
		for i, line in enumerate(board):
			line = line.strip().replace("  ", " ").split(" ")
			board[i] = line
	stop = False
	for number in numbers:
		if not stop:
			for board in boards:
				for row in board:
					if number in row:
						i = row.index(number)
						row[i] = "x"
						if isWinner(board):
							print("part 1: ", getWinnerSum(board) * int(number))
							stop = True
							break
		else:
			break


# part 2
with open("input.txt") as f:
	lines = f.readlines()
	numbers = lines[0].split(",")
	boards = list(map(lambda x: x.strip().split("\n"), "".join(lines[1::]).split("\n\n")))
	for board in boards:
		for i, line in enumerate(board):
			line = line.strip().replace("  ", " ").split(" ")
			board[i] = line
	boards_in_game = boards
	go = True
	for number in numbers:
		if go:
			new_boards = []
			for board in boards_in_game:
				still_in_game = True
				for row in board:
					if number in row:
						i = row.index(number)
						row[i] = "x"
						if isWinner(board):
							still_in_game = False
							if len(boards_in_game) == 1:
								print("part 2: ", getWinnerSum(board) * int(number))
								go = False
							break
				if still_in_game:
					new_boards.append(board)
			boards_in_game = new_boards	
