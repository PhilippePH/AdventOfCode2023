import sys
sys.path.insert(0, "/Users/philippe/Documents/code/AdventOfCode2023")
from readFile import readFile

def addToList(puzzleInput, i):
	specificList = []

	while i < len(puzzleInput) and len(puzzleInput[i]) > 0 and puzzleInput[i][0].isdigit():
		brokendownLine = puzzleInput[i].split()
		intValues = [int(x) for x in brokendownLine]
		specificList.append(intValues)
		i += 1

	return (i,	specificList)

def breakdownInput(puzzleInput):
	seeds = puzzleInput[0][7:].split()
	seeds = [int(x) for x in seeds]

	for i in range(1, len(puzzleInput), 1):
		if puzzleInput[i] == "seed-to-soil map:":
			i, seedToSoil = addToList(puzzleInput, i + 1)

		if puzzleInput[i] == "soil-to-fertilizer map:":
			i, soilToFertilizer =  addToList(puzzleInput, i + 1)

		if puzzleInput[i] == "fertilizer-to-water map:":
			i, fertilizerToWater= addToList(puzzleInput, i + 1)

		if puzzleInput[i] == "water-to-light map:":
			i, waterToLight = addToList(puzzleInput, i + 1)

		if puzzleInput[i] == "light-to-temperature map:":
			i, lightToTemperature = addToList(puzzleInput, i + 1)

		if puzzleInput[i] == "temperature-to-humidity map:":
			i, temperatureToHumidity = addToList(puzzleInput, i + 1)

		if puzzleInput[i] == "humidity-to-location map:":
			i, humidityToLocation = addToList(puzzleInput, i + 1)

	#print([seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation])
	return [seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]

def mapping(initialValue, transformationInformation):
	valueToReturn = initialValue #if this value isn't mapped to anything, it will be returned as-is

	# Go through each line of the transformatio
	for transformation in transformationInformation:
		# Check if initialValue falls within
		if initialValue >= transformation[1] and initialValue <= (transformation[1] + transformation[2]):
			# If so, return its offsetted value
			diff = initialValue - transformation[1]
			valueToReturn = transformation[0] + diff

			break # I am assuming that the ranges are mutually exclusive, and that a value will not be changed twice at the same mapping step

	return valueToReturn


def getAllSeeds(seeds):
	newSeeds = []

	i = 0

	while i < len(seeds):
		# range includes 0 which is fine cause we want to add the initial value
		# need to add a +1 cause last value is excluded
		for j in range(seeds[i+1] + 1):
			newSeeds.append(seeds[i] + j)
		i += 2

	return newSeeds

def solve(puzzleInput):
	locations = []

	listedInput = breakdownInput(puzzleInput)

	seeds = listedInput[0]

	# FOR PROBLEM TWO
	seeds = getAllSeeds(seeds)

	seedToSoil = listedInput[1]
	soilToFertilizer = listedInput[2]
	fertilizerToWater = listedInput[3]
	waterToLight = listedInput[4]
	lightToTemperature = listedInput[5]
	temperatureToHumidity = listedInput[6]
	humidityToLocation = listedInput[7]

	for seed in seeds:
		newSeed = mapping(seed, seedToSoil)
		newSeed = mapping(newSeed, soilToFertilizer)
		newSeed = mapping(newSeed, fertilizerToWater)
		newSeed = mapping(newSeed, waterToLight)
		newSeed = mapping(newSeed, lightToTemperature)
		newSeed = mapping(newSeed, temperatureToHumidity)
		location = mapping(newSeed, humidityToLocation)

		locations.append(location)

	return min(locations)

def main():
	testInput = readFile("test1.txt")
	testResult = solve(testInput)
	print(testResult)

	print("------\n")

	#testInput = readFile("test2.txt")
	#testResult = solveProblemTwo(testInput)
	#print(testResult)

	print("------\n")

	puzzleInput = readFile("input.txt")
	result = solve(puzzleInput)
	#result = solveProblemTwo(puzzleInput)
	print(result)

if __name__ == "__main__":
	main()
