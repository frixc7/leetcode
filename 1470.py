class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        matrix = [nums[:n], nums[n:]]
        i = 0
        j = 0

        while j < n:
            nums[i] = matrix[0][j]
            nums[i + 1] = matrix[1][j]
            i += 2
            j += 1

        return nums
