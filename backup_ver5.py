import os
import time
import zipfile

#Файлы и каталоги, которые необходимо скопировать, собираются в список:
source = 'C:\GIT\A-Byte-of-Python'
#Место расположения резервных копий
target_dir = "C:\Backup"
#Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%d%m%Y')
#Текущее время служит именем архива
now = time.strftime('%H%M%S')

#Запросим комментарий пользователя
comment = input('Введите комментарий: ')
if len(comment) == 0: #Проверяем, введен ли комментарий
    #Имя архива
    target = today + os.sep + now + '.rar'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.rar'

#Создаем каталог, если его нет
if not os.path.exists(today):
    os.mkdir(today) #создание каталога
    print('Каталог успешно создан', today)
 
#Запускаем создание резервной копии   
file_dir = os.listdir(source)

with zipfile.ZipFile(target, mode = 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(source, file)
        zf.write(add_file)

if os.system(add_file) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')