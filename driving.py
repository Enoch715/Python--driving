country = input('請輸入你的國家: ')
age = int (input('請輸入你的年齡: '))
if country == '台灣' or '臺灣':
	if age < 18:
		print('您還不能考駕照')
	elif age >= 18:
		print ('恭喜! 您可以考駕照')