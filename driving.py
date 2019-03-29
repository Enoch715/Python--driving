while True:
	country = input('請輸入你的國家: ')
	if country == '台灣' or country == '臺灣':
		age = int(input('請輸入你的年齡: '))
		if age >= 18:
			print('恭喜! 您可以考駕照')
			break
		else:
			print('您還不能考駕照')
			break
	elif country == '美國':
		age = int(input('請輸入你的年齡: '))
		if age >= 16:
			print('恭喜! 您可以考駕照')
			break
		else:
			print('您還不能考駕照')
			break
	else:
		print('國家只能輸入 台灣/美國')
