import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data_file = open('./accelerometer_data_csv_form.txt', 'r') 



try:
	lines = data_file.read().splitlines()
	while '' in lines: lines.remove('')

	g_x = []
	g_y = []
	g_z = []

	a_x = []
	a_y = []
	a_z = []

	m_x = []
	m_y = []
	m_z = []

	pitch = []
	roll = []
	heading = []

	all_list = []
	name_list = ['g_x', 'g_y', 'g_z', 'a_x', 'a_y', 'a_z', 'm_x', 'm_y', 'm_z', 'pitch', 'roll', 'heading']
	all_list.extend((g_x, g_y, g_z, a_x, a_y, a_z, m_x, m_y, m_z, pitch, roll, heading))


	for line in lines:
		current_line_list = line.split(',')
		for val, array in zip(current_line_list, all_list):
			array.append(float(val))



	for lists, name in zip(all_list, name_list):
		pd.DataFrame(lists).plot(title=name)


		
	
finally:
	data_file.close()
