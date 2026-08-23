sentence=input('enter a sentence: ')
vowel=0
for alphabet in sentence:
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        vowel+=1

print(vowel)
