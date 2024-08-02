# Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

def check_vowel_or_consonant(char):
    vowels ="AEIOUaieou"
    if char.isalpha() and len(char) ==1:
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Invalid input"  
input_Char =input("Enter a Single Character :")
result = check_vowel_or_consonant(input_Char)
print(f"The Character '{input_Char}' is a {result}. ")      