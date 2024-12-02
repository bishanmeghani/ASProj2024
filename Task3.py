from Task2 import *
import re

def compress(originalFile, newFile):
    unique_words, positions = get_unique_words_and_postions(originalFile, "r")
    print(unique_words)
    print(positions)
    output_unique_words_and_positions(newFile, "w", unique_words, positions)

def decompress(newFile, orignalFile):
    #open compressed file: newFile
    f = open(newFile, "r")
    #get uniqpositionue words
    out = f.read().split("$")
    f.close()

    #get positions
    positions = out[1].split("#")
    positions = [int(p) for p in positions]
    #put them in a dictionary where key is the position and value is the unique word
    unique_words = out[0].split('#')
    unique_words_dict = {key+1: val for key, val in enumerate(unique_words)}
    #for each position look up the value from the dictionary and create a new list, join list
    reconstructed = []
    for p in positions:
        reconstructed.append(unique_words_dict[p])
    reconstructed = ' '.join(reconstructed)
    reconstructed = re.sub(r'\s([?.,;:!"](?:\s|$))', r'\1', reconstructed)
    reconstructed = re.sub(r'\n +', r'\n', reconstructed)
    reconstructed = re.sub(r' +\n', '\n', reconstructed)
    reconstructed = reconstructed.strip()

    newOriginal = open(orignalFile, "w")
    newOriginal.write(reconstructed)
    newOriginal.close()

#compress("lorem.txt", "loremoutput.txt")
decompressed_text = decompress("loremoutput.txt", "decompressedLorem.txt")