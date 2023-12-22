x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

x = []
x.append(x1)
x.append(x2)
x.append(x3)
x.sort()

if x[1] == x[0]:
    x4 = x[2]
else:
    x4 = x[0]

y = []
y.append(y1)
y.append(y2)
y.append(y3)
y.sort()

if y[1] == y[0]:
    y4 = y[2]
else:
    y4 = y[0]

print(x4, y4)
