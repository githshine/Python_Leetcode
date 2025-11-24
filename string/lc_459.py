# 459. Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it 
#               and appending multiple copies of the substring together.

# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:
# Input: s = "aba"
# Output: false
# Example 3:
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Must start from the beginning
        if not s:
            return False
        
        idx = 1
        while idx < len(s):
            subStr = s[0:idx]
            if len(s) % len(subStr) != 0:
                idx += 1
                continue
            multiple = len(s) // len(subStr)
            if s != subStr * multiple:
                idx += 1
                continue
            else:
                return True
        return False
        # s = "abcd"
        # print(s[-1:0:-1]) #Output: dcb [反向取切片。 End index 是不包含的]

if __name__ == '__main__':
    obj = Solution()
    print(obj.repeatedSubstringPattern("abab")) #true
    print(obj.repeatedSubstringPattern("ababab")) #true
    print(obj.repeatedSubstringPattern("aba")) #false
    print(obj.repeatedSubstringPattern("abcabcabcabc")) # true
    print(obj.repeatedSubstringPattern("")) # true