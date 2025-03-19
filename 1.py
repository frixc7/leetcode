# FIRST SOLUTION

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# SECOND SOLUTION

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for y in nums:
            if y in hashMap:
                hashMap[y] += 1
            else:
                hashMap[y] = 1

        for x in range(len(nums)):
            result = target - nums[x]

            if result in hashMap and nums[x] != result:
                return [x, nums.index(result)]
            elif result in hashMap and nums[x] == result:
                if hashMap[result] > 1:
                    return [x, nums.index(result, nums.index(result) + 1)]
