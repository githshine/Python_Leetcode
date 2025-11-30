# 520. Detect Capital
# Given a string word, return true if the usage of capitals in it is right.
#  Right means: all capitals or all not capitals or only the first letter is capital

# Example 1:
# Input: word = "USA"
# Output: true
# Example 2:
# Input: word = "FlaG"
# Output: false

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 以下代码不需要。 因为python的切片永远不会报错。 如果你的参数给的超出了有效索引范围，切片只会返回空字符串 ''
        # ❌ 单个索引越界会报错：word[1]
        # ✅ 切片越界不会报错： word[100:]
        # if len(word) == 1:
        #     return True if word == word.lower() or word == word.upper() else False
        
        if word == word.lower() or word == word.upper() or word == word[0].upper() + word[1:].lower():
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.detectCapitalUse("USA")) #true
    print(obj.detectCapitalUse("FlaG")) #false