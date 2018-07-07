# visualisation of grid

#  0  1  2  3  4 (column numbers)
#  -  -  -  -  -
# 58 93 54  1 76 | row 0
# 83 70 54 36 43
# 54 89 87 17 67
# 74 25 77 74 27
# 45 70  1 57 81 | row 4

# generate grid, with each sub-list as column (hard-coded for now)
grid = [[58, 83, 54, 74, 45],
	[93, 70, 89, 25, 70],
	[54, 54, 87, 77,  1],
	[ 1, 36, 17, 74, 57],
	[76, 43, 67, 27, 81]]

# empty nested list, one for each starting cell
routes = [[] for i in range(0, len(grid))]


def cycleThrough(grid):
	# index for current row and column
	currentColumn = len(grid)-2
	# working array = last column (for the first cycle)
	workingArray = grid[len(grid)-1]
	# update workingArray each time a column is cycled through
	while currentColumn >= 0:
		workingArray = processColumn(grid, workingArray, currentColumn)
		currentColumn -= 1
	# add starting row index to each route
	for i, row in enumerate(routes):
		row.insert(0, i)

	return(workingArray)


def processColumn(grid, workingArray, currentColumn):
	rowIndex = 0
	# the real working array is only amended once a whole column has been cycled through
	workingArrayTemp = []
	# loops through penultimate column and estblishes a working array
	for rowValue in grid[currentColumn]:
		# RIGHT
		# adds up cell to right
		fastPath = (rowValue + workingArray[rowIndex])
		# adds row index for that cell to the route (to be changed if there is a faster cell above or below)
		routes[rowIndex].insert(0, rowIndex)
		# RIGHT AND BELOW
		# IF not at bottom row
		if rowIndex < len(grid) - 1:
			# IF this is a faster route...
			if fastPath > rowValue + workingArray[rowIndex+1]:
				# new lowest cost is product of current cell and previous lowest cost
				fastPath = rowValue + workingArray[rowIndex+1]
				# route for current row adopts route history of that cell, and adds the cell
				routes[rowIndex] = list(routes[rowIndex+1])
				routes[rowIndex].insert(0, rowIndex+1)
		# RIGHT AND ABOVE
		# IF not at top row
		if rowIndex > 0:
			#IF this is a faster route...
			if fastPath > rowValue + workingArray[rowIndex-1]:
				# new lowest cost is product of current cell and previous lowest cost
				fastPath = rowValue + workingArray[rowIndex-1]
				# route adopts history of cell
				routes[rowIndex] = list(routes[rowIndex-1])
				# changes first item, since the route for the previous row is one longer than the current one
				routes[rowIndex][0] =  rowIndex-1

		# adds lowest cost to temporary working array
		workingArrayTemp.append(fastPath)
		rowIndex += 1

	return(workingArrayTemp)

print("Lowest cost from each starting point")
print(cycleThrough(grid))
print("Fastest route from each starting point (by row index)")
print(routes)
