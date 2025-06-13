# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        pars = ""
        for i,v in enumerate(command):
            if v == "G":
                pars += "G"
            elif v == "(":
                if command[i+1] == ")":
                    pars += "o"
                else:
                    pars += "al"
        return pars