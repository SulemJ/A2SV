# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        total = 0
        for i in range(1, n+1):
            total ^= i
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]

        # Step 3: Find perm[0]
        perm0 = total ^ odd_xor

        # Step 4: Rebuild permutation
        perm = [perm0]
        for e in encoded:
            perm.append(perm[-1] ^ e)

        return perm
