def commom_characters(word1, word2):
    output = ""
    for i in (word1):
        for j in word2:
            if i == j:
                output += i + ", " 
    length_of_output = len(output)
    print("Common letters: " + output[0:y-2])


commom_characters("house", "computers")