# coding utf-8

import os
import psutil
import sys

print ('Good afternoon, user!')
name = input ('What your name? ')
print (f'{name}, welcome to work!')

answer = input ('Do you want to work? (Y/N)? ')

# PEP-8
if answer == 'Y':
	print ('Какую операцию Вы хотите совершить?')
	print ('Мой функционал:')
	print ('[1] - вывести список файлов')
	print ('[2] - вывести информацию о системе')
	print ('[3] - выведу список процессов')
	do = int (input ("Укажите номер действия: "))
	if do == 1:
		print (f'Список файлов {os.listdir()}')
	elif do == 2:
		print (f'Имя текущей рабочей директории: {os.getcwd()}')
		print (f'Платформа (ОС): {sys.platform}')
		print (f'Кодировка файловой системы: {sys.getfilesystemencoding()}')
		print (f'Имя (логин) текущего пользователя в системе: {os.getlogin()}')
		print (f'Количество ядер у CPU: {psutil.cpu_count()}')
	elif do == 3:
		print (f'Список запущенных процесов: {psutil.pids()}')
	else:
		print ('You entered an invalid value.')
elif answer == 'N':
	print ('You are fired')
else:
	print ('Unknown answer.')
	
