a = int(input())
result = []
i = 2
while a >= i:
    if a % (i) == 0:
        result.append(i)
        a = a / i
        print(i)
    else:
        i += 1
