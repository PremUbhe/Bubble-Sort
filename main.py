def buboole_sort(array):
    l = len(array)-1
    i = 0
    x = 0
    y = 1

    while i < l:
        i += 1

        if array[x] > array[y]:
            array[x], array[y] = array[y], array[x]   # swap
            x += 1
            y += 1
        else:
            x += 1
            y += 1


array1 = [1, 9, 4, 3, 1, 7, 10, 50, 12, 5]
buboole_sort(array1)
print(array1)
buboole_sort(array1)
print(array1)
buboole_sort(array1)
print(array1)
buboole_sort(array1)
print(array1)
buboole_sort(array1)
print(array1)
