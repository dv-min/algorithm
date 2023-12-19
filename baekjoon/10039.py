hap = 0
for i in range(5):
    a = int(input())
    hap += a if a > 40 else 40
print(int(hap / 5))
