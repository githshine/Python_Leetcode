# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
#  that the number could represent. Return the answer in any order. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        print(list('abc'))
        rstList = list(letterMap.get(digits[0]))
        print(rstList)
        # rstList = rst.split('*')
        for ch in digits[1:]:
            length = rstList
            for c in letterMap.get(ch):
                for curLett in rstList:
                    rstList.append(c + curLett)
            rstList = rstList[length:]
        return rstList
if __name__ == "__main__":
    obj = Solution()
    print(obj.letterCombinations('23')) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(obj.letterCombinations('2')) # ["a","b","c"]