""""
https://www.coderbyte.com/editor/guest:Letter%20Capitalize:Python

Challenge
Have the function LetterCapitalize(str) take the str parameter being passed and capitalize
the first letter of each word. Words will be separated by only one space.

Sample Test Cases
Input:"hello world"

Output:"Hello World"


Input:"i ran there"

Output:"I Ran There"
"""
def LetterCapitalize(str):
    wordsList = str.split()

    return " ".join([x.capitalize() for x in wordsList])