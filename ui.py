from model import get_info
from logger import writing_csv, read_contact, writing_txt

def click():
    print('1. Добавить новый контакт\n2. Вывести телефонную книгу')
    mode = int(input())
    if mode == 1:
        a = get_info()
        writing_txt(a)
        writing_csv(a)
    elif mode == 2:
        print(read_contact())
    else:
        print('Введено неверное значение!')