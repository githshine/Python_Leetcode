# 1. Two Sum
# Given an array of integers nums and an integer target, 
#   return indices of the two numbers such that they add up to target.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

from typing import List;

class Solution:
    # 常规做法 还行😐
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    return [i,j]
                
    def twoSum_idxChanged(self, nums: List[int], target: int) -> List[int]:
        nums.sort() # 这样会原地修改 nums 数组，导致最终输出的 index 的数据 跟原本的index 数据不同。 不对～
        print("nums:",nums)

        i = 0
        j = len(nums) -1
        while i < j:
            curSum = nums[i] + nums[j]
            if(curSum == target):
                return [i,j]
            elif curSum < target:
                i = i+1
            elif curSum > target:
                j = j-1

                
        

if __name__ == "__main__":
    obj = Solution();
    print(obj.twoSum([2,7,11,15],9) )#[0,1]
    print(obj.twoSum([3,2,4],6)) #[1,2]
