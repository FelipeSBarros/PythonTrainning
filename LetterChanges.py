""""
https://www.coderbyte.com/editor/guest:Letter%20Changes:Python

Challenge
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm.
 Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
 Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

Sample Test Cases

Input:"hello*3"

Output:"Ifmmp*3"

Input:"fun times!"

Output:"gvO Ujnft!"
"""
from string import ascii_lowercase as letters
from string import whitespace, punctuation, digits
def LetterChanges(str):
    str = str.lower()
    Lstr = list(str)
    for i in range(len(Lstr)):
        if Lstr[i] == 'z':
            Lstr[i] = 'A'
        elif Lstr[i] in whitespace:
            pass
        elif Lstr[i] in punctuation:
            pass
        elif Lstr[i] in digits:
            pass
        else:
            l = letters[ letters.find(Lstr[i]) + 1]
            if l in ('a', 'e', 'i', 'o', 'u'):
                l = l.upper()
            Lstr[i] = l

        str = "".join(Lstr)

    return str
