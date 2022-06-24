from AdressBook import *
from Notates import *








def main():
    contacts = reading_db(file_name)
    print('Выберите направление работы помощника: Notate - Введите(N) | AdressBook - Введите(A) ')
    branch = input('>>> ')
    if branch == 'A':
        while True:
            user_command = input('>>> ')
            command, data = command_parser(user_command)
            print(command(contacts, *data))
            if command is exiting:
                break
    elif branch == 'N':
        pass

    else:
        print('Нет доступной работы,выберите работу заново')


if __name__ == '__main__':
    main()