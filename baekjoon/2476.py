n = int(input())

rs = []
for i in range(n):
    a, b, c = list(map(int, input().split()))
    if a == b and a == c and b == c:
        r = 10000 + a * 1000
    elif a != b and a != c and b != c:
        if a > b and a > c:
            r = a
        elif b > a and b > c:
            r = b
        else:
            r = c
        r = r * 100
    else:
        if a == b and a == c:
            r = a
        elif b == a and b == c:
            r = b
        else:
            r = c
        r = 1000 + r * 100
    rs.append(r)

print(max(rs))
