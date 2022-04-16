import pytest
import os
import data_proc
import split_data
#from asyncio import run

def test_file_exist():
	res = data_proc.read_data_from_file('exampl1.csv')
	assert(res) == -1

def test_file_root():
	res = data_proc.read_data_from_file('exampl.csv')
	assert(res) == 1

#def test_is_file_csv()
#	try:
		#run("./main.py")
#		assert(False)
#	except ValueError:
#		assert(True)

def test_one_coll():
	res = data_proc.read_data_from_file("example_one_coll.csv")
	assert(res) == 2

def test_data():
	data = data_proc.read_data_from_file("example_incorrect_data.csv")
	res = split_data.split_data(data, 5)
	assert(res) == 1


