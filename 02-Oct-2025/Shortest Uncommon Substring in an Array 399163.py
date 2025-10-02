# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        res= []
        for i in range(n):
            s=arr[i]
            m= len(arr[i])
            substrings=set()
            for j in range(1,m+1):
                for k in range(m-j+1):
                    substrings.add(s[k:k+1])
            ans=None
            for sub in sorted(substrings, key=lambda x:(len(x), x)):
                found=False
                for l in range(n):
                    if l==i:
                        continue
                    if sub in arr[l]:
                        found =True
                        break
                if not found:
                    ans = sub
                    break
                
            res.append(ans if ans else "")
        return res                    
                    

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        result = []

        for i in range(n):
            substrings = set()
            s = arr[i]
            m = len(s)

            # generate all substrings of s
            for l in range(1, m+1):  # length of substring
                for start in range(m - l + 1):
                    substrings.add(s[start:start+l])

            candidate = None

            # check uniqueness
            for sub in sorted(substrings, key=lambda x: (len(x), x)):
                found = False
                for j in range(n):
                    if i == j:
                        continue
                    if sub in arr[j]:
                        found = True
                        break
                if not found:  # unique
                    candidate = sub
                    break

            result.append(candidate if candidate else "")

        return result

