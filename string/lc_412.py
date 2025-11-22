# 412. Fizz Buzz
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(n): # starts from 0 to (n-1)
            num = i+1
            if num % 5 == 0 and num % 3 == 0:
                lst.append('FizzBuzz')
            elif num % 3 == 0:
                lst.append('Fizz')
            elif num % 5 == 0:
                lst.append('Buzz')
            else:
                lst.append('' + str(num))

        return lst

if __name__ == "__main__":
    obj = Solution()
    print(obj.fizzBuzz(3))
    print(obj.fizzBuzz(5))
    print(obj.fizzBuzz(15))
