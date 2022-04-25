#  Работа с файлами

# Указатель
# Hello world


# open( <путь до вашего файла)

#file = open(text txt) Относительный путь


# Режимы для работы с файлами
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)
# t b + x 


# file = open('text.txt', 'r')
# data  = file.read()
# data = data.split('\n')
# print(data)
# file.close()


# file = open('text.txt', 'r')
# data = file.readlines()
# print(data)
# file.close()

#Контекстыный менедженр

# with open('text.txt') as file:
#     data = file.read()
#     print(data)

# print(file.read()) -oshibka

# with open('text1.txt', 'w') as file:
#     file.write('Hello, file was opened with')

# write
# writelines

# ls = ['aaaaaa', 'aaaav', 'vvvvvbbbb']
# with open('text.txt', 'w') as file:
#     file.writelines(line + '\n' for line in ls)

# with open('~/Desktop/Makers/Makers19/types/text.txt', 
# 'a') as file:
#     file.write('New string')

#file.tell()   Возвращает индекс где находится указ

#file.seek(int)  Перемещает указатель на указанный int

#---------------------------------------------

# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract
# import re


# def get_imei_code(image):
#     list_of_imei = []
#     for x in image:
#     string1 = pytesseract.image_to_string
#     (x)
#     list_of_imei.append(re.findall(
#     r'ME.\d. \s\d+', string1
#     ))
    
# with open('imeicode.txt', 'w') as file:
#     for x in list_of_imei[0]:
#         file.writhe(x)  

# get_imei_code(['/home/marat/Desktop/Makers/Makers19/types/files/imei.jpg'])


age = int(input())
if age <=2:
    print(str(age*5.25))
elif age>2:
    print(str(10.5+age*4))
else:
    print()        

