input_data = int(input())
a = 0
cnt = 1

while input_data > 1:
    # print(input_data)
    input_data = input_data - 6 * cnt
    cnt = cnt + 1

print(cnt)
