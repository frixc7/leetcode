class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixlist = []
        total = 0
        for i in nums:
            total += i
            self.prefixlist.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preright = self.prefixlist[right]
        preleft = self.prefixlist[left - 1] if left > 0 else 0
        return preright - preleft

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
