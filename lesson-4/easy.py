# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

 import random
 lst = []
 new_lst = []

for _ in range(5):
	lst.append(random.randint(1, 20))

print(lst)

for dig in lst:
	new_lst.append(int(dig**2))

print(new_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# я не поняла, как здесь через генератор сделать

fruits1 = ["Orange", "Muskmelon", "Mango", "Lemon", "Banana"]
fruits2 = ["Mango", "Apple", "Watermelon", "Lemon"]
fruits = []

for fr1 in fruits1:
	for fr2 in fruits2:
		if fr1 == fr2: fruits.append(fr1)

print(fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random 
lst = []
new_lst = []

for _ in range(10):
	lst.append(random.randint(1, 100))

print(lst)

for dig in lst:
	if dig % 3 == 0 and dig % 4 != 0 and dig > 0:
		new_lst.append(dig)

print(new_lst)






