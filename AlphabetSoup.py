""""
https://www.coderbyte.com/editor/guest:Alphabet%20Soup:Python
Challenge
Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
Sample Test Cases
Input:"coderbyte"

Output:"bcdeeorty"


Input:"hooplah"

Output:"ahhloop"
"""
def AlphabetSoup(str):
    strList = [x for x in str]
    strList.sort()
    return ''.join(strList)