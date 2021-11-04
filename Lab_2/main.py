import psycopg2
import keyboard
import time
from config import host, user, password, db_name
import control


def main():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        print("""Для генерации данных нажмите '1'
Для работы с таблицами(добавление/редактирование/удаление) нажмите '2'
Для поиска данных нажмите 3
Для выхода из любого пункла/программы нажмите 0
                """)
        while keyboard.read_key() != "0":
            if keyboard.read_key() == "1":
                while True:
                    print("\nВведите название таблицы и количество данных")
                    command_input = input()
                    command = command_input.split(' ')
                    if command[0] == "students":
                        control.generate_students(int(command[1]), connection)
                        continue
                    elif command[0] == "subjects":
                        control.generate_subjects(int(command[1]), connection)
                        continue
                    elif command[0] == "groups":
                        control.generate_groups(int(command[1]), connection)
                        continue
                    elif command[0] == "stop":
                        break
                    else:
                        print("Таблица не найдена!")
                        continue
            elif keyboard.read_key() == "2":
                while True:
                    print("\nВведите действие:")
                    command_input_obj = input()
                    command_input = command_input_obj.split(' ')
                    if command_input[0] == "add":
                        print("\nВведите данные:")
                        command = input()
                        if command_input[1] == "student":
                            if len(command.split(' ')) == 3:
                                control.add_student(command, connection)
                                continue
                            else:
                                print("Not correct input data")
                                continue
                        elif command_input[1] == "group":
                            if len(command.split(' ')) == 3:
                                control.add_group(command, connection)
                                continue
                            else:
                                print("Not correct input data")
                                continue
                        elif command_input[1] == "subject":
                            if len(command.split(' ')) == 2:
                                control.add_subject(command, connection)
                                continue
                            else:
                                print("Not correct input data")
                                continue
                        else:
                            print("Таблица не найдена!")
                            continue
                    elif command_input[0] == "update":
                        print("\nВведите данные:")
                        command = input()
                        if command_input[1] == "student":
                            if len(command.split(' ')) == 3:
                                control.update_student(command, connection)
                                continue
                            else:
                                print("Not correct input data")
                                continue
                        elif command_input[1] == "group":
                            if len(command.split(' ')) == 3:
                                control.update_group(command, connection)
                                continue
                            else:
                                print("Not correct input data")
                                continue
                        elif command_input[1] == "subject":
                            if len(command.split(' ')) == 2:
                                control.update_subject(command, connection)
                                continue
                            else:
                                print("Not correct input data")
                                continue
                        else:
                            print("Таблица не найдена!")
                            continue
                    elif command_input[0] == "delete":
                        print("\nВведите данные:")
                        command = input()
                        if len(command.split(' ')) == 1 and (isinstance(command.split(' ')[0], int)):
                            if command_input[1] == "student":
                                control.delete_student(command, connection)
                                continue
                            elif command_input[1] == "group":
                                control.delete_group(command, connection)
                                continue
                            elif command_input[1] == "subject":
                                control.delete_subject(command, connection)
                                continue
                            else:
                                print("Таблица не найдена!")
                                continue
                        else:
                            print("Not correct input data")
                            continue
                    elif command_input[0] == "stop":
                        break
                    else:
                        print("Такого действия не найдено!")
                        continue
            elif keyboard.read_key() == "3":
                while True:
                    print("Введите таблицу:")
                    command_input_obj = input()
                    if command_input_obj == "students":
                        print("Введите данные:")
                        command = input()
                        start_time = time.time()
                        c = control.search_in_students(command, connection)
                        print("Время выполнения запроса: %s" % (time.time() - start_time))
                        if c is []:
                            print("There are no results for this search\n")
                        else:
                            for i in c:
                                print("|", i[0], "|", i[1], "|", i[2], "|", i[3], "|")
                        continue
                    elif command_input_obj == "groups":
                        print("Введите данные:")
                        command = input()
                        start_time = time.time()
                        c = control.search_in_groups(command, connection)
                        print("Время выполнения запроса: %s" % (time.time() - start_time))
                        if c is []:
                            print("There are no results for this search")
                        else:
                            for i in c:
                                print("|", i[0], "|", i[1], "|", i[2], "|\n")
                        continue
                    elif command_input_obj == "subjects":
                        print("Введите данные:")
                        command = input()
                        start_time = time.time()
                        c = control.search_in_subjects(command, connection)
                        print("Время выполнения запроса: %s" % (time.time() - start_time))
                        if c is []:
                            print("There are no results for this search")
                        else:
                            for i in c:
                                print("|", i[0], "|", i[1], "|\n")
                        continue
                    elif command_input_obj == "stop":
                        break
                    else:
                        print("Таблица не найдена!")
                        continue
        print("\nGoodBye)")
    except Exception as _ex:
        print("[INFO] Error with connection PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection closed")


if __name__ == "__main__":
    main()
