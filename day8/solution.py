import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile
from collections import deque

def changeInput(puzzleInput):
	directions = deque(puzzleInput[0])
	elements = {}
	startingElements = []

	for i in range(2, len(puzzleInput), 1):
		elements[puzzleInput[i][0:3]] = [puzzleInput[i][7:10], puzzleInput[i][12:15]]

		if puzzleInput[i][2] == "A":
			startingElements.append(puzzleInput[i][0:3])

	#print(directions, elements, startingElements)
	return (directions, elements, startingElements)


def solveProblemOne(puzzleInput):
	directions, elements, currentElements = changeInput(puzzleInput)

	foundEnd = [0] * len(currentElements)
	counter = 0

	while True:
		direction = directions.popleft() # removes the value from the front and returns it
		directions.append(direction) # add it back to the back of the queue

		for i in range(len(currentElements)):
			currentElement = currentElements[i]
			#print(currentElement)

			currentElement = elements[currentElement][(direction == "R")] # direction == "R" will be 1 if true (right) or 0 if false (left)
			currentElements[i] = currentElement #updating the list

			if currentElement[2] == "Z": # seeing if this one has found the end
				foundEnd[i] = 1
			else:
				foundEnd[i] = 0
			if sum(foundEnd) == len(currentElements):
				return counter
			counter += 1

		#print(counter, currentElement, directions)



def main():
	#testInput = readFile("test1.txt")
	#testResult = solveProblemOne(testInput)
	#print(testResult)

	print("------\n")

	testInput = readFile("test3.txt")
	testResult = solveProblemOne(testInput)
	print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	result = solveProblemOne(puzzleInput)
	#result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
