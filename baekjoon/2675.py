n = int(input())
result = []
for n in range(n):
    a, b = input().split(" ")
    str = ""
    for i in range(len(b)):
        for j in range(int(a)):
            str += b[i : i + 1]
    result.append(str)

for rs in result:
    print(rs)
