class Solution:
    def checkDivisibility(self, n: int) -> bool:
        N= list(str(n))
        sum_n = sum(int(i) for i in N)
        prod_n = math.prod(int(i) for i in N)
        return n %(sum_n + prod_n) == 0