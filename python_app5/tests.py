import pytest
import os
import data_proc
import split_data
import random
import statistics

def test_file_exist():
	res = data_proc.read_data_from_file('exampl1.csv')
	assert(res) == -1

def test_file_root():
	res = data_proc.read_data_from_file('example_root.csv')
	assert(res) == 1

def test_is_file_csv():
	res = data_proc.read_data_from_file("example.jpg");
	assert(res) == 2

def test_one_coll():
	res = data_proc.read_data_from_file("example_one_coll.csv")
	assert(res) == 2

def test_data():
	data = data_proc.read_data_from_file("example_incorrect_data.csv")
	res = split_data.split_data(data, 5)
	assert(res) == 1

def test_split():
	random.seed()
	data = data_proc.read_data_from_file("example.csv")
	m = float(data[len(data) - 1][0]) - float(data[0][0])
	m = int(m)
	sp = random.randint(1, m)
	res = split_data.split_data(data, sp)
	k = 0
	for i in res:
		assert(float(data[k][0]) - float(data[k + len(i) - 1][0])) < sp 
		k += len(i) 

def test_count():
	data = data_proc.read_data_from_file("example.csv")
	m = float(data[len(data) - 1][0]) - float(data[0][0])
	m = int(m)
	sp = random.randint(1, m)
	res = split_data.split_data(data, sp)
	i = 1
	k = True
	time = sp
	for unit in data:
		if float(unit[0]) <= time: 
			continue
		else:
			if k: 
				i += 1
				k = False
			k = True 
			time = float(unit[0]) + sp
	assert(len(res)) == i

def test_stat():
	data = data_proc.read_data_from_file("example.csv")
	m = float(data[len(data) - 1][0]) - float(data[0][0])
	m = int(m)
	sp = random.randint(1, m)
	res = split_data.split_data(data, sp)
	sp_res = data_proc.calculate_statistic(res)
	k = 0
	for unit in res:
		assert(len(unit)) == sp_res[k]['length'] 
		assert(statistics.mean(float(i) for i in unit)) == sp_res[k]['mean']
		assert(statistics.mode(unit)) == sp_res[k]['mode']
		assert(statistics.median(float(i) for i in unit)) == sp_res [k]['median']
		k += 1 