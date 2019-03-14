""""
https://www.coderbyte.com/editor/guest:Check%20Nums:Python

Challenge
Have the function CheckNums(num1,num2) take both parameters being passed and return the string true
if num2 is greater than num1, otherwise return the string false.
If the parameter values are equal to each other then return the string -1.

Sample Test Cases

Input:3 & num2 = 122

Output:"true"

Input:67 & num2 = 67

Output:"-1"

"""
def CheckNums(num1, num2):
    return '-1' if num2 == num1 else 'true' if num2 > num1 else 'false'
    # if num2 > num1:
    #     return 'true'
    # elif num2 == num1:
    #     return '-1'
    # else:
    #     return 'false'