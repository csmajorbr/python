def do_twice(f, valor):
    f(valor)
    f(valor)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)
    
print(do_four(print_twice, 'spam'))