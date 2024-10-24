def  remove_vowel (text):
    vowel ="aeiouAEIOU"
    return ''.join([char for char in text if char not in vowel])
text = input("evodiya enter the text:")
print ("text without  vowels:", remove_vowel(text))