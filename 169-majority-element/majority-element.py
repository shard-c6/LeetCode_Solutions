class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate= 0
        vote_count = 0
        for i in nums:
            if vote_count == 0:
                candidate = i
            if i == candidate:
                vote_count+=1
            else:
                vote_count -=1
        return candidate