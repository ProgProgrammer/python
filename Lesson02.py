# coding utf-8

print ('Good afternoon, user!')
name = input ('What your name? ')
print (name,', welcome to work!')

answer = input ('Do you want to work? (Y/N)? ')

# PEP-8
if answer == 'Y':
	print ('You can use the calculator, or see brief recommendations for working with the Python language: PEP-8')
	program = input ('Enter the title: ')
	if program == 'calculator':
		print ('System error')
	elif program == 'PEP-8':
		print ('Этот документ описывает соглашение о том, как писать код для языка python.'
				'Этот документ создан на основе рекомендаций Гуидо ван Россума с добавлениями от Барри.'
				'Ключевая идея Гуидо такова: код читается намного больше раз, чем пишется. '
				'Собственно, рекомендации о стиле написания кода направлены на то,'
				'чтобы улучшить читабельность кода и сделать его согласованным между большим числом проектов.'
				'В идеале, весь код будет написан в едином стиле, и любой сможет легко его прочесть.')
	else:
		print ('You entered an invalid value.')
elif answer == 'N':
	print ('You are fired')
else:
	print ('Unknown answer.')
	
