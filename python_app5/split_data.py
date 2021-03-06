def split_data(data, c):
	"""
	Разбивает данные из списка на подотрезки
	заданной длины. 
	На вход получает список и интервал разбиения
	"""
	splitData = [[]] # создание двумерного списка для хранения статистики,
	                 # разбитой на с-минутные подотрезки
	i = 0
	time = c

	for unit in data:
		try:
			float(unit[0])
			int(unit[1])
		except:
			return 1
		if float(unit[0]) <= time: # проверка входит ли элемент в данный подотрезок
			splitData[i].append(unit[1]) # добавление элемента во вложенный список
		else:
			if len(splitData[i]) != 0: # проверка есть ли элементы в данном подотрезке
				i += 1
				splitData.append([]) # добавление пустого вложенного списка
			splitData[i].append(unit[1]) # добавление первого элемента в список 
			time = float(unit[0]) + c # задание времени при достижени еоторого
			                          # запись в данный подотрезок прекращается
	return splitData