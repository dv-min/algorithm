h, m, s = list(map(int, (input().split())))


runs = int(input())

tots = s + runs
totm = m + int(tots / 60)
toth = h + int(totm / 60)

s = tots % 60
m = totm % 60
h = toth % 24

print(h, m, s)
