x = 50

def func():
    global x
    
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение х на ', x)
    
func()
print('x теперь равен', x)