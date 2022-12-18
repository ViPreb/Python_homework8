import view
import database
import phone_book

def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book()
        case 2:
            database.load_contacts()
        case 3:
            database.save_contacts()
        case 4:
            phone_book.add_contact()
        case 5:
            phone_book.change_contact()
        case 6:
            phone_book.remove_contact()
        case 7:
            phone_book.find_contact()
        case 0:
            return True


while True:
    choice = view.main_menu()
    if choice_menu(choice):
     break
