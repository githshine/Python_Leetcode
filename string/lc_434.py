# 434. Number of Segments in a String
# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:
# Input: s = "Hello"
# Output: 1

class Solution:
    def countSegments(self, s: str) -> int:
        lst = s.split(' ')
        noneEmpty = [x for x in lst if len(x) != 0]
        # print('noneEmpty:',noneEmpty)
        return len(noneEmpty)

if __name__ == '__main__':
    obj = Solution()
    # print(obj.countSegments("Hello, my name is John"))
    # print(obj.countSegments("Hello"))
    print(obj.countSegments("")) #expect: 0
    print(obj.countSegments(" i ")) #expect: 0