class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            if num > current_sum + num:
                current_sum = num
            else:
                current_sum = current_sum + num

            if max_sum > current_sum:
                max_sum = max_sum
            else:
                max_sum = current_sum


        return max_sum
    

sol = Solution()
nums=[-2, 1, -3, 4, -1, 2, 1,-5, 4]
print("max sum is --> " , sol.maxSubArray(nums))
nums=[1]
print("max sum is --> " , sol.maxSubArray(nums))
nums=[5,4,-1,7,8]
print("max sum is --> " , sol.maxSubArray(nums))