print('Hello World!')

s = "aaabXYc"
print(s.strip("abc"))
s = "aaabXabcYc" # strip() 函数只会把两端中 属于这个集合（参数）的字符 移除。并不会影响到中间的内容
print(s.strip("abc"))

s = "cabbbac"
print(s.strip("abc"))
print(s.replace("abc",''))


arr = ['a', 'b', 'c']

for idx, ch in enumerate(arr):
    print(idx, ch)
for idx, ch in enumerate(arr,5):
    print(idx, ch)

# ❌ 错误示例（共享同一列表）
def bad_append(x, arr=[]):
    arr.append(x)
    return arr
print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2]  <-- 意外累积
# ✅ 正确示例（None 模式）
def good_append(x, arr=None):
    if arr is None:
        arr = []
    arr.append(x)
    return arr
print(good_append(1))  # [1]
print(good_append(2))  # [2]   <-- 安全

a = [1,2,3]
b = a
b.append(4)
print(a) 

lst1 = [1,2,3,4]
print(lst1, lst1[::-1])

s = "aaabbc"
count = {}
for c in s:
    count[c] = count.get(c,0)+1
print(count)

def isPalim(str):
    return str[::-1] == str
print(isPalim('racecar')) #true
print(isPalim('Hannah')) #false
print(isPalim('hannah')) #true