import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile

""" Initial notes
Might be simpler to find symbols and then see if any numbers are adjacent, rather than find numbers and then determine if they are eligible?
A list of strings is going to be a good format for this as the indexing will be pretty easy

Steps:
	loop using indexes (so you can then search around)
	if you find a symbol, search around
		if you find a digit, construct the full number and make sure you add it to the sum
			just need to make sure youu consider all numbers around the symbol and construct the numbers well
"""

SYMBOLS = {"~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "\\", "|", "/", '"', "'", ":", ";", "<", ">", ",", "?" }

def createNumber(puzzleInput, lineNumber, columnNumber):
	#a number will be on the same line, but in different columns
	#numbers on the left must be pre-pended, and the right appended
	#we know the current coordinates is a digit

	number = str(puzzleInput[lineNumber][columnNumber])
	numberCoordinates = []

	# pre-pending
	leftwardCol = columnNumber - 1
	while leftwardCol >= 0 and puzzleInput[lineNumber][leftwardCol].isdigit():
		number = str(puzzleInput[lineNumber][leftwardCol]) + number
		numberCoordinates.append(str(lineNumber)+str(leftwardCol))
		leftwardCol -= 1

	# appending
	rightwardCol = columnNumber + 1
	while rightwardCol < len(puzzleInput[lineNumber]) and puzzleInput[lineNumber][rightwardCol].isdigit():
		number += str(puzzleInput[lineNumber][rightwardCol])
		numberCoordinates.append(str(lineNumber)+str(rightwardCol))
		rightwardCol += 1

	return (int(number), numberCoordinates)

def addNumbers(puzzleInput, lineNumber, columnNumber):
	visited = []
	total = 0

	for lineOffset in [-1, 0, 1]:
		for columnOffset in [-1, 0, 1]:
			x = lineNumber + lineOffset
			y = columnNumber + columnOffset
			coordinate = str(x)+str(y)

			if coordinate not in visited:
				if puzzleInput[x][y].isdigit():
					number, coordinates = createNumber(puzzleInput, x, y)
					total += number

					for coordinateSet in coordinates:
						visited.append(coordinateSet)

	return total


def addGearRatios(puzzleInput, lineNumber, columnNumber):
	number1 = 0
	number2 = 0
	visited = []

	for lineOffset in [-1, 0, 1]:
		for columnOffset in [-1, 0, 1]:
			x = lineNumber + lineOffset
			y = columnNumber + columnOffset
			coordinate = str(x)+str(y)

			if coordinate not in visited:
				if puzzleInput[x][y].isdigit():
					number, coordinates = createNumber(puzzleInput, x, y)
					if number1 == 0:
						number1 = number
					elif number2 == 0:
						number2 = number
					else :
						sys.exit("Hmmm I found to many numbers..")

					for coordinateSet in coordinates:
						visited.append(coordinateSet)


	return (number1 * number2)

def solveProblemOne(puzzleInput):
	total = 0

	for lineNumber in range(len(puzzleInput)):
		for columnNumber in range(len(puzzleInput[lineNumber])):
			if puzzleInput[lineNumber][columnNumber] in SYMBOLS:
				total += addNumbers(puzzleInput, lineNumber, columnNumber)
	return total

def solveProblemTwo(puzzleInput):
	gearRatio = 0

	for lineNumber in range(len(puzzleInput)):
		for columnNumber in range(len(puzzleInput[lineNumber])):
			if puzzleInput[lineNumber][columnNumber] == "*":
				gearRatio += addGearRatios(puzzleInput, lineNumber, columnNumber)

	return gearRatio

def main():
	#testInput = readFile("test1.txt")
	#testResult = solveProblemOne(testInput)
	#print(testResult)

	print("------\n")

	testInput = readFile("test1.txt")
	testResult = solveProblemTwo(testInput)
	print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	#result = solveProblemOne(puzzleInput)
	result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
