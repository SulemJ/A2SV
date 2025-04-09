# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        count = 0
        left = 0
        
        # Use array for faster lookups
        char_count = [0, 0, 0]  # counts for 'a', 'b', 'c'
        
        for right in range(len(s)):
            # Convert character to index and increment count
            char_count[ord(s[right]) - ord('a')] += 1
            
            # Check if all 3 characters exist in the current window
            # Instead of calling all() repeatedly, we check directly
            while char_count[0] > 0 and char_count[1] > 0 and char_count[2] > 0:
                char_count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            # Add count of valid starting positions
            count += left

            
        return count 
