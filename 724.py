# SOL1: Brute force

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == len(nums):
                if sum(nums[:i]) == 0:
                    return i
            elif sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
