"""
Кириллов Иван 22107
Проверка гипотизы Гольдбаха
"""
import ctypes

cal_primes = ctypes.CDLL('./calculate_primes.so') # загрузка библиотеки

# указывает, какие параметры приннимает функция
cal_primes.calculate_primes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ]

n, m = input().split() # считывает числа n и m
m = int(m) # приводит n, m к целочисленному типу
n = int(n) #
m += 1;

p = ctypes.c_int * m # создание тип массива из м элементов типа c_int
k = p() # создаем массив k
cal_primes.calculate_primes(k, m) # вызываем функцию для назождения 

count = 0 
first = 0
second = 0

# находим в интервале от n до m числа удовлетворяющие гипотизе Гольдбаха 
for i in range(n, m):
	if i % 2 == 0: # проверка: является ли число четным?
		for j in range(2, i):
			if k[j] == 1 and k[i - j] == 1 and j <= i - j: # проверка является ли число 
														   # j <= i - j, чтобы пары не повторялись
				if (count == 0):
					first = j
					second = i - j;
				count += 1
		if count > 0:
			print(i, count, first, second) # выводит число, колличество его разложений 
										   # на простые числа и одно из разложений, 
										   # в том случае если четное число удовлетворяет
										   # гипотизе Гольдбаха
	count = 0




