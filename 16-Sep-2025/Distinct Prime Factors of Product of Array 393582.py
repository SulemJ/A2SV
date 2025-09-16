# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(n):
            factors = []
            divisor = 2
            while n > 1:
                if n % divisor == 0:
                    factors.append(divisor)
                    n //= divisor  # Use integer division
                else:
                    divisor += 1
            return factors

        primes =set()
        for i in range(len(nums)):
            primes.update(prime_factors(nums[i]))
        return len(primes)
        # nums.sort()
