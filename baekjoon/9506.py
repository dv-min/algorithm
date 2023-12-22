rs = []
while 1:
    n = int(input())
    if n == -1:
        break
    else:
        s = str(n) + " ="
        c = 0
        for i in range(int((n / 2)) + 1):
            if i > 0:
                if n % i == 0:
                    #   print(i)
                    c += i
                    s += " " + str(i) + " +"

        if c == n:
            s = s[0 : len(s) - 1]
            rs.append(s)
        else:
            rs.append(str(n) + " is NOT perfect.")

for r in rs:
    print(r)
