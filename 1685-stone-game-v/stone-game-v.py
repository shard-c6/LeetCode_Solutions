class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # 1. Build a prefix sum array so we can get subarray sums in O(1) time
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        # 2. Top-down DP with memoization
        @lru_cache(None)
        def dp(i, j):
            # Base case: if it's a single stone, Alice can't split it, score is 0
            if i == j:
                return 0
                
            max_score = 0
            
            # Try splitting the array at every possible point k
            for k in range(i, j):
                left_sum = prefix[k + 1] - prefix[i]
                right_sum = prefix[j + 1] - prefix[k + 1]
                
                # Bob throws away the larger half. Alice gets the smaller half.
                if left_sum < right_sum:
                    score = left_sum + dp(i, k)
                elif left_sum > right_sum:
                    score = right_sum + dp(k + 1, j)
                else:
                    # If they are equal, Alice gets to choose the path that yields the max score
                    score = left_sum + max(dp(i, k), dp(k + 1, j))
                    
                if score > max_score:
                    max_score = score
                    
            return max_score

        # Start the game from index 0 to n-1
        return dp(0, n - 1)