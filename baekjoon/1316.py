word = list(input())

chk = []
totCnt = 0
for i in range(len(word)):
    if i == 0:
        chk.append(word[i])
    elif i > 0:
        if word[i] == word[i - 1]:
            chk.append(word[i])
        else:
            print(word[i], chk)
            if word[i] in chk:
                if i == len(word) - 1:
                    totCnt = totCnt + 1
print(chk)

print(totCnt)
