option = input("Input of sentence... Press M for manual input or F for file: ")
while option:
    if option.upper() == "M":
        sentence = input("Enter a sentence: ")
        break
    elif option.upper() == "F":
        f = open("sentencefile.txt", "r")
        sentence = f.read()
        f.close()
        break
    else:
        print("invalid input, try again")
        option = input("Input of sentence... Press M for manual input or F for file: ")

word = input("Enter a word: ").lower()
positions = []
sentence_list = sentence.lower().split()
i = 0
while i < len(sentence_list):
    if sentence_list[i] == word:
        positions.append(i+1)
    i += 1
if len(positions) == 0:
    print("The word", word, "is not found in the sentence")
elif len(positions) == 1:
    print("The word", word, "occurs in position", positions[0])
elif len(positions) == 2:
    print("The word", word, "occurs in positions", positions[0], "and", positions[1])
else:
    output = f"The word {word} occurs in positions: "
    for p in range(0, len(positions)-1):
        output = output + str(p) + ", "
    output = output[:-2]
    output += " and " + str(positions[-1])
    print(output)
