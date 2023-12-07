import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile


""" Initial notes
The total distance = multiplication of the time you pushed on the button times the remaining time
so for a 5 sec race, the options aree
	0 x 5, 1 x 4, 2 x 3, 3 x 2, ...
	Meaning the ttotal distance is pyramidal (symmetric over the center) --> meaning you only need to calculate half and "double" or "-1 and then double"
"""

def treatInput(puzzleInput):
	time = puzzleInput[0][5:].split()
	distance = puzzleInput[1][9:].split()

	time = [int(x) for x in time]
	distance = [int(x) for x in distance]

	return (time, distance)

def waysToWin(time, distance):
	counter = 0

	for i in range(0, time // 2 + 1, 1):
		if i * (time - i) > distance:
			if i == (time)/ 2:
				counter += 1 # 1 because top of pyramid 
			else:
				counter += 2 # two since it is symmetrical
	return counter

def solveProblemOne(puzzleInput):
	total = 1

	time, distance  = treatInput(puzzleInput)

	for i in range(len(time)):
		total *= waysToWin(time[i], distance[i])

	return total


def main():
	testInput = readFile("test1.txt")
	testResult = solveProblemOne(testInput)
	print(testResult)

	print("------\n")

	#testInput = readFile("test2.txt")
	#testResult = solveProblemTwo(testInput)
	#print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	result = solveProblemOne(puzzleInput)
	#result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
