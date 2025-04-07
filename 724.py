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

# SOL2: with Prefix Sums

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsums = []
        t = 0
        for i in nums:
            t += i
            prefixsums.append(t)

        for i in range(len(nums)):
            leftsum = prefixsums[i-1] if i-1 >= 0 else 0
            rightsum = (prefixsums[-1] - prefixsums[i]) if i != len(nums)-1 else 0
            if rightsum == leftsum:
                return i
        return -1
