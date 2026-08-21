class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Precompute LCMs for all subsets using bitmasking to speed up the check function
        # subset_lcm[i] stores the LCM of the coins present in mask i, 
        # and subset_bits[i] stores the set bit count (parity).
        subset_lcm = [1] * (1 << n)
        subset_bits = [0] * (1 << n)
        
        for i in range(1, 1 << n):
            # Find the last set bit to easily derive the LCM from a previously computed submask
            lsb = i & -i
            prev = i ^ lsb
            bit_idx = lsb.bit_length() - 1
            
            # Compute LCM safely, capping at a value higher than any possible answer
            max_limit = coins[0] * k
            val = math.lcm(subset_lcm[prev], coins[bit_idx])
            subset_lcm[i] = min(val, max_limit + 1)
            subset_bits[i] = subset_bits[prev] + 1

        def check(mx: int) -> bool:
            cnt = 0
            for i in range(1, 1 << n):
                if subset_lcm[i] <= mx:
                    if subset_bits[i] % 2 == 1:
                        cnt += mx // subset_lcm[i]
                    else:
                        cnt -= mx // subset_lcm[i]
            return cnt >= k

        # Binary search range
        l, r = 1, min(coins) * k
        ans = r

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans