n = int(input())
a = 300
b = 60
c = 10

ta = 0
tb = 0
tc = 0

if n % c > 0:
    print(-1)
else:
    if n >= a:
        ta = int(n / a)
        n = n % a
    if n >= b:
        tb = int(n / b)
        n = n % b
    if n >= c:
        tc = int(n / c)
        n = n % c
    print(ta, tb, tc)
