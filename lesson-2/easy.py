# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ['Груша', ' Дыня', 'Банан', 'Папайя', 'Манго', 'Апельсин']

for num, frut in enumerate(fruits):
    print(str(num) + '. {:>8}'.format(frut))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

femname = ["Лена", "Маша", "Саша", "Женя", "Катя"]
manname = ["Дима", "Женя", "Саша", "Андрей", "Миша"]

for fnm in femname[:]:
    for mnm in manname[:]:
        if mnm == fnm:
            femname.remove(mnm)
print("Женские имена: {}".format(femname))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

num  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_num = []

print(num)

for nm in reversed(num):
    count = num.index(nm)
    if (nm % 2) == 0:
         new_nm= nm / 4
         new_num.insert(0, new_nm)
         num.remove(nm)
    else:
         nm = nm * 2
         num[count] = nm

print(num)
print(new_num)
