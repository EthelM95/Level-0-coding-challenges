def vowels(word):
    output = ""
    outputLength = 0
    for x in word:
        letter = x.lower()
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    
            if output.find(letter) == -1:
                output += letter + ", "
    outputLength = len(output)
    print("Vowels: " + output[0:outputLength-2])
    
vowels("Umuzi")