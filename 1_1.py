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
print(st)

c = []
for i in range(10, 100):
    c += [[i, 0]]
print(c)
for i in range(90):
    for j in range(len(st) - 1):
        if str(c[i][0])[0] == st[j] and str(c[i][0])[1] == st[j + 1]:
            #print(i, j, c[i])
            c[i][1] += 1
print(c)

maxx = 0
k = 0
shab = ''
for i in range(len(c)):
    if maxx < c[i][1]:
        maxx = c[i][1]
        k = c[i][0]
        shab = c[i][1]
print(k, shab)




#--------------------------------------------------------------------------------------------
"""
def naiv(text, shablon):
    n = 0
    len_shab = len(shablon)
    for i in range(len(text) - len_shab + 1):
        text_srez = text[i:i + len_shab]
        if text_srez == shablon:
            n += 1
    return n


def result(stroka):
    kolvo_vxogdenyi = {}
    for i in range(10, 100):
        kolvo_vxogdenyi[i] = naiv(stroka, str(i))
    sorted_pairs = sorted(kolvo_vxogdenyi.values(), reverse=True)
    c = sorted_pairs.count(sorted_pairs[0])
    return print('(наивный) количество наиболее часто встречающихся двузначных чисел: ', c)


result(stroka)
"""