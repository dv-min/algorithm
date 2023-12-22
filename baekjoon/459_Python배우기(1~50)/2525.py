h, m = list(map(int, (input().split())))
run = int(input())

addh = int(h + (m + run) / 60)
if addh - 24 >= 0:
    addh = addh - 24

addm = (m + run) % 60

print(addh, addm)
