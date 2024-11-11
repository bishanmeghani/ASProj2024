f = open("words.txt", "r")
words = []
sentence = f.readline()
sentence = sentence.split()
for w in sentence:
    words.append(w)
f.close()

unique_words = []
for w in words:
    if not w in unique_words:
        unique_words.append(w)

unique_words_dict = {key: val+1 for val, key in enumerate(unique_words)}

positions = ""
for w in sentence:
    positions += str(unique_words_dict[w])

positions = ','.join(positions)

of = open("output.txt", "w")
of.write(",".join(unique_words))
of.write("\n")
of.write(positions)
of.close()