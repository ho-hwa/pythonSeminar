#simple.py

languages = ['Java', 'C', 'perl', 'Python']

for lang in languages:
	if lang in ['Python','perl']:
		print("%6s need interpreter" %lang)

	elif lang in ['C','Java']:
		print("%6s need complier" %lang)
	else:
		print("should not reach here")

