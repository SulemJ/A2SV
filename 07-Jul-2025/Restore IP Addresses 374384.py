# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        if n < 4 or n > 12:
            return res
        
        def backtrack(start: int, parts: list[str]):
            if len(parts) == 4:
                if start == n:
                    res.append(".".join(parts))
                return

            for length in (1, 2, 3):
                if start + length > n:
                    break
                segm = s[start : start + length]
                
                if segm[0] == '0' and length > 1:
                    continue
                
                value = int(segm)
                if value > 255:
                    continue
                parts.append(segm)
                backtrack(start + length, parts)
                parts.pop()
        
        backtrack(0, [])
        return res