text = input("Enter a sentence: ")
words = text.split()
word_count = {word: words.count(word) for word in set(words)}
print("Word Occurrences:", word_count)
