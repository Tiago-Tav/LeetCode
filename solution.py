class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        times = len(nums)
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums.pop(idx)
                nums.append('_')
                times -= 1
                continue
            idx += 1
        return times
        