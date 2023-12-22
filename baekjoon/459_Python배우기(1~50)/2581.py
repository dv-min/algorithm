m = int(input())
n = int(input())
result = []
for i in range(m, n):
    solbool = 0
    for j in range(2, i):
        print(i, j)
        if i % j == 0:
            break
        else:
            result.append(i)
            break


print(result)
result.sort()
print(sum(result))
