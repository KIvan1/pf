import pytest
import os
import data_proc

def test_file_exist():
	res = data_proc.read_data_from_file('exampl1.csv')
	assert(res) == -1

def test_file_root():
	res = data_proc.read_data_from_file('exampl.csv')
	assert(res) == 1

def test_is_file_csv()
	res = data_proc.read_data_from_file('test.txt')
	assert(res) == 2


