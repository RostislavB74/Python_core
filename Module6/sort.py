# python sort.py \\DESKTOP-6G8HACK\Users\Rost\Desktop\Мотлох
# Для того щоб успішно впоратися з цим завданням, ви повинні винести логіку обробки папки в окрему функцію.
# Щоб скрипт міг пройти на будь-яку глибину вкладеності, функція обробки папок повинна рекурсивно викликати сама себе, коли їй зустрічаються вкладенні папки.
# Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли за групами:

# зображення ('JPEG', 'PNG', 'JPG', 'SVG');
# відео файли ('AVI', 'MP4', 'MOV', 'MKV');
# документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
# музика ('MP3', 'OGG', 'WAV', 'AMR');
# архіви ('ZIP', 'GZ', 'TAR');
# невідомі розширення.
# Ви можете розширити та доповнити цей список, якщо хочете.

# В результатах роботи повинні бути:

# Список файлів в кожній категорії (музика, відео, фото та ін.)
# Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
# Перелік всіх розширень, які скрипту невідомі.
# Потім необхідно додати функції, які будуть відповідати за обробку кожного типу файлів.

# Крім того, всі файли та папки потрібно перейменувати, видаливши із назви всі символи, що призводять до проблем. Для цього потрібно застосувати до імен файлів функцію normalize. Варто розуміти, що перейменувати файли потрібно так, щоб не змінити розширення файлів.

# Функція normalize:

# Здійснює транслітерацію кириличного алфавіту на латинський.
# Замінює всі символи крім латинських літер, цифр на '_'.
# Вимоги до функції normalize:

# приймає на вхід рядок та повертає рядок;
# здійснює транслітерацію кириличних символів на латиницю;
# замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
# транслітерація може не відповідати стандарту, але бути читабельною;
# великі літери залишаються великими, а маленькі — маленькими після транслітерації.
# Умови для обробки:
# зображення переносимо до папки images
# документи переносимо до папки documents
# аудіо файли переносимо до audio
# відео файли до video
# архіви розпаковуються та їх вміст переноситься до папки archives
# Критерії приймання завдання
# всі файли та папки перейменовуються за допомогою функції normalize.
# розширення файлів не змінюється після перейменування.
# порожні папки видаляються
# скрипт ігнорує папки archives, video, audio, documents, images;
# розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів, але без розширення в кінці;
# файли, розширення яких невідомі, залишаються без зміни.
#d:/Users/Rost/Documents/GitHub/module-6/sort.py C:/Users/Rost/Desktop/Мотлох/
import os
import shutil

main_path = 'C:\\Users\\Rost\\Desktop\\Мотлох\\'
# key names will be folder names!
extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv', 'mpeg'],
    
    'audio': ['mp3', 'wav', 'ogg', 'amr', 'cda'],

    'image': ['jpg', 'png', 'jpeg', 'svg'],

    'archives': ['zip', 'rar', 'gz'],

    'documents': ['pdf', 'xlsx', 'xls', 'txt', 'doc', 'docx', 'rtf', 'pptx','ppt'],
    }
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "h", "d", "e", "e", "zh", "z", "y", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "iu", "ia", "ie", "i", "i", "g")

#def normalize(name):
# for dirpath, dirnames, filenames in os.walk(main_path):
#     for filename in filenames:
#         print(os.path.abspath(filename))

# from pathlib import Path

# print(next(Path(main_path).rglob(findThis)))

# last_dir = ''
# dir = main_path
# os.chdir(dir)
# while last_dir != dir:
#     dir = os.getcwd()
#     print(glob.glob('*.xls'))
#     os.chdir('..')
#     last_dir = os.getcwd()   
import os
list_files=[]
for root, dirs, files in os.walk("."):  
    print(f'root = {root}, dirs= {dirs}')
    for filename in files:
        list_files.append(filename)
    
for keys in extensions:
    os.makedirs(keys, mode=0o777, exist_ok=False)


# def walk(path, prev_list_dir):
#     print(prev_list_dir)
#     print (os.getcwd())
#     os.chdir(path)
    
#     list_dir = list (filter(os.path.isdir, os.listdir()))

#     for el in list_dir:
#         list_dir.remove(el)
#         return walk(fr'{path}\{el}', list_dir)
    
# walk(main_path, [])