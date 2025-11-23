# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice 
#       in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

from typing import List
from collections import Counter

class Solution:
    def containsDuplicate_01(self, nums: List[int]) -> bool:
        numSet = set(nums)
        return len(numSet) != len(nums)
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        # for v,c in counter.items():
        most_v, most_c = counter.most_common(1)[0]  # most_commin(n) return a list of tuple
        return True if most_c >= 2 else False
                

if __name__ == "__main__":
    obj = Solution()
    print(obj.containsDuplicate([1,2,3,1]))
    print(obj.containsDuplicate([1,2,3,4]))