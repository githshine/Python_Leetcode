# 415. Add Strings
# Given two non-negative integers, num1 and num2 represented as string, return 
#                       the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers 
#       (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

class Solution:
    def addStrings_01(self, num1: str, num2: str) -> str:
        numLst1 = list(num1)
        numLst2 = list(num2)

        idx = 0
        sum = 0
        len1 = len(numLst1)
        while idx < len1:
            numStr = numLst1[idx]
            # print("numStr:", numStr)
            sum += int(numStr) * pow(10,len1 - 1 - idx)
            # print("sum:", sum)
            idx += 1
        idx = 0
        len2 = len(numLst2)
        while idx < len2:
            numStr = numLst2[idx]
            # print("numStr:", numStr)
            sum += int(numStr) * pow(10, len2 - 1 -idx)
            # print("sum:", sum)
            idx += 1
        return str(sum)
    
    def addStrings(self, num1: str, num2: str) -> str:
        maxLen = max(len(num1), len(num2))
        numLst1 = list(num1.zfill(maxLen))
        numLst2 = list(num2.zfill(maxLen))

        # numLst1.reverse()
        # str does not has reversr() function
        #   but it can be reversed using slicing -- str[::-1]

        idx = maxLen - 1
        sumLst = []
        pre = 0
        while idx >= 0:
            if int(numLst1[idx]) + int(numLst2[idx]) + pre < 10: 
              sumLst.insert(0, str( int(numLst1[idx]) + int(numLst2[idx]) + pre ) )
              pre = 0
            else:
              sumLst.insert(0, str( int(numLst1[idx]) + int(numLst2[idx]) + pre - 10 ))
              pre = 1
            idx -= 1
        if pre > 0:
            sumLst.insert(0, str(pre))
        # return sumLst.join('')
        return ('').join(sumLst)

if __name__ == '__main__':
    obj = Solution()
    print(obj.addStrings("12","34")) #46
    print(obj.addStrings("11","123")) #134
    print(obj.addStrings("456","77")) #533
    print(obj.addStrings("0","0")) #0
    print(obj.addStrings("1","9")) # 10