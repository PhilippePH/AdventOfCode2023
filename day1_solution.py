from readFile import readFile
import sys

"""
Initial idea:
Read file, save content in list, close file.
Initiate sum at zero.
	For each line, loop from the left until you find 1st digit.
	Then, loop from the right until you find 1st digit (which is the last one of the line).
Combine and add to the sum.
Return sum.
"""

def findFirstDigit(line):
	for i in range(len(line)):
		if line[i].isdigit():
			return line[i]
	sys.exit('No first digit found')

def findSecondDigit(line):
	for i in range(len(line) - 1, -1, -1):
		if line[i].isdigit():
			return line[i]
	sys.exit('No second digit found')

def solveProblemOne(input):
	result = 0

	for i in range(len(input)):
		firstDigit = findFirstDigit(input[i])
		secondDigit = findSecondDigit(input[i])

		# concatenate the digitS
		value = int(str(firstDigit) + str(secondDigit))

		result += value

	return result

def main():
	input = readFile("day1_input.txt");
	result = solveProblemOne(input)
	print(result)

if __name__ == "__main__":
	main()
