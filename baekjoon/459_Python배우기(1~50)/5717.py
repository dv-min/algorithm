rs = []
while 1:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    rs.append(a + b)


for r in rs:
    print(r)
