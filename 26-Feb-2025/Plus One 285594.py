# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i= int("".join(map(str, digits)))
        # i= i)
        i+=1
        # print(digits)
        return [int(digit) for digit in str(i)]