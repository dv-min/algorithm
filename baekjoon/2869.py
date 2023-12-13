input_data = input().split(" ")
a = int(input_data[0])
b = int(input_data[1])
v = int(input_data[2])

d = a - b
if (v - b) % d > 0:
    print(int(((v - b) / d)) + 1)
else:
    print(int((v - b) / d))
