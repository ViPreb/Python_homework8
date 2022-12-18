import view
import database

phone_book = []
person = list()

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list) -> list:
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)


def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт? {phone_book[id - 1][0]}? Введите y / n')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id - 1)

def change_contact():
    global phone_book
    new_id = view.input_change_id_contact()
    new_index = view.input_change_index_contact()
    new_item = view.input_change_item_contact()
    phone_book[new_id-1][new_index-1] = new_item


def find_contact():
    global phone_book
    global person
    new_find_item = view.input_find_item()
    # точное вхождение
    for index, person in enumerate(phone_book):
        if new_find_item in phone_book[index]:
            # print('Строка с позицией {}: {}\n'.format(index, person))
            print(f'Строка с позицией {index+1}: {phone_book[index]}')
        # else:
        #     print('Значение отсутствует')







