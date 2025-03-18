class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j, k = 0, len(nums) - 1, 0

        for h in nums:
            if h != val:
                k += 1

        while i != j and i < len(nums) and j > -1:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1

        return k
