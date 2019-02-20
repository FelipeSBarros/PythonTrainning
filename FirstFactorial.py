""""
https://www.coderbyte.com/editor/guest:First%20Factorial:Python

Challenge
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Sample Test Cases

Input:4

Output:24

Input:8

Output:40320

"""
def FirstFactorial(num):
    if num == 1:
        return num
    else:
        l = list(range(1, num + 1))[::-1]
        i = 0
        while i <= len(l)-1:
            if i == 0:
                fac = l[i] * l[i + 1]
            elif i == len(l) - 1:
                fac = fac * l[i]
            else:
                fac = fac * l[i + 1]
            i += 1
        return fac