#W6A1
nums = list(map(int, input("Nhập dãy số:").split()))
new = []
for i in nums:
    if i not in new:
        new.append(i)
print(new)
#W6A2
num = list(map(int, input("Nhập dãy số:").split()))
new = []
tong = 0
for i in num:
    tong += i
    new.append(tong)
print(new)
#W6A3
nums = tuple(map(int, input("Nhập dãy số:").split()))
n = int(input("Xoay trái:"))
nums = nums[n-1:] + nums[:n-1]
print(nums)
#W6A4
A = list(map(str, input("Nhập dãy:").split()))
keys = {}
for a in A:
    key, value = a.split(':')
    if key in keys:
        keys[key].append(value)
    else:
        keys[key] = value
        keys[key] = [keys[key]]
print(keys)
#W6A5
nums = list(map(int, input("Nhập dãy số nguyên:").split()))
dicts = {}
po = 0
ze = 0
neg = 0
for i in nums:
    if i < 0:
        neg += 1
    elif i > 0:
        po += 1
    elif i == 0:
        ze += 1
dicts['positives'] = po
dicts['negatives'] = neg
dicts['zero'] = ze
print(dicts)
#W6A6
nums = list(map(int, input("Nhập dãy số nguyên:")))
for i in nums:
    tong += i
print(tong)
#W6A7
nums = tuple(map(str, input("Nhập dãy:").split()))
print(nums[0], nums[-1], nums[::-1])
#W6A8
strings = list(map(str, input().split()))
dicts = {}
for i in strings:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1
print(dicts)
#W6A9
import ast
d1 = ast.literal_eval(input("Nhập dict thứ nhất:"))
d2 = ast.literal_eval(input("Nhập dict thứ hai:"))
for key, value in d2.items():
    if key in d1:
        d1[key] += value
    else:
        d1[key] = value
result = sorted(d1.items())
print(result)
#W6A10
nums = list(map(int, input("Nhập dãy số nguyên:").split()))
n = int(input("Nhập số:"))
result = set()
for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == n:
            result.add((nums[i], nums[j]))
result = sorted(list(result))
print(result)
#W6A11
A = []
B = []
nums = list(map(int, input().split()))
for i in nums:
    if i % 2 == 0:
        A.append(i)
    else:
        B.append(i)
print(tuple(A))
print(tuple(B))
#W6A12
nums = list(map(int, input("Nhập dãy số:").split()))
num = {}
max_group = []
for i in nums:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
    maxn = 0
for i in num.values():
    if maxn < i:
        maxn = i
for key, value in num.items():
    if value == maxn:
        max_group.append(key)
print(min(max_group))
#W6A13
strings = list(map(str, input("Nhập dict:").split()))
dicts = {}
for i in range(1, len(strings), 2):
    dicts[strings[i]] = strings[i - 1]
print(dicts)
#W6A14
list1 = list(map(int, input("Nhập list 1:").split()))
list2 = list(map(int, input("Nhập list 2:").split()))
new = set(list1) & set(list2)
print(list(new))
#W6A15
strings = list(map(str, input("Nhập dict:").split()))
n = int (input("Nhập giá trị:"))
dicts = {}
result = {}
for i in range(0,len(strings)- 1, 2):
    dicts[strings[i]] = int(strings[i+1])
for key, value in dicts.items():
    if value > n:
        result[key] = value
print(result)
#W6A16
n = int(input("Nhập số hàng:"))
m = int(input("Nhập số cột:"))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        val = int(input(f"a[{i}][{j}] = "))
        row.append(val)
    matrix.append(row)
for i in range(m):
    for j in range(n):
        print(f"{matrix[i][j]:>4}", end = " ")
    print()
#W6A17
n = int(input("Nhập cỡ ma trận: "))
while True:
    matrix = [list(map(int,input("Nhập dòng: ").split())) for i in range(n)]
    if len(matrix) == n:
        break
    else:
        print(f"Ma trận có {n} hàng")
i = 0
j = 0
print("Đường chéo chính:")
while i < n and j < n:
    print(matrix[i][j], end = " ")
    i += 1
    j += 1
print()
print("Đường chéo phụ:")
i = 0
j = n - 1
while i < n and j >= 0:
    print(matrix[i][j], end = " ")
    i += 1
    j -= 1
#W6A18
m, n, k = map(int,input("Nhập ").split())
while True:
    matrix = [list(map(int, input("Nhập hàng:").split())) for i in range(m)]
    if len(matrix) == m:
        break
    print(f"Ma trận có {m} hàng")
if k - 1 < n:
    print(f"Tổng trên hàng {k}:")
    hang = 0
    for i in range(n):
        hang += matrix[k - 1][i]
    print(hang)
if k - 1< m:
    print(f"Tổng trên cột {k}:")
    cot = 0
    for i in range(m):
        cot += matrix[i][k - 1]
    print(cot)
#W6A19
nums = list(map(int, input("Nhập dãy số: ").split()))
n = max(nums)
for i in range(len(nums)):
    if nums[i] == n:
        print(i)
        break
#W6A20
nums = list(map(int, input("Nhập dãy số: ").split()))
n = int(input())
for i in range(len(nums)):
    if nums[i] == n:
        print(i)
        break
#W6A21
strings = list(map(str, input("Nhập chuỗi: ").split()))
dicts = {}
for i, item in enumerate(strings):
    if item not in dicts:
        dicts[item] = [i]
    else:
        dicts[item].append(i)
dicts = {key: tuple(value) for key, value in dicts.items()}
print(dicts)
#W6A22
nums = list(map(int, input("Nhập dãy số: ").split()))
n = max(nums)
for i in range(len(nums)):
    if nums[i] == n:
        print(i)
        break