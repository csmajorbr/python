def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_4xs(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

print(do_4xs(print, "Snugglebunnies"))
