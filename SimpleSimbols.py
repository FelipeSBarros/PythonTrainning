""""
https://www.coderbyte.com/editor/guest:Simple%20Symbols:Python

Challenge
Have the function SimpleSymbols(str) take the str parameter being passed and determine
 if it is an acceptable sequence by either returning the string true or false.
 The str parameter will be composed of + and = symbols with several letters between
  them (ie. ++d+===+c++==a) and for the string
  to be true each letter must be surrounded by a + symbol.
   So the string to the left would be false.
   The string will not be empty and will have at least one letter.

Sample Test Cases
Input:"+d+=3=+s+"

Output:"true"


Input:"f++d+"

Output:"false"
"""
from string import ascii_letters as letters

def SimpleSimbols(str):
    str = "=" + str + "="
    for i in str:
        if i in letters:
            if not str[str.find(i) +1] == "+" or not str[str.find(i) - 1] == "+":
                return False
    return True