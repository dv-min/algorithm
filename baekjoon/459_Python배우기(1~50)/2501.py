input_data = input().split(" ")
n = int(input_data[0])
k = int(input_data[1])
result = []
for i in range(n):
    if n % (i + 1) == 0:
        result.append(i + 1)

result.sort()
if len(result) < k:
    print(0)
else:
    print(result[k - 1])
