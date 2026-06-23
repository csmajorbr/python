def duplica(f):
    f()
    f()

def quadriplica(f):
    duplica(f)
    duplica(f)

def linha_horizontal():
    print('+', end = '')
    print(' -' * 4, end = ' ')

def linha_horizontal_completa():
    duplica(linha_horizontal)
    print('+')

def linha_vertical():
    print('|', end = '')
    print(' ' * 9, end = '')

def linha_vertical_completa():
    duplica(linha_vertical)
    print('|')

def desenho_superior_completo():
    linha_horizontal_completa()
    quadriplica(linha_vertical_completa)

duplica(desenho_superior_completo)
linha_horizontal_completa()
