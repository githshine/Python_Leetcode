# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
#         determine if the input string is valid.

# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {')':'(', '}':'{',']':'['}
        rstLst = []
        # for ch in s:
        #     if len(rstLst) == 0:
        #         rstLst.append(ch)
        #     else:
        #         if parDict.get(ch,None) == rstLst[-1]:
        #             rstLst.pop()
        #         else:
        #             rstLst.append(ch)
        for ch in s:
            if len(rstLst) > 0 and rstLst[-1] == parDict.get(ch,None):
                rstLst.pop()
            else:
                rstLst.append(ch)
        # print('rstLst:', rstLst)
        return len(rstLst) == 0
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.isValid("()")) # true
    print(obj.isValid("()[]{}")) # true
    print(obj.isValid('(]')) # true