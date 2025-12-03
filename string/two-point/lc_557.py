# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within
#   a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"

class Solution:
    
    def reverseWords_01(self, s: str) -> str:
        def reverseOneWord(s: str) -> str:
            word = list(s) # a list
            l,r = 0,len(word) -1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            return "".join(word)
        
        wordLst = s.split(' ')

        # for word in wordLst:
        #     print("word:", word)
        #     word = reverseOneWord(word)  # 这种方式是把数据从数组中取出来 进行一系列计算，但是并不直接修改原数组
        #     print("word after reversing:", word)
        wordLst = [reverseOneWord(word) for word in wordLst] #这里会修改原数组
        # print(' '.join(wordLst))
        return ' '.join(wordLst)
    
    def reverseWords(self, s: str) -> str:
        wordLst = s.split(' ')
        wordLst = [word[::-1] for word in wordLst]
        return ' '.join(wordLst)

if __name__ == "__main__":
    obj = Solution()
    print(obj.reverseWords("Let's take LeetCode contest")) # Output: "s'teL ekat edoCteeL tsetnoc"
    print(obj.reverseWords("Mr Ding")) # "rM gniD"