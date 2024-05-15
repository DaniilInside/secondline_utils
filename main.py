from database import connect_db_rnis_to, connect_db_avtovokzal
from user_operations import check_user, copy_user

def main():
    print('Выберите, где хотите скопировать учетку:')
    print('1. РНИС ТО\n2. Автовокзал')
    choice = int(input())

    if choice not in [1, 2]:
        print('Неверный выбор!')
        return

    if choice == 1:
        connection = connect_db_rnis_to()
    elif choice == 2:
        connection = connect_db_avtovokzal()
    
    print('Введите логин пользователя, которого хотите скопировать:')
    username = input()
    check = check_user(connection, username)

    if check:
        print('Начинаем копирование!')
        new_username = input('Как хотите назвать копию? ')
        if new_username:
            clone_success = copy_user(connection, username, new_username)
            if clone_success:
                print('Копирование успешно!')
    else:
        print('Такого пользователя не существует!')

    connection.close()
    connection.close()

if __name__ == "__main__":
    main()
