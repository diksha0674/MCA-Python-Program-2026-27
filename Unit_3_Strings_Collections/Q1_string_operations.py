# Q1. String operations and methods

sentence = input("Enter a sentence: ")
print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Without leading/trailing spaces:", sentence.strip())

old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
print("After replacement:", sentence.replace(old_word, new_word))

character = input("Enter a character to count: ")
print("Occurrences:", sentence.count(character))

start_text = input("Enter text to check at the beginning: ")
end_text = input("Enter text to check at the end: ")
print("Starts with:", sentence.startswith(start_text))
print("Ends with:", sentence.endswith(end_text))

extra = input("Enter another string for concatenation: ")
print("Concatenation:", sentence + " " + extra)
print("Repetition (2 times):", sentence * 2)
word = input("Enter text to search: ")
print("Membership:", word in sentence)
