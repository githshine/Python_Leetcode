# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it 
#   while maintaining the relative order of the non-zero elements.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # leftIdx = rightIdx = 0
        # 不能使用for 循环，因为这里 idx 是由 range 内部的iterator 控制的，idx -= 1 对它毫无影响
        #     而且在 for循环中操作列表（特别是进行pop删除的动作），可能会导致后续的循环中数组越界 等 bug
        # for idx in range(0, len(nums)):
        #     if nums[idx] == 0:
        #         count += 1
        #         nums.pop(idx)
        #         nums.append(0)
        #         idx -= 1
        #     if idx == len(nums) - count:
        #         break

        # 应该使用 while 循环 来实现对loop 的完全控制 -- 可以前进或者后退 index
        i =0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

                count += 1
            else:
                i += 1
            if i == len(nums) - count:
              break

        print("nums:",nums)

if __name__ == '__main__':
    obj = Solution()
    obj.moveZeroes([0,1,0,3,12])
    obj.moveZeroes([0])
    obj.moveZeroes([0,0,1])
    obj.moveZeroes([3,2,1])