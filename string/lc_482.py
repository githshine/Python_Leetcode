# 482. License Key Formatting

# Example 1:
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters 
#               except the first part as it could be shorter as mentioned above.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lst = s.split('-')
        str = ''.join(lst)
        # print("str:", str)
        rst = []
        count = 0
        tmp = ''
        for ch in str[::-1]:
            if ch.isalpha() and ch.islower():
                ch = ch.upper()
            tmp = ch + tmp
            count += 1
            if count % k == 0:
                rst.append(tmp)
                tmp = ''
        if tmp:
            rst.append(tmp) #add the last item
        
        # reverse the list rst
        # print("before reverse:", rst)
        # rst_2 = rst[::-1] 
        # print("after reverse:", rst_2)

        # return "-".join(rst_2)
        return "-".join(rst[::-1])
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.licenseKeyFormatting('5F3Z-2e-9-w',4)) #"5F3Z-2E9W"
    print(obj.licenseKeyFormatting('2-5g-3-J',2)) #"2-5G-3J"