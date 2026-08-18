class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Edge case: k == 1
        if k == 1:
            counts = Counter(nums)
            valid = [num for num, freq in counts.items() if freq == 1]
            return max(valid) if valid else -1

        # Edge case: k == n
        if k == n:
            return max(nums)

        # General case: count appearances across all subarrays of size k
        # Since k < n, elements appearing in exactly 1 subarray are typically boundary elements
        from collections import defaultdict

        sub_counts = defaultdict(int)

        for i in range(n - k + 1):
            sub = nums[i : i + k]
            seen_in_this_sub = set(sub)
            for x in seen_in_this_sub:
                sub_counts[x] += 1

        valid = [num for num, freq in sub_counts.items() if freq == 1]
        return max(valid) if valid else -1  