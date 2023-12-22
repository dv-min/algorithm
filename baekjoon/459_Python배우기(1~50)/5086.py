rs = []
while 1:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    elif a > 0 and b > 0:
        if b % a == 0:
            rs.append(1)
        elif a % b == 0:
            rs.append(2)
        else:
            rs.append(3)


for r in rs:
    if r == 1:
        print("factor")
    elif r == 2:
        print("multiple")
    else:
        print("neither")
