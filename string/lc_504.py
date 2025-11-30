# 504. Base 7
# Given an integer num, return a string of its base 7 representation.
# Example 1:
# Input: num = 100
# Output: "202"
# Example 2:
# Input: num = -7
# Output: "-10"

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        isNegative = num < 0
        num = abs(num)
        rst = ''

        while num > 0:
            rst = str(num % 7) + rst
            num = num // 7
        return '-' + rst if isNegative else rst

if __name__ == '__main__':
    obj = Solution()
    print(obj.convertToBase7(0)) #0
    print(obj.convertToBase7(10)) #10
    print(obj.convertToBase7(-10)) # -10
    print(obj.convertToBase7(-7)) # -10
    print(obj.convertToBase7(100)) # 202