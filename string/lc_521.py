# 521. Longest Uncommon Subsequence I
# Given two strings a and b, return the length of the longest uncommon subsequence between a and b. 
#         If no such uncommon subsequence exists, return -1.

# Example 1:
# Input: a = "aba", b = "cdc"
# Output: 3
# Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
# Note that "cdc" is also a longest uncommon subsequence.
# Example 2:
# Input: a = "aaa", b = "bbb"
# Output: 3
# Explanation: The longest uncommon subsequences are "aaa" and "bbb".
# Example 3:
# Input: a = "aaa", b = "aaa"
# Output: -1
# Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        lestUStr = ''
        longerStr = a if len(a) > len(b) else b
        shorterStr = b if len(a) > len(b) else a
        l,r = 0, len(longerStr)

        while l < r:
            if longerStr[l:r] not in shorterStr and r-l > len(lestUStr):
                lestUStr = longerStr[l:r]
                return len(lestUStr)
            elif l < r-1:
                r -= 1
                if longerStr[l:r] not in shorterStr and r-l > len(lestUStr):
                    lestUStr = longerStr[l:r]
                    return len(lestUStr)
            elif l+1 < r:
                l += 1
                if longerStr[l:r] not in shorterStr and r-l > len(lestUStr):
                    lestUStr = longerStr[l:r]
                    return len(lestUStr)
            else:
                l += 1
                r -= 1
        return -1
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.findLUSlength("aba", "cdc")) #a = "aba", b = "cdc" -> 3
    print(obj.findLUSlength("aaa", "bbb")) #a = "aaa", b = "bbb" -> 3
    print(obj.findLUSlength("aaa", "aaa")) #a = "aaa", b = "aaa" -> -1
    print(obj.findLUSlength("abcdefg", "abcdefg")) #  -1
    print(obj.findLUSlength("abcdefg", "abcedfg")) #  7
    print(obj.findLUSlength("abcdefgh", "abcedfg")) #  8