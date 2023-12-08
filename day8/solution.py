import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile
from collections import deque
def changeInput(puzzleInput):
	directions = deque(puzzleInput[0])
	elements = {}

	for i in range(2, len(puzzleInput), 1):
		elements[puzzleInput[i][0:3]] = [puzzleInput[i][7:10], puzzleInput[i][12:15]]
	#print(directions, elements)
	return (directions, elements)

def solveProblemOne(puzzleInput):
	directions, elements = changeInput(puzzleInput)

	currentElement = "AAA"
	counter = 1

	while True:
		direction = directions.popleft() # removes the value from the front and returns it
		directions.append(direction) # add it back to the back of the queue

		currentElement = elements[currentElement][(direction == "R")] # direction == "R" will be 1 if true (right) or 0 if false (left)
		if currentElement == "ZZZ":
			return counter
		counter += 1

		#print(counter, currentElement, directions)



def main():
	testInput = readFile("test1.txt")
	testResult = solveProblemOne(testInput)
	print(testResult)

	print("------\n")

	testInput = readFile("test2.txt")
	testResult = solveProblemOne(testInput)
	print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	result = solveProblemOne(puzzleInput)
	#result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
