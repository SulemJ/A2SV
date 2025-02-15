# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        i = 1
        while i <= n:
            if i %3 == 0 and i %5 == 0:
                arr.append("FizzBuzz")
            elif i%3 == 0:
                arr.append("Fizz")
            elif i%5 == 0:
                arr.append("Buzz")
            else: 
                arr.append(str(i))
            i = i+1
        return arr