cyph_str = 'ДТГАЕ ЕУЕНД ЩЧШБЕ ЕААИЕ ОНЮЮВ НБЕ.,'
cyph_key = 'БЕРЛИН'
abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


cs_str = ''.join(cyph_str.split(' ')) # no whitespaces
reshaped = list(map(''.join, zip(*[iter(cs_str)]*len(cyph_key))))
parts = [''.join(st) for st in list(zip(*reshaped))]


def sort_by(abc, s):
	return sorted([abc[abc.index(l)] for l in s])

res = ''
for l in cyph_key:
	res += parts[sort_by(abc, cyph_key).index(l)]

	
print(res)


