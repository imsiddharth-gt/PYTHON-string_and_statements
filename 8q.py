"""Check Whether Two Strings Are Anagrams
 Input: listen, silent → Output: Anagram"""

word1 = "listen"
word2 = "silent"

if sorted (word1)==sorted (word2)  :
    print("Anagram")
    
else :
    print(" not anagram")
