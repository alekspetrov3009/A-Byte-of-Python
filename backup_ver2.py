import os
import time

source = ['F:\GIT\A-Byte-of-Python']
target_dir = "F:\Backup"
today = target_dir + os.sep + time.strftime('%d%m%Y')
now = time.strftime('%H%M%S')

#Создаем каталог, если его нет
if not os.path.exists(today):
    os.mkdir(today) #создание каталога
    print('Каталог успешно создан', today)
    
#Имя архива
target = today + os.sep + now + '.rar'
    
zip_command = "rar a {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')