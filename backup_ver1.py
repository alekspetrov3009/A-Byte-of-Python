import os
import time

source = ['F:\GIT\A-Byte-of-Python']
target_dir = "F:\Backup"
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.rar'
zip_command = "rar a {0} {1}".format(target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')