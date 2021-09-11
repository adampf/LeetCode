

class Solution:

    # def __init__(self, nums, target):
    #     self.nums = nums
    #     self.target = target

    def twoSum(nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(i, j)
                    return [i, j]

        return print("Target value not found given the nums list")

    twoSum(nums=[11, 15, 2, 7], target=17)



