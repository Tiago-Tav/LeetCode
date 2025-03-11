class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}
        for n in range(len(nums)):
            if (target - nums[n]) in numMap:
                return [numMap[target - nums[n]], n]
            numMap[nums[n]] = n
