# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram_01(self, s: str, t: str) -> bool:
        # lst_s_0 = list(s)
        # print('lst_s_0:', lst_s_0)
        
        # lst_s = list(s).sort()
        # print('lst_s:', lst_s)  # 这里的输出结果是 None，因为 sort() 函数是对数组进行的原地排序，sort() 函数本身返回的结果为 None -- 这是Python的一个经典坑
        lst_s = list(s)
        lst_s.sort()
        s_2 = ''.join(lst_s)
        # 这里的 list(t) 可以省略，因为 sorted() 既可以对array 排序 也可以对 string 排序，因为他们都 iteraiterable
        t_2 = ''.join(sorted(list(t))) # sorted() 返回一个排序后的 新数组
        # print('s_2:',s_2)
        # print('t_2:',t_2)
        return s_2 == t_2
    
    def isAnagram(self, s: str, t: str) -> bool:
        chDict = {}
        for ch in s:
            chDict[ch] = chDict[ch] + 1 if chDict.get(ch,0) != 0 else 1
        for ch in t:
            if chDict.get(ch,0) != 0:
                chDict[ch] -= 1 
                if chDict[ch] == 0:
                  del chDict[ch]
            else:
                return False
        return len(chDict) == 0
            

if __name__ == '__main__':
    obj = Solution()
    print(obj.isAnagram('anagram','nagaram')) #true
    print(obj.isAnagram('rat','car')) #false
    print(obj.isAnagram('a','abb')) #false
