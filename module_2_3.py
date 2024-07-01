my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0  # переменная для индекса списка
while start < len(my_list):
    if my_list[start] < 0:  # завершаем вывод если элемент меньше нуля
        break
    elif my_list[start] == 0:  # пропускаем элемент, если равен нулю
        start = start + 1
        continue
    else:
        print(my_list[start])
    start = start + 1
