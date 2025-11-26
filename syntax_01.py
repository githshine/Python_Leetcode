# 练习：从列表 [1,-2,3] 中取正数并平方

lst = [1,-2,3]
lst2 = [x*x for x in lst if x > 0]
print(lst2)

lst1 = list(filter(lambda x: x > 0,lst))
print("lst1:",lst1)
lst3 = map(lambda x: x * x, lst1)
print("lst3:",list(lst3))

names = ["Alice","Bob"]
scores = [90,85]
for name,score in zip(names, scores):
  print(name, score)

print("zip result:",list(zip(names, scores)))

tupl = [("Alice",90),("Bob",85)]
print(sorted(tupl, key=lambda x : x[1]))
print(sorted(tupl, key=lambda x : x[1],reverse=True))

# 按多个条件排序，例如：
# 成绩降序
# 如果成绩相同，按名字升序
students = [("Alice", 90), ("Bob", 85), ("Carol", 90),("Kelly",85), ("Jack",85)]
print(sorted(students, key=lambda x:(-x[1], x[0])))

s = 'aaabbbcccc'
dic = {}
for ch in s:
  dic[ch] = dic.get(ch,0) + 1
print(dic)

# 题：求最大子数组和（简单版）
lst = [1, -2, 4, -3, -5, 2, 1, 0, -8, 14] #11
# lst = [1, -2, 4, -3, -5, 2, -1, -1, 8, -4]
lst = [1, 2, 4, -2, -5, 2, 1, 0, -8, -14] #11
sum = 0
maxSum = float('-inf')

for num in lst:
  # sum += num
  if sum <= 0:
    sum = num
  else:
    sum += num

  if sum > maxSum:
    maxSum = sum
print(maxSum)

# 题：移除排序数组的重复元素
lst = [1,1,2,2,3,4,5,5,5,5]
# print("Directly use set:", set(lst))
s = set()

len = len(lst)
idx = 0
while idx < len:
  n = lst[idx]
  if n in s:
    lst.remove(n)
    len -= 1
  else:
    s.add(n)
    idx += 1
print(lst)