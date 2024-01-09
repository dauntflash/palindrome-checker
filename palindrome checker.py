word = input("Enter the word you want to check: ")

while True:
    if word.isalpha():
        break
    else:
        word = input("Invalid input, please enter a word you want to check: ")

lower_word=word.lower()
length = len(word)

lowerReversed_word=""
Reversed_word=""
i = length - 1
while i >= 0:
    lowerReversed_word+=lower_word[i]
    Reversed_word+=word[i]
    i -= 1

print("Original word was",word,"and the reversed form of the word is",Reversed_word +". " )
if lowerReversed_word != lower_word:
    print("The word is not a palindrome.")
else:
    print("The word is a palindrome")


#ALTERNATIVE CODE TO GET THE SAME OUTPUT
'''

word = input("Enter the word you want to check: ")
while True:
    if word.isalpha():
        break
    else:
        word = input("Invalid input, please enter a word you want to check: ")

lower_word=word.lower()
Reversed_word = word[::-1]
lowerReversed_word = Reversed_word.lower()

print("Original word was",word,"and the reversed form of the word is",Reversed_word +". " )
if lowerReversed_word != lower_word:
    print("The word is not a palindrome.")
else:
    print("The word is a palindrome")

b                            

'''