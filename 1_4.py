n = 3571
a = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
# print(a, len(a))
st = ""
for i in range(500):
    st += str(a[i])
#print(st)

c = []
for i in range(10, 100):
    c += [[i, 0]]
#print(c)





for k in range(90):
    t = str(c[k][0])
    p = [0] * len(t)
    #print(p)
    j = 0
    i = 1
    while i < len(t):
        if t[j] == t[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    #print(c[k][0], p)
    i = 0
    j = 0
    while i < len(st):
        if st[i] == t[j]:
            i += 1
            j += 1
            if j == len(str(c[k][0])):
                c[k][1] += 1
                j = 0
                i -= 1
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
print(c)

maxx = 0
k = 0
for i in range(len(c)):
    if maxx < c[i][1]:
        maxx = c[i][1]
        k = c[i][0]
print(k)

