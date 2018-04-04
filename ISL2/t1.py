cyph_str = 'ГРМРЛ ЬИОДА В,О-Р ВЕ-ЕГ ДТАОД ТТДЫА ЗРЫАЕ ЕРМГЫ'
d = lambda c: ''.join([''.join(''.join(c)[s::len(c)]) for s in range(len(c))])
print(d(cyph_str.split(' ')))
