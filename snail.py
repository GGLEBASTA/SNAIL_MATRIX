def snail(snail_map):
    """Функция обрабатывающая матрицу 3-столбцов * N-строк улиткой по часовой стрелке выводя значения"""
    """!!Важно отметить: количество столбцов,допустимое в матрице для ввода,только равное 3!!"""
    dl_in = len(snail_map[0]) #длина строки в матрице
    dl = len(snail_map) #количество строк в матрице
    i = 0
    list_el = [] #итоговый список чисел для вывода
    #первая строка
    for x in snail_map[0]:
        list_el.append(x)
    #правый борт
    while i < dl-2:
        i+=1
        list_el.append(snail_map[i][-1])
    #последняя строка
    reverse_ = snail_map[-1]
    reverse_.reverse()
    for x in reverse_:
        list_el.append(x)
    #левый борт
    while i <= dl-2:
        list_el.append(snail_map[i][0])
        i -= 1
        if(i==0):
            break
    #внутрянка
    z = 0
    i = 1
    while i <= dl-2:
        while z < dl_in-2:
            z+=1
            list_el.append(snail_map[i][z])
        z = 0
        i+= 1

    return list_el


array = [[1,2,3],
         [8,9,4],
         [7,6,5],
         [10,11,12],
         [13,14,15],
         [16,17,18]]
m = snail(array)
print(m)