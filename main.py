def translate(phrase):
    translation = ""
    for letter in phrase:                       #Loops helps to go throgh each letter of phrase
        if letter in "AEIOUaeiou":              # After the loop, it checks through if the letter in ""AEIOUaeiou""
            translation = translation + "g"     # If it is ,It takes each letter and check for the vowel ( Vowel detector). Then, replace with "g".
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
