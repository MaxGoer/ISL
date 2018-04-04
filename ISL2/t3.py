rus_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyph_str = 'ШФСВРФ ЙЩЦВЕ ИФСФЗЁ ХФРЩХЁКШ З ЙФМЙВ ЙЦФЗЁ'
ofs = -6 # Сдвиг вправо, поэтому сдвигаем влево

trantab = str.maketrans(rus_abc, rus_abc[ofs:] + rus_abc[:ofs])
print(cyph_str.lower().translate(trantab))

