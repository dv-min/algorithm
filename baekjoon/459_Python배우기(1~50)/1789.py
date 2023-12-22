a = int(input())
cnt = 0
i = 0
while a > 0:
    i += 1
    cnt += 1
    if a <= cnt * 2:
        cnt = a
    a -= cnt
print(i)
