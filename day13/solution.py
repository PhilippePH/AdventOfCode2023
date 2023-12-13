import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile

"""I assume we can do the search on the 2 or 3 rows/columns in the middle only? (3 if odd number and we need to ignore either first or last column)"""

def checkColRowByRow(pattern, left, right):
	for i in range(len(pattern)):
		if pattern[i][left] != pattern[i][right]:
			return True ## this is a cofnusing return value though
	return False

def checkColMirror(left, right, pattern):
	initialLeft = left
	while left >= 0 and right < len(pattern[0]):
		if checkColRowByRow(pattern, left, right):
			return 0
		else:
			left -= 1
			right += 1

	return initialLeft + 1


def checkRowMirror(left, right, pattern):
	initialLeft = left
	while left >= 0 and right < len(pattern):
		if pattern[left] != pattern[right]:
			return 0
		else:
			left -= 1
			right += 1
	return 100 * (initialLeft + 1)

def findReflection(pattern, checkingRows):
	num = len(pattern)

	if num % 2 == 0:
		left = len(pattern) / 2 - 1
		right = len(pattern) / 2

		if checkingRows:
			return checkRowMirror(left, right, pattern)
		return checkColMirror(left, right, pattern)

	else:
		middle = len(pattern) // 2 + 1
		pairs = [[middle - 1, middle], [middle, middle+1]]

		for pair in pairs:
			left = pair[0]
			right = pair[1]


			if checkingRows:
				value = checkRowMirror(left, right, pattern)
			else:
				value = checkColMirror(left, right, pattern)

			if value > 0:
				return value
	return 0


def findReflectionMain(pattern): # bad name
	value = findReflection(pattern, True)

	if value == 0:
		return findReflection(pattern, False)

	return value

def getPatterns(puzzleInput):
	patterns = []
	pattern = []
	for line in puzzleInput:
		if len(line) == 0:
			patterns.append(pattern)
			pattern = []
		else:
			pattern.append(line)
	if len(pattern) > 0:
		patterns.append(pattern)
	return patterns

def solveProblemOne(puzzleInput):
	total = 0

	patterns = getPatterns(puzzleInput)

	for pattern in patterns:
		total += findReflectionMain(pattern)

	return total

def main():
	testInput = readFile("test1.txt")
	testResult = solveProblemOne(testInput)
	print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	result = solveProblemOne(puzzleInput)
	##result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
