t = int(input())

rs = []
for i in range(t):
    n = int(input())
    ra = ""
    rb = 0
    for j in range(n):
        a, b = list(input().split())

        if rb == 0:
            ra = a
            rb = b
        else:
            if int(b) > int(rb):
                ra = a
                rb = b
    rs.append(ra)

for r in rs:
    print(r)
