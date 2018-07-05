#  0  1  2  3  4 (column numbers)
#  -  -  -  -  -
# 58 93 54  1 76 | row 0
# 83 70 54 36 43
# 54 89 87 17 67
# 74 25 77 74 27
# 45 70  1 57 81 | row 4

# generate grid, with each sub-list as column (answer = 155)
grid = [[58, 83, 54, 74, 45],
	[93, 70, 89, 25, 70],
	[54, 54, 87, 77,  1],
	[ 1, 36, 17, 74, 57],
	[76, 43, 67, 27, 81]]



def cycleThrough(grid):
	# index for current row and column
	rowIndex = 0
	currentColumn = len(grid)-2
	# working array = last column (for the first cycle)
	workingArray = grid[len(grid)-1]
	# will replace workingArray each time a column is cycled through
	while currentColumn >= 0:
		workingArray = processColumn(grid, workingArray, currentColumn)
		currentColumn -= 1
	# prints shortest final route
	print(sorted(workingArray)[0])


def processColumn(grid, workingArray, currentColumn):
	rowIndex = 0
	workingArrayTemp = []

	# loops through penultimate column and estblishes a working array
	for rowValue in grid[currentColumn]:
		additions = []
		# adds up cell to right
		additions.append(rowValue + workingArray[rowIndex])
		# adds up cell right and below IF not at bottom
		if rowIndex < len(grid) - 1:
			additions.append(rowValue + workingArray[rowIndex+1])
		# adds up cell right and above IF not at top
		if rowIndex > 0:
			additions.append(rowValue + workingArray[rowIndex-1])
		# adds lowest total to WA and resets  additions
		workingArrayTemp.append(sorted(additions)[0])

		rowIndex += 1
	return(workingArrayTemp)

cycleThrough(grid)

