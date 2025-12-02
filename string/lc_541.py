# 541. Reverse String II
# Given a string s and an integer k, reverse the first k characters for every 2k characters 
#     counting from the start of the string.
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rst = '' 
        while len(s) > 0:
            if len(s) > 2*k:
                rst += s[0:k][::-1] + s[k:2*k]
                s = s[2*k:]
            elif len(s) > k:
                # 2*k > len(s) > k
                rst += s[0:k][::-1] + s[k:]
                s = ''
            else:
                # len(s) <= k
                rst += s[0:][::-1]
                s = ''
        return rst
        
                

if __name__ == "__main__":
    obj = Solution()
    print(obj.reverseStr("hello",2))
    print(obj.reverseStr("helloworld",2))
    print(obj.reverseStr("abcdefg",2)) #Output: "bacdfeg"
    print(obj.reverseStr("abcd",2)) #Output:  "bacd"