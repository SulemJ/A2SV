# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(n):
            if n <2:
                return False
            if n%2==0:
                return n==2
            for i in range(3, int(sqrt(n))+1, 2):
                if n%i==0:
                    return False
            return True
        if n<=2:
            return 2
        if n<=3:
            return 3
        if n<=5:
            return 5 
        if n<=7:
            return 7
        if n<=11:
            return 11
        length=1
        while True:
            for i in range(10**(length-1), 10**length):
                s= str(i)
                palind = int(s+ s[-2::-1])
                if palind>=n and  isPrime(palind):
                    return palind
            length+=1