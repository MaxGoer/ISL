from itertools import *


abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_'
cyph_str = 'ЗОМДБШЕ_УЬЁУВЁКШПЙЙОЖЯНФЬБЛДШФЩГЙЫЬКЫМЧУЛ_КИКВТД'
cyph_key = 'ЗАЕЗД'

res = ''
for l in zip(cyph_str, cycle(cyph_key)):
	try:
		ofs = abc.index(l[1])
		ofs_abc = abc[-ofs:] + abc[:-ofs]
		res += abc[ofs_abc.index(l[0])]
	except:
		pass

	
print(res)
