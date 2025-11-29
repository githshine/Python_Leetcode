# 500. Keyboard Row
# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Explanation:
# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
# Example 2:
# Input: words = ["omk"]
# Output: []
# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

from typing import List
class Solution:
    def isOneLineWord(self,word):
        keyBoardLines = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for keyBoard in keyBoardLines:
            count = 0
            for ch in word:
                if ch not in keyBoard:
                    break
                count += 1
            if count == len(word):
              return True
            
        return False
    
    def findWords(self, words: List[str]) -> List[str]:
        isOneLineWordLst = [self.isOneLineWord(word.lower()) for word in words]
        rstLst = []
        for isOneWord, word in zip(isOneLineWordLst,words):
            if isOneWord:
                rstLst.append(word)
        return rstLst
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.findWords(["Hello","Alaska","Dad","Peace"])) # Output: ["Alaska","Dad"]
    print(obj.findWords(["Hello",'qwe',"Alaska","cderfv","Dad"])) # Output: ["Alaska","Dad"]
    print(obj.findWords(["omk"])) #[]
    print(obj.findWords(["adsdf","sfd"])) #["adsdf","sfd"]

        
