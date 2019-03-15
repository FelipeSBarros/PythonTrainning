"""""
https://www.coderbyte.com/editor/guest:Time%20Convert:Python

Challenge
Have the function TimeConvert(num) take the num parameter being passed and
 return the number of hours and minutes the parameter converts to
 (ie. if num = 63 then the output should be 1:3).
 Separate the number of hours and minutes with a colon.

Sample Test Cases

Input:126

Output:"2:6"

Input:45

Output:"0:45"

"""

def TimeConvert(num):
        int_ = num // 60
        frac = num % 60
        return ":".join([str(int_), str(frac)])