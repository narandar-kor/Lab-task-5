sentence = input("Enter a sentence : ")

N_character = len(sentence)
N_words = len(sentence.split())
N_vowel = 0
N_spaces = 0
N_digits = 0

for i in sentence:
    if i==" ":
        N_spaces += 1
    elif i in "aeiou":
        N_vowel += 1
    elif i.isdigit():
        N_digits += 1


print(f"Number of character's is : {N_character}")
print(f"Number of word's is : {N_words}")
print(f"Number of vowel is : {N_vowel}")
print(f"Number of spaces is : {N_spaces}")
print(f"Number of digits is : {N_digits}")