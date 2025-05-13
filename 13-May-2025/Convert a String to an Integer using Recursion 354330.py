# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def strtoint(str, idx):
    if idx == len(str):
        return 0
    num=int(str[idx])

    return num * (10**(len(str)-idx-1)) + caller(str, idx+1)

def caller(str):
    return strtoint(str, 0)
