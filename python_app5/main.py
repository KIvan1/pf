"""
Кириллов Иван, 2 лабароторная 
Обработка данных из csv файла
"""
import data_proc
import split_data
import sys

if len(sys.argv) < 3: # прверка достаточно ли аргументов 
					  # переданно в командной строке 
	print('Not enough arguments')
else:
    data = data_proc.read_data_from_file(sys.argv[1])
    splitData = split_data.split_data(data, int(sys.argv[2]))
    dataStat = data_proc.calculate_statistic(splitData)
    for unit in dataStat: # цикл для вывода статистики
	    print('Section begin.')
	    data_proc.stat_print(unit)
	    print('Section end.\n')