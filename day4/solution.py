import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile

def splitLine(line):
	winningNumbers = set()
	ownNumbers = set()

	index = 6 # the ":" will never be before that index valuue

	# find the ":"
	while line[index] != ":":
		index += 1

	index += 2 # skip the space and go to first number index

	# add the winning numbers until you encounter |
	while line[index] != "|":
		winningNumbers.add(int(line[index : index + 2]))
		index += 3

	index += 2  # skip the | and go to the next number

	# add the ownNumbers
	while index < len(line):
		ownNumbers.add(int(line[index : index + 2]))
		index += 3

	return (winningNumbers, ownNumbers)

def solveProblemOne(puzzleInput):
	total = 0

	for line in puzzleInput:
		winningNumbers, ownNumbers = splitLine(line)

		cardValue = 0

		for number in ownNumbers:
			if number in winningNumbers:
				if cardValue == 0:
					cardValue = 1
				else:
					cardValue *= 2

		total += cardValue

	return total

def solveProblemTwo(puzzleInput):
	total = 0
	numberOfCards 
	for i in range(len(puzzleInput)):
		winningNumbers, ownNumbers = splitLine(line)

		cardValue = 0

		for number in ownNumbers:
			if number in winningNumbers:
				if cardValue == 0:
					cardValue = 1
				else:
					cardValue *= 2

		total += cardValue

	return total


def main():
	#testInput = readFile("test1.txt")
	#testResult = solveProblemOne(testInput)
	#print(testResult)

	print("------\n")

	testInput = readFile("test2.txt")
	testResult = solveProblemTwo(testInput)
	print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	result = solveProblemOne(puzzleInput)
	#result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
