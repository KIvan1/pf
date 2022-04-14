import csv
import os
import statistics

def read_data_from_file(file):
	"""
	Считывает данные из файла
	и возвращает их в виде списка.
	На вход получает имя файла 
	"""
	data = [] # создание список для хранения данных из файла
	if (os.access(file, os.F_OK) == False):
		return -1
	if (os.path.splitext(file) != '.csv'):
		print(os.path.splitext(file))
		return 2
	if (os.access(file, os.R_OK)):
		with open(file, newline = '') as csvfile: # открытие csv файла
			dataReader = csv.reader(csvfile, delimiter = ',') # создание объекта для 
			print(dataReader)											  # построчной итерации по файлу
			for row in dataReader:
				data.append(row) # помещение данных в список
			data.pop(0) # первый элеиент - название столбцов,
		            # удаляем его
	else: 
		return 1
	return data

def calculate_statistic(splitData):
	"""
	Вычисляет количество значений,
	среднее значение, моду и медиану
	для всех подотрезков.
	На вход получает список подотрезков.  
	"""
	dataStat = [] # создание списка для хранения статистики
	for unit in splitData:
		dataStat.append({'length': len(unit), 
			'mean': statistics.mean(float(i) for i in unit),
			'mode': statistics.mode(unit),
			'median': statistics.median(float(i) for i in unit)}) # вычисление статистики
		   														  # и помещение ее в список
	return dataStat

def stat_print(data):
	"""
	Выводит статистику для данного отрезка.
	На вход получает словарь, содержащий статистику. 
	"""
	for unit in data:
		print(unit,'\t' , data[unit])