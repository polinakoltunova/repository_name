n = 3571
a = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(str(i))
# print(a, len(a))
text = "".join(a)
# print(text)


def boier_myr(text, shablon):
    k = 0 # количество повторений шаблона в тексте
    len_shab = len(shablon)
    len_text = len(text)
    dict_sdvigov = {}

    for i in range(0, len_shab - 1):
        dict_sdvigov[shablon[i]] = len_shab - 1 - i                                   # словарь сдвигов нужен чтобы знать какой сдвиг соответствует каждой букве чтобы потом в зависимости от стоп символа определять насколько нужно осуществлять сдвиг
    print(" dict",dict_sdvigov)

    i = 0 # индекс в тексте
    j = 0 # индекс в шаблоне

    while i <= len_text - len_shab:
        j = len_shab - 1                                                          # на последнем месте в шаблоне и дальше двигаем его влево
        while j >= 0 and shablon[j] == text[i + j]:                               # text[i+j] это стоп символ
            j -= 1

        if j < 0:                                                                  #  если значения шаблона и текста совпали
            k += 1
            i += 1
        else:
            i += dict_sdvigov.get(text[i + j], len_shab)                           # если в таблице сдвигов не найден сдвиг то сдвинуться на длину шаблона
    return k


kolvo_vxogdenyi = {}
for i in range(10, 100):
    kolvo_vxogdenyi[i] = boier_myr(text, str(i))
print("a", kolvo_vxogdenyi)

sorted_pairs = sorted(kolvo_vxogdenyi.values(), reverse=True)
c = sorted_pairs.count(sorted_pairs[0])

print('(наивный) количество наиболее часто встречающихся двузначных чисел: ', c)



print('-----------------')

strokaaaa = 'этонетот'
shablonchik = 'тот'
b = boier_myr(strokaaaa, shablonchik)
print(b)




