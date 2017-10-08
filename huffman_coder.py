def huffmanText():
    inputType = raw_input("To encode a text file; type 0. To encode console input; type 1. ")

    if inputType == ("0"):
        inputLocation = raw_input("Please place the file you wish to encode in the huffman_coder directory. Please enter the name of the file.")
        inputLocation = "/home/martin/PycharmProjects/Huffman_Coder/" + inputLocation
        inputFile = open(inputLocation, "r")
        inputText = inputFile.read()

    if inputType == ("1"):
        inputText = raw_input("Please enter the string you wish to create a huffman coding tree for.")

    return inputText

characterList = []
characterCount = []
huffmanText = huffmanText()
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
print characterList
print characterCount

