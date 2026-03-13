# list of common words (source: Collins Dictionary)
common_words = ("the", "of", "and", "a", "to", \
    "in", "is", "you", "that", "it", "he", \
    "was", "for", "on", "are", "as", "with", "his", \
        "they", "I", "at", "be", "this", "have", "from")

# print out this list
title = "The original words"
print(title)
print(common_words)


# how many are there?
title = "A - Number of words"
print(title)
print(len(common_words))



# show the first 5 words
title = "B - First 5 words"
print(title)
print(common_words[:5])



# the last 3 words
title = "C - Last 3 words"
print(title)
print(common_words[-3:])


# every fifth word
title = "D - Every 5th word"
print(title)
print(common_words[::5])




# iterate over words, listing out the ones with four letters
title = "E - Four-letter words"
print(title)
for word in common_words:
    if len(word) == 4:
        print(word)
    





title = "F - Words starting with W"
print(title)  # ← this is missing everywhere
for word in common_words:
    if word.startswith("w"):
        print(word)




# show the words in alphabetical order (need to convert to a list first)
title = "G - Words in order"
print(title)
print(sorted(common_words))

