class Solution:
    def largestElement(self, nums):
        # # sortest method
        # return max(nums)

        # implemenation
        largest = nums[0]
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]

        return largest
