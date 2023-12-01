from readFile import readFile
import sys

"""
Problem 1 Initial idea:
Read file, save content in list, close file.
Initiate sum at zero.
	For each line, loop from the left until you find 1st digit.
	Then, loop from the right until you find 1st digit (which is the last one of the line).
Combine and add to the sum.
Return sum.

Problem 2 Edit:
Simply add a check after checking for a digit whether the x previous chars and the current one form a digit word.
"""

LETTER_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def findFirstDigit(line):
	for i in range(len(line)):
		# Check for number digit
		if line[i].isdigit():
			return line[i]

		for j in range(len(LETTER_DIGITS)):
			#print(line[i - (len(LETTER_DIGITS[j]) - 1) : i + 1])
			if line[max(0, i - (len(LETTER_DIGITS[j]) - 1) ) : i + 1] == LETTER_DIGITS[j] :
				return j + 1

	sys.exit('No first digit found')

def findSecondDigit(line):
	for i in range(len(line) - 1, -1, -1):
		if line[i].isdigit():
			return line[i]

		for j in range(len(LETTER_DIGITS)):
			#print(line[i : min(len(line), i + (len(LETTER_DIGITS[j]) - 1) + 1)])
			if line[i : min(len(line), i + (len(LETTER_DIGITS[j]) - 1) + 1)] == LETTER_DIGITS[j] :
				return j + 1

	sys.exit('No second digit found')

def solveProblemOne(input):
	result = 0

	for i in range(len(input)):
	#for i in range(1,2,1):
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
