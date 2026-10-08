""""Find the Longest Word in a Sentence
Input: I love programming → Output: programming"""

sentence = ("I love programing " )

words = sentence.split()
longest = max(words , key= len)

print(longest)
