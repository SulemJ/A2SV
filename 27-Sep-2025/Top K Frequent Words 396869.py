# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        freq = Counter(words)
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(freq[i][0])
        return ans
