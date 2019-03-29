country = input('請輸入你的國家: ')
age = input('請輸入你的年齡: ')
age = int(age)

if country == '台灣' or country == '臺灣':
	if age >= 18:
		print('恭喜! 您可以考駕照')
	else:
		print('您還不能考駕照')

elif country == '美國':
	if age >= 16:
		print('恭喜! 您可以考駕照')
	else:
		print('您還不能考駕照')

else:
	print('國家只能輸入台灣或美國')