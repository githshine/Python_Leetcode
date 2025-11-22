
class Solution:
    def longestPalindrome(self, s:str) -> int:
        count = 0
        strSet = set()
        for ch in s:
            if ch in strSet:
                strSet.remove(ch)
                count += 2
            else:
                strSet.add(ch)

        # 如果还有剩余字符，可以放在回文中心
        return count + (1 if len(strSet) > 0 else 0)

if __name__ == '__main__':
    # testing
    obj = Solution()
    print(obj.longestPalindrome("Aa"))
    print(obj.longestPalindrome("abccccdd")) #7