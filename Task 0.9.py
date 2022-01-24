def vowels(word):
    output = ""
    output_of_Length = 0
    for x in word:
        letter = x.lower()
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    
            if output.find(letter) == -1:
                output += letter + ", "
    output_of_length = len(output)
    print("Vowels: " + output[0:output_of_Length-2])
    
vowels("Umuzi")