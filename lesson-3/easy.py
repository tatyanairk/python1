# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    _ndigits = int(ndigits)
    st = pow(10, _ndigits)
    a =  number * st
    res = int(a)
    b = a - res
    if not (abs(b) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res / st
    
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    tcnum_list = str(ticket_number)
    if len(tcnum_list) != 6:
        return False
    first_digits = 0
    last_digits = 0
    for i in range(3):
        first_digits += int(tcnum_list[i])
        last_digits += int(tcnum_list[-i-1])
    if first_digits == last_digits:
         return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))