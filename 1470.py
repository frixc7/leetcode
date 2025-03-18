class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        matrix = [nums[:n], nums[n:]]
        i, j = 0, 0

        while j < n:
            nums[i], nums[i + 1] = matrix[0][j], matrix[1][j]
            i += 2
            j += 1

        return nums
