import math as math

cnt = int(input())
result = []
for i in range(cnt):
    n = list((input().split()))
    val = ""
    k = ""
    for j in n:
        if j == "%":
            val += "+ 5"
        elif j == "@":
            val += "* 3"
        elif j == "#":
            val += "- 7"
        else:
            val += j
        k = eval(val)
        val = str(k)
    result.append(k)
for rs in result:
    print(f"{rs:.2f}")
