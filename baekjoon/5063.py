a = int(input())

rs = []
for i in range(a):
    r, e, c = list(map(int, input().split()))
    if r == e - c:
        rs.append("does not matter")
    elif r < e - c:
        rs.append("advertise")
    elif r > e - c:
        rs.append("do not advertise")
for i in rs:
    print(i)
