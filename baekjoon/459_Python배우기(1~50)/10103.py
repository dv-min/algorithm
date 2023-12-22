n = int(input())
sa = 100
sb = 100

for i in range(n):
    a, b = list(map(int, input().split()))
    if a == b:
        continue
    elif a > b:
        sb = sb - a
    else:
        sa = sa - b

print(sa)
print(sb)
