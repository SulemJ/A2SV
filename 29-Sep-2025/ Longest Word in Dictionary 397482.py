# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        st, res = set(), ""
        st.add("")
        for word in words:
            if word[:-1] in st:
                if len(word) > len(res):
                    res= word
                st.add(word)
        return res