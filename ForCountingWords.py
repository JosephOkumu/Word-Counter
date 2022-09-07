myString = 'There are seven words in this string.'
numSpaces = 0

for currentCharacter in myString:
    #checks if the character is a space.
    if currentCharacter == ' ':
        numSpaces += 1
print('There are', numSpaces +1, 'words in the string.')
