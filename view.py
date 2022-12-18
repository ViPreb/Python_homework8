import  phone_book as pb
def main_menu():
    print('Выберите команду меню: ')
    print('1. Показать телефонную книгу: ')
    print('2. Загрузить телефонную книгу: ')
    print('3. Сохранить телефонную книгу: ')
    print('4. Добавить контакт: ')
    print('5. Изменить контакт: ')
    print('6. Удалить контакт: ')
    print('7. Найти контакт: ')
    print('0. Выйти из приложения\n')
    return input_menu()


def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: \n'))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('Такого пункта нет\n')
        except:
            print('Ошибка ввода. Введите корректный пункт меню\n') # если ввели что-то, кроме цифры


def print_phone_book():
    phone_book = pb.get_phone_book()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена\n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
        print()

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: \n')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите id контакта для удаления: '))
    return id


def input_change_id_contact():
    global phone_book
    print()
    print_phone_book()
    id = int(input('Введите id строки, которую хотите изменить: '))
    return id

def input_change_index_contact():
    global phone_book
    index = int(input('Введите номер поля, которое хотите изменить (1- имя, 2 - телефон, 3 - комментарий): '))
    return index

def input_change_item_contact():
    global phone_book
    new_item = input('Введите изменение: ')
    return new_item

def input_find_item():
    global phone_book
    print()
    print_phone_book()
    find_item = input('Введите точное значение имени или телефона или комментария: ')
    return find_item