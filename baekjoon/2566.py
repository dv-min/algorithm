a = []
maxCnt = 0
x = 0
y = 0

for i in range(9):
    a.append(list(map(int, input().split())))

for k in range(len(a)):
    for j in range(len(a[k])):
        if maxCnt < a[k][j]:
            maxCnt = a[k][j]
            x = k
            y = j

print(maxCnt)
print(x + 1, y + 1)
