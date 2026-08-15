class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_non_zero = False

        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
            
        if total_xor != 0:
            return len(nums)
        elif has_non_zero:
            return len(nums)-1
        else:
            return 0