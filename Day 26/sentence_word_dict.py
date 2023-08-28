sentence = "What is the velocity of an Unladen Swallow?"
sentence_list = sentence.split(" ")
words_len = {word: len(word) for word in sentence_list}
print(words_len)
