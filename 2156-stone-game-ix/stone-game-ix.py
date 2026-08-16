class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for stone in stones:
            cnt[stone % 3] += 1
            
        # If the number of 0s is even, they cancel out.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
            
        # If the number of 0s is odd, Alice needs a large imbalance to win.
        else:
            return abs(cnt[1] - cnt[2]) > 2