a = int(input())

rs = []
r = list(input())
acnt = 0
bcnt = 0
for i in r:
    if i == "A":
        acnt += 1
    else:
        bcnt += 1
if acnt > bcnt:
    print("A")
elif acnt < bcnt:
    print("B")
else:
    print("Tie")
