a = input()

r1 = 0
r2 = 0
if len(a) > 1:
    if a[0:1] == "A":
        r1 = 4.0
    elif a[0:1] == "B":
        r1 = 3.0
    elif a[0:1] == "C":
        r1 = 2.0
    elif a[0:1] == "D":
        r1 = 1.0

    if a[1:2] == "+":
        r2 = 0.3
    elif a[1:2] == "0":
        r2 = 0.0
    elif a[1:2] == "-":
        r2 = -0.3
else:
    r1 = 0.0
    r2 = 0.0


print(r1 + r2)
