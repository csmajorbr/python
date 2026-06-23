def duplicar(f):
    f()
    f()

def quadruplicar(f):
    duplicar(f)
    duplicar(f)

def linha_horizontal():
    print('+', end = '')
    print(' -' * 4, end = ' ')

def linha_horizontal_completa():
    quadruplicar(linha_horizontal)
    print('+')

def linha_vertical():
    print('|', end = '')
    print(' ' * 9, end = '')

def linha_vertical_completa():
    quadruplicar(linha_vertical)
    print('|')

def parte_superior_desenho():
    linha_horizontal_completa()
    quadruplicar(linha_vertical_completa)

quadruplicar(parte_superior_desenho)
linha_horizontal_completa()