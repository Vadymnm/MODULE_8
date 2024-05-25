class InvalidData(Exception):
    pass
def f1(person_name):
    print('  f1() called ')
    try:
        for name in person_name:
            if name == 'Robert':
                print("=== f1(): - We don't like you,  'Robert';   Your name is not allowed ! ===")
                raise InvalidData("Raise in f1() - We don't like you, the name is not allowed:  Robert")
            else:
                print(f'Hi there  is - {name}')
    except InvalidData  as exc:
        print(f'Обнаружено недопустимое имя "Robert" в f1(), {exc},- программа  прервана')
        print( '--Invalid  Data --')

def f2(person_name):
    print('  f2() called ')
    for name in person_name:
        if name == 'Robert':
            print("=== We don't like you,  'Robert',   the name is not allowed  ===")
            raise InvalidData("Raise in f2() - We don't like you, the name is not allowed:  Robert")
        print(f'Hi there {name}')

def greet_person(person_name):
    print('--------------------------------------')
    f1(person_name)
    print('--------------------------------------')
    f2(person_name)
    print('--------------------------------------')


names = ['Sasha', 'Dolly', 'Vasya', 'Robert', 'Nick', 'Masha']
#names = ['Sasha', 'Dolly', 'Vasya',  'Nick', 'Masha']
greet_person(names)