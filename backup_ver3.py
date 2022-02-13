import os
import time

#Файлы и каталоги, которые необходимо скопировать, собираются в список:
source = ['F:\GIT\A-Byte-of-Python']
#Место расположения резервных копий
target_dir = "F:\Backup"
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
zip_command = "rar a {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')