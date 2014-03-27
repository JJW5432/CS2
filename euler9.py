from euler8 import product

input = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

def intlist(l):
	"""takes a list of strings and returns list with int() applied to each element
	Tests:
		>>> intlist(["1", "2", "3"])
		[1, 2, 3]

		>>> intlist(["1", ["2", "3", ["4"]]])
		[1, [2, 3, [4]]]
	"""
	output = []
	for x in l:
		if type(x) == list:
			output.append(intlist(x))
		else:
			output.append(int(x))
	return output

rows_unsplit = input.strip().split("\n")
rows = [x.split(' ') for x in rows_unsplit]
rows = intlist(rows)

def numAt(x,y):
	"""returns element in column x and row y with origin at top left
	Tests:
		>>> numAt(0,0)
		8

		>>> numAt(3, 0)
		97

		>>> numAt(0,3)
		52

		>>> numAt(3,3)
		23
	"""
	return rows[y][x]

def down(x, y, n):
	"""returns a list of n numbers going down, and starting at number (x,y)
	Tests:
		>>> down(0, 0, 1)
		[8]

		>>> down(0, 0, 4)
		[8, 49, 81, 52]

		>>> down(6, 4, 4)
		[63, 45, 67, 12]

		>>> down(4, 6, 4)
		[64, 2, 66, 75]

		>>> down(4, 18, 4)
		[0]
	"""
	if y + n > len(rows):
		return [0]
	output = [numAt(x,y)]
	if n > 1:
		output+=down(x, y+1, n-1) 
	return output

def right(x, y, n):
	"""returns a list of n numbers going right, and starting at number (x,y)
	Tests:
		>>> right(0, 0, 1)
		[8]

		>>> right(0, 0, 4)
		[8, 2, 22, 97]

		>>> right(6, 4, 4)
		[63, 89, 41, 92]

		>>> right(4, 6, 4)
		[64, 23, 67, 10]

		>>> right(18, 4, 4)
		[0]
	"""
	if x + n > len(rows[0]):
		return [0]
	output = [numAt(x,y)]
	if n > 1:
		output+=right(x+1, y, n-1) 
	return output

def diag_right(x, y, n):
	"""returns a list of n numbers going down-right diagonal, and starting at number (x,y)
	Tests:
		>>> diag_right(0, 0, 1)
		[8]

		>>> diag_right(0, 0, 4)
		[8, 49, 31, 23]

		>>> diag_right(6, 4, 4)
		[63, 2, 26, 63]

		>>> diag_right(4, 6, 4)
		[64, 62, 99, 44]

		>>> diag_right(18, 4, 4)
		[0]
	"""
	if x + n > len(rows[0]) or y + n > len(rows):
		return [0]
	output = [numAt(x,y)]
	if n > 1:
		output+=diag_right(x+1, y+1, n-1) 
	return output


def diag_left(x, y, n):
	"""returns a list of n numbers going down-left diagonal, and starting at number (x,y)
	Tests:
		>>> diag_left(0, 0, 1)
		[8]

		>>> diag_left(0, 0, 4)
		[0]

		>>> diag_left(6, 4, 4)
		[63, 3, 64, 68]

		>>> diag_left(4, 6, 4)
		[64, 68, 58, 36]

		>>> diag_left(18, 18, 4)
		[0]
	"""
	if x - n + 1 < 0 or y + n > len(rows):
		return [0]
	output = [numAt(x,y)]
	if n > 1:
		output+=diag_left(x-1, y+1, n-1) 
	return output

highest = 0
for x in range(16):
	for y in range(16):
		guess =  max([product(z) for z in [down(x, y, 4), right(x, y, 4), diag_right(x,y,4), diag_left(x,y,4)]])
		if guess > highest:
			highest = guess


if __name__ == "__main__": #runs tests in correct context
	import doctest
	doctest.testmod()