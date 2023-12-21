a = list(str(input()))


rs = 0
for i in range(len(a)):
    if i > 0:
        if a[i - 1] == a[i]:
            rs += 5
        else:
            rs += 10
    else:
        rs += 10

print(rs)
