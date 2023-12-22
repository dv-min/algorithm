def gcd(a, b):
    if b > 0:
        r = a % b
    else:
        return a
    return gcd(b, r)


rs = []
for n in range(int(input())):
    a, b = list(map(int, input().split()))
    rs.append(int(a * b / gcd(a, b)))


for r in rs:
    print(r)
