tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input_data = list(map(int, (input().split())))
a, b = input_data
result = ""

while a > 0:
    result = tmp[a % b] + result
    a = int(a / b)

print(result)
