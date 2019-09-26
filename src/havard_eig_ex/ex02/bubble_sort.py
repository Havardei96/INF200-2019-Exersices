def bubble_sort(dataa):
    data_list = list(dataa)
    for i in range(len(data_list) - 1, 0, -1):
        for j in range(i):
            if data_list[j] > data_list[j + 1]:
                replace_temp = data_list[j]
                data_list[j] = data_list[j + 1]
                data_list[j + 1] = replace_temp
    return data_list


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
