import re

def get_unique_words_and_postions(aFile, file_mode):
    words = []
    f = open(aFile, file_mode)
    sentence = f.read()
    sentence = re.findall(r"[\w']+|[.,!?;()@\-\n]", sentence)
    for w in sentence:
        words.append(w)
    f.close()
    unique_words = []
    for w in words:
        if not w in unique_words:
            unique_words.append(w)
    unique_words_dict = {key: val+1 for val, key in enumerate(unique_words)}
    print(unique_words_dict)
    positions = []
    for w in sentence:
        positions.append(unique_words_dict[w])
    positions = [str(p) for p in positions]
    strpositions = '#'.join(positions)
    return (unique_words, strpositions)

def output_unique_words_and_positions(aFile, file_mode, unique_words, positions):
    of = open(aFile, file_mode)
    of.write("#".join(unique_words))
    of.write("$")
    of.write(positions)
    of.close()

#unique_words, positions = get_unique_words_and_postions("words.txt", "r")
#output_unique_words_and_positions("output.txt", "w", unique_words, positions)