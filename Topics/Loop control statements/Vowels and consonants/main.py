vowel = list("aeiou")
words = input()
for word in words:
    if not word.isalpha():
        break
    print("vowel" if word in vowel else "consonant")