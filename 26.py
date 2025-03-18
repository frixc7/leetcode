# FIRST SOLUTION (TLE)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):  # first pointer
            j = i + 1  # second pointer
            while j < len(nums) - k:  # len(nums) - k is the length of the list after element removal
                if nums[i] == nums[j]:
                    for h in range(j + 1, len(nums)):  # removing an element in the middle of the list
                        nums[h - 1] = nums[h]
                    k += 1  # incrementing this counter by 1 to keep track of how many elements were removed
                else:
                    j += 1  # j is only incremented if no element is removed so that this pointer doesn’t skip an element after removal
        return len(nums) - k  # this is the original length of the array minus the number of elements removed
        # this takes a lot of time since it's O(n^3). Should be O(n^2) max.

# SECOND SOLUTION (TLE)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i + 1
        k = 0
        while i < len(nums) - k:
            if j < len(nums) - k:
                if nums[i] == nums[j]:
                    for h in range(j + 1, len(nums)):
                        nums[h - 1] = nums[h]
                    k += 1
                    continue
                else:
                    j += 1
                    continue
            i += 1
            j = i + 1
        return len(nums) - k

# THIRD SOLUTION

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        j = 1
        while j < len(nums):
            if nums[j] in nums[:p]:
                j += 1
            else:
                nums[p] = nums[j]
                p += 1
                j = p
        return len(nums[:p])
