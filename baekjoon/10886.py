a = int(input())

ncnt = 0
ycnt = 0
for i in range(a):
    r = int(input())
    if r == 0:
        ncnt += 1
    else:
        ycnt += 1
if ncnt > ycnt:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
