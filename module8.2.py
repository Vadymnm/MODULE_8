class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def f3(a,b):
    print('   f3() called  ')
    summ = 25
    for i in range(a,b):
        try:
            res = round(summ / i, 2)
            print('i = ',i,'res = ',res)
        except ZeroDivisionError as exc:
            print("Перехват исключения  (try / except) in f3() -  Деление на ноль")
            print(f'Вот что пошло не так в f3()- {exc},- но программа  продолжает  работать')
    print('Программа  выполнена  до  конца')
    return res

def f4(a,b):
    print('   f4() called ')
    summ = 25
    for i in range(a,b):
        if i == 0:
            raise MyCustomException (" 'raise' interruption in f4() --  Деление на ноль -- 'Программа  остановлена!")
        res = round(summ / i, 2)
        print('i = ',i,'res = ',res)
    print('Программа  выполнена  до  конца')
    return res


f3(-5,6)
print('--------------------------------------------------')
#f4(-5,6)
#print('--------------------------------------------------')
try:
    result = f4(-5,6)
except MyCustomException(" 'TRY/EXCEPT' interruption  --  Деление на ноль -- 'Программа  остановлена!"):
    print(result)

