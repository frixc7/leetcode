class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for i in nums:
            if i in countMap:
                countMap[i] += 1
            else:
                countMap[i] = 1

        for k, v in countMap.items():
            if v > 1:
                return True

        return False
