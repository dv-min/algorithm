n, m = map(int, input().split())

a = []
b = []
c = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

# print(m)
for k in range(n):
    for j in range(m):
        print(a[k][j] + b[k][j], end=" ")
    print()
