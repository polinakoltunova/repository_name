n = 3571
a = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(str(i))
#print(a, len(a))
stroka = "".join(a)

x = 10 #Размер алфавита
m = 2 #Длина шаблона


def hash(chast_stroki, x, m):
    hash = 0
    for i in range(m):
        hash += (ord(chast_stroki[i]) - 48)* (x**(m-i-1))      # ord - целочисленный код символа;  48- ord('0');
                                                                # минус нужен чтобы найти индекс числа, т.е.
                                                                # (расстояние между символами)
        hash = hash % 101   # mod простое число (% 101) для уменьшения размера хэша (если бы хэш был огромным)
    return hash


# massiv_hash массив хэшей, соответствующий каждой позиции строки размером длины шаблона
massiv_hash = [hash(stroka[i:i + m], x, m) for i in range(len(stroka) - m)]


def rabin_karp(stroka, massiv_hash, shablon, x, m):
    p = 0
    hash_shablon = hash(shablon, x, m)
    for i in range(len(stroka) - m - 1):
        hash_stroka = massiv_hash[i]
        # проверка равенства хэшей:
        if hash_stroka == hash_shablon:
            stroka_srez = stroka[i:i + m]
            if shablon == stroka_srez: # наивное сравнение
                p += 1
    return p


kolvo_vxogdenyi = {}
for i in range(10, 100):
    kolvo_vxogdenyi[i] = rabin_karp(stroka, massiv_hash, str(i), x, m)

sorted_pairs = sorted(kolvo_vxogdenyi.values(), reverse=True)
kkk = sorted_pairs[0] #  переменная в ответе, отвечающее за то, сколько раз встречается шаблон
for i in kolvo_vxogdenyi:
    if kolvo_vxogdenyi[i] == kkk:
        ckok_ras_vstr = i
c = sorted_pairs.count(sorted_pairs[0])
print('(рабин-карп) количество наиболее часто встречающихся двузначных чисел:', c, ", а именно:")
print("шаблон который наиболее часто встречается:", kkk)
print("сколько раз встречается данный шаблон:", ckok_ras_vstr)








