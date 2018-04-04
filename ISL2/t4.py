from itertools import *

rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyph_str = 'ЙХРК Г УЦИЭЩЕВ ЧР Г ХКЕДИГ'
cyph_key = '54524'

res = ''
for l in zip(''.join(cyph_str.split(' ')), cycle(cyph_key)):
	try:
		# print('Letter: {} | ABC index: {:2} | New_index: {:2} | New letter: {}'.format(l[0], rus_abc.index(l[0].lower()), rus_abc.index(l[0].lower()) - int(l[1]), rus_abc[(rus_abc.index(l[0].lower()) - int(l[1])) % len(rus_abc)]))
		res += rus_abc[(rus_abc.index(l[0].lower()) - int(l[1])) % len(rus_abc)]
	except:
		res += ' '

print(res)

