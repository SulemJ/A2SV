# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((cur_string, num))
                cur_string = ""
                num = 0
            elif char == "]":
                last_string, repeat_count = stack.pop()
                cur_string = last_string + cur_string * repeat_count
            else:
                cur_string += char

        return cur_string