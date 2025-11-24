# 53. Maximum Subarray
# Given an integer array nums, find the subarray 
#         with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        strIdx = 0
        # for strIdx in range(0, len(nums)):
        curSum = 0
        for idx in range(strIdx, len(nums)):
            curSum += nums[idx]
            if curSum < nums[idx]:
                strIdx = idx
                curSum = nums[strIdx]
                
            maxSum = curSum if curSum > maxSum else maxSum

        return maxSum
if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([-2,1])) # 1
    print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(obj.maxSubArray([1])) # 1
    print(obj.maxSubArray([-1])) # -1
    print(obj.maxSubArray([4,-5,1])) # 4