from cli_assis_teem01.Notates import *
from  cli_assis_teem01.AdressBook import *



def main():
    while True:
        branch = input('Выберите одну из предложеных команд: '
              '\nNotate - Введите(N) | AdressBook - Введите(A)\n'
              'Для завершения работы помощника ведите (X)\n>>>')

        if branch.upper() == 'A':
            print(f'{"_"*40} \nРабота з Adress_book')
            contacts = reading_db(file_name)
            while True:
                user_command = input('AdressBook >>> ')
                command, data = command_parser(user_command)
                print(command(contacts, *data))
                if command is backing:
                    print(f'Возврат в предыдущее меню. Завершена работа c Adress_book.\n{"_"*40} ')
                    break
        elif branch.upper() == 'N':
            print(f'{"_" * 40} \nРабота з Notates')
            notates_list = reading_db_notate(file_name_notates)
            while True:
                user_command_not = input('>>> ')
                command_not, data = command_parser_not(user_command_not)
                print(command_not(notates_list, *data))
                if command_not is backing_notates:
                    print(f'Возврат в предыдущее меню. Завершена работа c Notates.\n{"_" * 40} ')
                    break
        elif branch.upper() == 'X':
            break




if __name__ == '__main__':
    main()