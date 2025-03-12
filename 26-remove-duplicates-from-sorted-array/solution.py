class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        previous = nums[0]
        n = 1
        while n < len(nums):
            if nums[n] == previous:
                nums.pop(n)
            else:
                previous = nums[n]
                n += 1
        return len(nums)
