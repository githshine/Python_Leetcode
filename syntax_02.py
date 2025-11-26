# 反转列表 [1,2,3,4]，打印结果
lst = [1,2,3,4]
lst = lst[::-1]
print(lst)

# 统计 "aaabbc" 每个字符出现次数
from collections import Counter
str = 'aaabbc'
c = Counter(str)
print(c)
print(c.most_common(2))
print(c.most_common(len(str)))
for tuple in c.most_common(len(str)):
  print("tuple:", tuple[0],tuple[1])

# 判断 [1,2,3,2] 是否有重复元素
lst = [1,2,3,2]
print( len(lst) != len(set(lst)) )

# 判断 "racecar" 是否回文
str = 'racecar'
str = 'raceca'
print(str == str[::-1])

# a=[1,2,3]; b=a; b.append(4); print(a) 输出什么？为什么
a = [1,2,3]
b = a
c = [1,2,3,4]
b.append(4)
print("a and b:", a, b)
print("a == b: ", a==b)
print("b is a: ", b is a) # True, b is a
print("c == a: ", c==a)  # only compare the content : True
print("c is a: ", c is a) # compare the address : Flase

# 从 [1,-2,3] 中取正数并平方
lst = [1,-2,3]
lst1 = [x for x in lst if x > 0]  # filter
print(lst1)
lst2 = [x*x for x in lst1]  # map
print(lst2)

# 遍历 names=["Alice","Bob"], scores=[90,85] 打印 "Alice: 90"
names=["Alice","Bob"]
scores=[90,85]
for name,score in zip(names,scores):
  print("%s: %d" % (name,score))

# 对 [1,-2,3] +1 并过滤负数
lst = [1,-2,3]
lst1 = [x+1 for x in lst]
print("lst1:",lst1)
lst2 = [x for x in lst1 if x > 0]
print("lst2:",lst2)

# 对 [("Alice",90),("Bob",85)] 按成绩降序排序
lst = [("Alice",80),("Bob",85)]
print(sorted(lst, key=lambda x: x[1]))
print(sorted(lst, key=lambda x: x[1], reverse=True))
print(sorted(lst, key=lambda x: -x[1]))

# 对列表 [5,2,9,1] 取偶数排序并平方
lst = [5,2,9,1,0,4]
evenLst = sorted([x for x in lst if x % 2 == 0])
print(evenLst)
powerLst = [x*x for x in evenLst]
print(powerLst)

# 统计 "leetcode" 每个字符次数
from collections import Counter
str = 'leetcode'
c = Counter(str)
print(c)

str = 'leetcode'
dict = {}
for ch in str:
  dict[ch] = dict.get(ch,0) + 1
for key,value in dict.items():
  print(key,value)


# 判断 "level" 是否回文
str = 'level'
print(str == str[::-1])

# 最大子数组和（简单版）
# [1,-2,3,4,-1] 找最大和
lst = [1,-2,3,4,-1,2]
lst = [-9,-8,-7,-6,-5,-4,3,-2]
maxSum = float('-inf')
sum = 0

for n in lst:
  if sum < 0:
    sum = n
  else:
    sum += n
  if sum > maxSum:
    maxSum = sum
print(maxSum)

# 移除排序数组 [1,1,2,2,3] 重复元素
lst = [1,1,2,2,3] 
if len(lst) == 1:
  print(lst)
l,r = 1,1
for r in range(1,len(lst)):
  if lst[r] != lst[r-1]:
    lst[l] = lst[r]
    l += 1
print(lst)
del lst[l:]
print(lst)

# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it 
#   while maintaining the relative order of the non-zero elements.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
lst = [0,1,0,3,12,3]
size = len(lst)
l,r = 0,0
for r in range(0,len(lst)):
  if lst[r] != 0:
    lst[l] = lst[r]
    l += 1
print("after rewrite:",lst)
del lst[l:]
print("after delete:", lst)
lst += [0] * (size - len(lst))
print(lst)

# 找数组 [2,7,11,15] 两数和为 9
target = 9
lst = [1,2,7,11,15]
l,r = 0, len(lst) -1
print(l,r)
while l < r:
  sum = lst[l] + lst[r]
  if sum == target:
    print("satisfied indexes:", l,r)
    break
  elif sum < target:
    l +=1
  elif sum > target:
    r -= 1

# 写一个 Person 类，打印 name
class Person:
  def __init__(self,name):
    self.name = name
  def __str__(self, name):
    return name

p = Person("Hannah")
print(p.name)

