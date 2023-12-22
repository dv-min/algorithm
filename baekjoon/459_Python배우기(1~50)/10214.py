n = int(input())

rs = []
for i in range(n):
    sa = 0
    sb = 0
    for k in range(9):
        a, b = list(map(int, input().split()))
        sa += a
        sb += b
    if sa == sb:
        rs.append("Draw")
    elif sa > sb:
        rs.append("Yonsei")
    else:
        rs.append("Korea")
    # print("rs : ", sa, sb)

for r in rs:
    print(r)
