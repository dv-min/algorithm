a, b, c = list(map(int, input().split()))
if a == b and b == c:
    rs = 10000 + a * 1000
elif a != b and b != c and a != c:
    if a >= b and a >= c:
        rs = a * 100
    elif b >= a and b >= c:
        rs = b * 100
    else:
        rs = c * 100
else:
    if a == b or a == c:
        rs = 1000 + a * 100
    elif b == a or b == c:
        rs = 1000 + b * 100
    else:
        rs = 1000 + c * 100
print(rs)
