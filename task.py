1
first_num = 9 
second_num = 7
my_str = "start"
print(first_num, second_num, my_str)
     
first_num = 5.2
print(first_num, type(first_num))
var= third_num = first_num + second_num
print(third_num)

first_num += 5
second_num += first_num 
print(first_num, second_num)

second_num = 10
print(first_num, second_num) 

print(my_str) 
my_str *= 5
print(my_str) 

num_1 = 7
num_2 = 10
num_3 = 4
summ = num_1 + num_2 + num_3
print(f"Сумма всех целых чисел: {summ}")
num_1 = 7.9
num_2 = 21.3
num_3 = float(num_3)
summ = num_1 + num_2 + num_3
print(f"Сумма всех нецелых чисел: {summ}")
num_1 = 130
num_2 = 4
num_3 = 2
multiplying = num_1 * num_2 * num_3
print(f"Умножение всех чисел: {multiplying})
division = (num_1 / num_2) / num_3
print(f"Деление: {division})
num_1 = 2
num_2 = 3
num_3 = 4
degree = num_1  ** (num_2 ** num_3) 
print(f"Числа в степени: {degree})
math = ((43 + num_1) + (num_2 + 67) - (num_3 * 2)) // 2
print(math)


2
print("Задание 1")
print("Программа для перевода байт в биты")
переменная_1 = int(input("Введите количество байт:"))
пременная_2 = переменная_1 * 8 
print(f"{переменная_1} байт ровно {пременная_2} бит.")

s = 500 
c = 60 
n = 80
print(f"Электронная книга по прогроммированию на английском языке состоит из S страниц")
print(f"В среднем на странице {c} строк по {n} символов.")
print('Используется кодировка UTF-8. Определите объём текстового файла в Кбайтах.\n')
print("Расчет (шаг 4)")
r1 = s * c * n 
print(f"Всего символов (и байт) в книге: {s} * {c} * {n} = {r1}")
r2 = r1 / 1024 
print(f"Объём в Кбайтах: {r1} байт / 1024 = {r2:.2f} Кбайт\n")
print("Вывод решения (шаг 5)")
print(f"{s} * {c} * {n} = {r1} - Всего символов (байт) в книге.")
print(f"Итоговый объём текстовый файла: {r2.2f} Кбайт.")


3
minutes = int(input("Введите количество минут:"))
hours = minutes // 60
remaining_minutse = minutes % 60
print(hours)
print(remaining_minutse)

a = int(input("Рекомендуемый минимум часов сна (a):"))
b = int(input("Рекомендуемый минимум часов сна (b):"))
h = int(input("Сколько часов спит Аня сейчас (h):"))
if h < a: 
    print("Недосып")
elif h > b: 
    print("Пересып")
else: 
    print("Это нормально")

import math 
figure_type = input("Введите тип фигуры (треугольник, прямоугольник, круг):").lower()
area = 0
if figure_type == "Треугольник":
    a = float(input("Длина основания:"))
    h = float(input("Высота:"))
    area = 0.5 * a * h 
elif figure_type == "Прямоугольник":
    a = float(input("Длина:"))
    b = float(input("Ширина:"))
    area = a * b 
elif figure_type == "Круг":
    r = float(input("Радиус:"))
    area = 3.14 * r ** 2 

else: 
    print("Неизвестный тип фигуры")

if area > 0: 
    print(f"Площадь {figure_type}a: {area:.2f}")

n = int(input("Введите количество программистов:"))
if n % 10 == 1 and n % 100 != 11:
    ending = ""
elif 2 <= n % 10 <= 4 and not ( 12 <= n % 100 <= 14):
    ending = "а"
else: 
    ending = "ов"
print(f"{n} программист {ending}")

n = int(input("Введите количество программистов:"))
if n % 10 == 1 and n % 100 != 11:
    ending = ""
elif 2 <= n % 10 <= 4 and not ( 12 <= n % 100 <= 14):
    ending = "а"
else: 
    ending = "ов"
print(f"{n} программист {ending}")

ticket = input(" Введите номер билета:")
if len(ticket)!=6 or not ticket.isdigit():
    print("Ошибка! Введите ровно 6 цифр")
else:
    digits = [int(digit) for digit in ticket]
    if sum(digits[:3]) == sum(digits[3:]):
        print("Счастливый")
    else: 
        print("Обычный")
