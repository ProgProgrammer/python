# coding utf-8

import os
import psutil
import sys
import shutil

print ('Good afternoon, user!')
name = input ('What your name? ')
print (f'{name}, welcome to work!')

answer = ''

# PEP-8
while answer != 'q':
	answer = input ('Do you want to work? (Y/N)? Для выхода нажмите "q". ')
	if answer == 'Y':
		print ('Какую операцию Вы хотите совершить?')
		print ('Мой функционал:')
		print ('[1] - вывести список файлов')
		print ('[2] - вывести информацию о системе')
		print ('[3] - вывести список процессов')
		print ('[4] - продублировать файлы в текущей директории')
		print ('[5] - дублировать указанный файл')
		print ('[6] - удалить все фалы в текущей директории')
		print ('[7] - удаление выбранного файла')
		print ('[8] - удаление файлов с определенным окончаниями')
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
		elif do == 4:
			print ('Дублирование файлов в текущей директории.')
			ending = input ('Какое буквенное окончание вы хотели бы видеть в конце файла? ')
			if ending != '':
				file_list = os.listdir()
				i = 0
				while i < len (file_list):
					newfile = file_list[i] + '.' + ending
					shutil.copy (file_list[i], newfile)
					i += 1
				print ('Файл(ы) скопирован(ы).')
			else:
				print ('Окончание файла не введено.')
		elif do == 5:
			print ('Дублирование выбранного файла в текущей директории.')
			ending = input ('Какое буквенное окончание вы хотели бы видеть в конце файла? ')
			if ending != '':
				choice = int (input ('Вы хотите выбрать дублируемыйй файл по индексу или по имени? (индекс - 1; имя - 2)' ))
				if choice == 1:
					file_two = os.listdir()
					i = int (input ('Укажите индекс файла (начиная считать с верхней строки от числа 0 слева направо), который необходимо дублировать: '))
					if i != '':
						newfile = file_two[i] + '.' + ending
						shutil.copy (file_two[i], newfile)
						print ('Файл скопирован.')
					else:
						print ('Индекс файла не указан.')
				elif choice == 2:
					filename = input ('Укажите имя файла: ')
					if os.path.isfile (filename):
						newfile = filename + '.' + ending
						shutil.copy (filename, newfile)
						print ('Файл скопирован.')
					else:
						print ('Имя файла не указано.')
			else:
				print ('Окончание файла не введено.')
		elif do == 6:
			choice = input ('Удаление всех файлов в текущей директории. Вы точно хотите удалить путь ко всем файлам в директории, включая исполняемый? (Y/N) ')
			if choice == 'Y':
				file_list = os.listdir()
				i = 0
				while i < len (file_list):
					os.remove (file_list[i])
					i += 1
					print ('Файл(ы) удален(ы).')
			elif choice == 'N':
				print ('Удаление отменено.')
			else:
				print ('Введено неизвестное значение.')
		elif do == 7:
			filename = input ('Укажите имя файла, который необходимо удалить: ')
			if os.path.isfile (filename):
				os.remove (filename)
				print ('Файл удален.')
			else:
				print ('Файл не найден.')
		elif do == 8:
			print ('Удаление файлов с определенным окончаниями.')
			ending = input ('Файл с каким окончанием вы хотели бы удалить? ')
			if ending != '':
				dirname = input ('Введите имя директории: ')
				file_list = os.listdir(dirname)
				i=0
				while i < len (file_list):
					fullname = os.path.join (dirname, file_list[i])
					if fullname.endswith ('.' + ending):
						os.remove (fullname)
						i += 1
					else:
						print ('Ошибка.')
			else:
				print ('Окончание не введено.')
	elif answer == 'N':
		print (name + ', you are fired.')
	else:
		print ('Unknown answer.')
	
