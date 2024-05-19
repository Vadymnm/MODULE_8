a = 555
b = 'string'

def add_everything_up(a, b):
    print('Успешная оперaция,  результат = ',a+b)

b = 'string'
a = 'A12B3C'
print('a = ',a,' b =  ',b)
try:
    add_everything_up(a, b)
except TypeError:
    print('unsupported operand type(s) for +; строка: ', str(a)+str(b))

print()
a = 555.456
b = 'string'
print('a = ',a,' b =  ',b)
try:
    add_everything_up(a, b)
except TypeError:
    print('unsupported operand type(s) for +; строка: ', str(a)+str(b))

print()
a = 123.454
b = 8
print('a = ',a,' b =  ',b)
try:
    add_everything_up(123.454, 8)
#    add_everything_up(a, b)
except TypeError:
    print('unsupported operand type(s) for +; строка: ', str(a)+str(b))

print()
a = '123.454'
b = 8
print('a = ',a,' b =  ',b)
try:
    add_everything_up('123.454', 8)
#    add_everything_up(a, b)
except TypeError:
    print('unsupported operand type(s) for +; строка: ', str(a)+str(b))