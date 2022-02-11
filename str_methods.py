name = 'Swaroop'

if name.startswith('Swa'):
    print('Да, строка начинаетсяна "Swa"')
    
if 'a' in name:
    print('Да, она содержит строку "a"')
    
if name.find('war') != -1:
    print('Да, она содержит строку "war"')
    
delimiter = '_*_'

mylist = ['a', 'b', 'c']
print(delimiter.join(mylist))