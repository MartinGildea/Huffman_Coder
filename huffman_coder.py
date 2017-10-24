######################################################################
# INPUT:  A string from a text file designated by the user, or a string inputted into the console by the user.
# OUTPUT: Scrapes the seleceted text file if neccessary, and assigns the string to a variable.
######################################################################
def inputter():
    inputType = raw_input("To encode a text file; type 0. To encode console input; type 1. ")

    if inputType == "0":
        inputLocation = raw_input("Please place the file you wish to encode in the huffman_coder directory. Please enter the name of the file.")
        inputLocation = "/home/martin/PycharmProjects/Huffman_Coder/" + inputLocation
        inputFile = open(inputLocation, "r")
        inputText = inputFile.read()

    if inputType == "1":
        inputText = raw_input("Please enter the string you wish to create a huffman coding tree for.")

    return inputText

######################################################################
# INPUT:  A string of variable length. Eg/ AaaaaBBBbbbb
# OUTPUT: A frequency count of all the characters in that string (Case sensitive), splint into two arrays. Eg/ [1, 4, 3, 4] [A, a, B, b]
######################################################################
def characterScraper(huffmanText):
    huffmanLength = len(huffmanText)
    for looper in range(0, huffmanLength):
        character = huffmanText[looper]
        duplicateCheck = len(characterList)
        duplicateYes = 0
        for counter in range(0, duplicateCheck):
            if character == characterList[counter]:
                characterCount[counter] = characterCount[counter] + 1
                duplicateYes = 1
        if duplicateYes == 0:
            characterList.append(character)
            characterCount.append(1)

######################################################################
# INPUT:  The arrays; characterCount and characterList. Eg/ [T, E, S] [2, 1, 1]
# OUTPUT: A unique binary code for each entry in the lists in decending order of length. Eg/ [10, 11, 0]
######################################################################
def binaryMaker():
    currentLength = len(characterCount)
    while currentLength != 1:

        # Find the most regularly occuring string and remove it from characterList
        # Remove the equivalent frequency count from characterCount
        currentLength = len(characterCount)
        smallestValue = characterCount[0]
        smallestEntry = 0
        smallestString = characterList[0]
        for looper in range(0, currentLength):
            if characterCount[looper] < smallestValue:
                smallestEntry = looper
                smallestValue = characterCount[looper]
                smallestString = characterList[looper]
        del characterCount[smallestEntry]
        del characterList[smallestEntry]

        # Find the second most regularly occuring string and remove it from characterList
        # Remove the equivalent frequency count from characterCount
        currentLength = len(characterCount)
        if currentLength != 1:
            if smallestEntry == 0:
                secondSmallestValue = characterCount[1]
                secondSmallestEntry = 1
                secondSmallestString = characterList[1]
            else:
                secondSmallestValue = characterCount[0]
                secondSmallestEntry = 0
                secondSmallestString = characterList[0]
            for counter in range(0, currentLength):
                if (characterCount[counter] < secondSmallestValue):
                    secondSmallestEntry = counter
                    secondSmallestValue = characterCount[counter]
                    secondSmallestString = characterList[counter]
            del characterCount[secondSmallestEntry]
            del characterList[secondSmallestEntry]
        else:
            secondSmallestEntry = 0
            secondSmallestValue = characterCount[0]
            secondSmallestString = characterList[0]
            del characterCount[secondSmallestEntry]
            del characterList[secondSmallestEntry]

        # Combine the least regularly occuring string and the second least regularly occuring string into an array and add to characterList
        # Add the occurance count of the least regularly occuring string and the second least regularly occuring and add to characterCount
        combinedValue = smallestValue + secondSmallestValue
        combinedString = smallestString + secondSmallestString
        characterList.append(combinedString)
        characterCount.append(combinedValue)

        # SPLIT SMALLEST STRING INTO A LIST AND ADD 0 TO ALL IN STRING
        length = len(smallestString)
        for outerLoop in range(0, length):
            character = smallestString[outerLoop]
            duplicateYes = 0
            duplicateCheck = len(binaryRecordString)
            for counter in range(0, duplicateCheck):
                if character == binaryRecordString[counter]:
                    duplicateYes = 1
                    entry = counter
            if duplicateYes == 0:
                binaryRecordString.append(smallestString)
                binaryRecord.append("0")
            else:
                binaryRecord[entry] = binaryRecord[entry] + "0"

        # SPLIT SECOND SMALLEST STRING INTO A LIST AND ADD 1 TO ALL IN STRING.
        length = len(secondSmallestString)
        for outerLoop in range(0, length):
            character = secondSmallestString[outerLoop]
            duplicateYes = 0
            duplicateCheck = len(binaryRecordString)
            for counter in range(0, duplicateCheck):
                if character == binaryRecordString[counter]:
                    duplicateYes = 1
                    entry = counter
            if duplicateYes == 0:
                binaryRecordString.append(secondSmallestString)
                binaryRecord.append("1")
            else:
                binaryRecord[entry] = binaryRecord[entry] + "1"
        currentLength = len(characterCount)

    # Reverse each binary code in the array binaryRecord. Eg/ 10 --> 01
    for counter2 in range(0, len(binaryRecord)):
        flip = binaryRecord[counter2]
        flipped = str()
        for counter3 in range(0, len(flip)):
            flipped = (flipped + (flip[-(counter3 + 1)]))
        binaryRecord[counter2] = flipped

######################################################################
# INPUT:  The array characterCount.
# OUTPUT: A copy of the array in ascending numerical order.
######################################################################
def listCopy():
    for counter in range(0, len(characterCount)):
        savedCharacterCount.append(characterCount[counter])
    while (len(savedCharacterCount) != 1):
        smallest = savedCharacterCount[0]
        smallestCount = 0
        for looper in range (0, len(savedCharacterCount)):
            if savedCharacterCount[looper] < smallest:
                smallest = savedCharacterCount[looper]
                smallestCount = looper
        del savedCharacterCount[smallestCount]
        finalCount.append(smallest)
    finalCount.append(savedCharacterCount[0])

######################################################################
# INPUT:  The orignal string(huffmanText), binary record, and binary record string. Eg/ (TEST) ['10', '11', '0'], ['E', 'S', 'T']
# OUTPUT: The string in binary. Eg/ Test ---> (010110)
######################################################################
def finalBinary (text):
    binaryOutput = str()
    for looper in range (0, (len(text))):
        character = text[looper]
        for counter in range(0, len(binaryRecord)):
            if character == binaryRecordString[counter]:
                addition = binaryRecord[counter]
        binaryOutput = binaryOutput + addition
    return binaryOutput

############ Initialising Arrays ############
characterList = []        # A list of all individiual characters in the string inputted by the user.
characterCount = []       # A list of the number of times a character occurs in the corresponding position in characterList. Eg/ characterCount[0] is a frequency count of chracterList[0]
savedCharacterCount = []  # A copy of characterCount
binaryRecord = []         # The unique binary code generated for each character, ordered from longest code to shortest.
binaryRecordString = []   # The letter corresponding to the binary code in the same position of binaryRecord. Eg/ binaryRecord[0] is the binary code of the character in binaryRecordString[0]
finalCount = []           # A copy of characterCount sorted into the order that corresponds to binaryRecordString.

############ PROGRAM ############
huffmanText = inputter()
characterScraper(huffmanText)
listCopy()
binaryMaker()
binaryOutput = finalBinary(huffmanText)
print finalCount
print binaryRecordString
print binaryRecord
print binaryOutput
print "Binary code is " + str(len(binaryOutput)) + " bits long."
