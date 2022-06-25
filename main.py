from AdressBook import *
from Notates import *








def main():
    contacts = reading_db(file_name)
    while True:
        branch = input('Выберите одну из предложеных команд: '
              '\nNotate - Введите(N) | AdressBook - Введите(A)\n'
              'Для завершения работы помощника ведите (X)\n>>>')

        if branch.upper() == 'A':
            print(f'{"_"*40} \nРабота з Adress_book')
            while True:
                user_command = input('AdressBook >>> ')
                command, data = command_parser(user_command)
                print(command(contacts, *data))
                if command is exiting:
                    print(f'Возврат в предидущее меню. Завершена работа c Adress_book.\n{"_"*40} ')
                    break
        elif branch.upper() == 'N':
            while True:
                user_command = input('>>> ')
                print(user_command)     # Коли будуть команди в Notates.py, цей код перепишеться
                if user_command =='ex':
                    break
        elif branch.upper() == 'X':
            #writing_db(contacts)
            break




if __name__ == '__main__':
    main()