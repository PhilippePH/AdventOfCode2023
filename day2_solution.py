from readFile import readFile
import sys

COLOURS = ["red", "green", "blue"]
CUTOFFS = [12, 13, 14]

def reformatLine(line):
	# get gameId, which always starts at index 5
	gameId = str(line[5])
	i = 6
	while line[i].isdigit():
		gameId += str(line[i])
		i += 1
	gameId = int(gameId)
	newLine = []

	redValue = 0
	greenValue = 0
	blueValue = 0
	digitInTheMaking = "0"
	colorInTheMaking = ""

	line += ";"
	#print(line)

	while i < len(line):
	#	print(f"{colorInTheMaking=} {digitInTheMaking=} {greenValue=}")
		# found end of a draw
		if line[i] == ";":
			# commit the draw value
			#print("redvalue", redValue)
			newLine.append({COLOURS[0]:redValue, COLOURS[1]:greenValue, COLOURS[2]:blueValue})
	#		print(newLine)

			# reinitialise values
			redValue = 0
			greenValue = 0
			blueValue = 0
			digitInTheMaking = "0"
			colorInTheMaking = ""

		elif line[i].isdigit():
			digitInTheMaking += str(line[i])

		else:
			if line[i] != " " and line[i] != ":" and line[i] != ",":
				colorInTheMaking += line[i]

			if colorInTheMaking in COLOURS:
	#			print("!")
				if colorInTheMaking == COLOURS[0]:
					redValue = int(digitInTheMaking)
					#print(digitInTheMaking, redValue)
				elif colorInTheMaking == COLOURS[1]:
					greenValue = int(digitInTheMaking)
	#				print(greenValue)
				elif colorInTheMaking == COLOURS[2]:
					blueValue = int(digitInTheMaking)

				digitInTheMaking = "0"
				colorInTheMaking = ""

		i += 1

	return (newLine, gameId)

def solveProblemOne(input):
	# set the total
	result = 0

	# loop by line
	for line in input:
		# reformat line
		newLine, gameId = reformatLine(line)

		for draw in newLine:
			skip = False
			# check conditions
			if draw[COLOURS[0]] > CUTOFFS[0] or draw[COLOURS[1]] > CUTOFFS[1] or draw[COLOURS[2]] > CUTOFFS[2]:
				skip = True
				break

		if skip:
			continue

		#update the total if all draws make game possible
		result += gameId

	return result


def main():
	testInput = readFile("day2_test.txt")
	testResult = solveProblemOne(testInput)
	print(testResult)

	print("------\n")

	input = readFile("day2_input.txt");
	result = solveProblemOne(input)
	print(result)

if __name__ == "__main__":
	main()
