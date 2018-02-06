# coding utf-8

import os
import psutil
import sys
import shutil

print ('Good afternoon, user!')
name = input ('What your name? ')
print (f'{name}, welcome to work!')

answer = ''

def system_info ():
	print (f'Имя текущей рабочей директории: {os.getcwd()}')
	print (f'Платформа (ОС): {sys.platform}')
	print (f'Кодировка файловой системы: {sys.getfilesystemencoding()}')
	print (f'Имя (логин) текущего пользователя в системе: {os.getlogin()}')
	print (f'Количество ядер у CPU: {psutil.cpu_count()}')
	
def ending ():
	ending = input ('Какое буквенное окончание вы хотели бы видеть в конце файла? ')
	
	
def dublicate_file (filename):
	if os.path.isfile (filename):
		newfile = filename + '.' + ending
		shutil.copy (filename, newfile)
		if os.path.exists (newfile):
			print ('Файл ' + newfile + ' успешно скопирован.')
			return True
		else:
			print ('Ошибка копирования.')
			return False
			

	

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
		print ('[8] - вывести список файлов в выбранной директории')
		print ('[9] - удаление файлов с определенными окончаниями в выбранной директории')
		print ('[10] - удаление всех файлов в выбранной директории')
		do = int (input ("Укажите номер действия: "))
		if do == 1:
			print (f'Список файлов {os.listdir()}')
		elif do == 2:
			system_info ()
		elif do == 3:
			print (f'Список запущенных процесов: {psutil.pids()}')
		elif do == 4:
			print ('Дублирование файлов в текущей директории.')
			ending ()
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
			ending ()
			if ending != '':
				choice = int (input ('Вы хотите выбрать дублируемый файл по индексу или по имени? (индекс - 1; имя - 2): ' ))
				if choice == 1:
					file_two = os.listdir()
					i = int (input ('Укажите индекс файла, который необходимо дублировать (начинать считать с верхней строки от числа 0 слева направо): '))
					if i != '':
						count = dublicate_file (file_two [i])
						print ('Скопирован ' + count + ' файл')
				elif choice == 2:
					filename = input ('Укажите имя файла: ')
					count = dublicate_file (filename)
					print ('Скопирован ' + count + ' файл')
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
			print ('Удаление выбранного файла по имени.')
			filename = input ('Укажите имя файла, который необходимо удалить: ')
			if os.path.isfile (filename):
				os.remove (filename)
				print ('Файл удален.')
			else:
				print ('Файл не найден.')
		elif do == 8:
			print ('Вывод списка файлов в указанной директории.')
			dirname = input ('Введите имя директории (в конце строки укажите две "\\"): ')
			print (f'Список файлов: {os.listdir(dirname)}')
		elif do == 9:
			print ('Удаление файлов с определенным окончаниями в выбранной директории.')
			ending ()
			if ending != '':
				dirname = input ('Введите имя директории (в конце строки укажите две "\\"): ')
				file_list = os.listdir(dirname)
				doubl_count = 0
				for f in file_list:
					fullname = os.path.join (dirname, f)
					if fullname.endswith ('.' + ending):
						os.remove (fullname)
						if not os.path.exists (fullname):
							doubl_count += 1
							print ('Файлы ' + fullname + ' удалены.')
				return doubl_count
			else:
				print ('Окончание не введено.')
		elif do == 10:
			choice = input ('Удаление всех файлов в выбранной директории, включая исполняемый. ВЫ точно желаете удалить путь ко всем файлам? (Y/N)')
			if choice == 'Y':
				dirname = input ('Введите имя директории (в конце строки укажите две "\\"): ')
				file_list = os.listdir(dirname)
				for f in file_list:
					fullname = os.path.join (dirname, f)
					os.remove (fullname)
				print ('Удалено ' + fullname + ' файлов.')
			elif choice == 'N':
				print ('Удаление отменено.')
			else:
				print ('Выбор не сделан.')
	elif answer == 'N':
		print (name + ', you are fired.')
	elif answer == 'q':
		print ('Спасибо за использование программы "Робот-помощник".')
	else:
		print ('Unknown answer.')
	
