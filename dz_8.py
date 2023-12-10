"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.

1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Дополнить справочник возможностью копирования данных 
из одного файла в другой. Пользователь вводит номер 
строки, которую необходимо перенести из одного файла в другой.

"""
from csv import DictReader, DictWriter


def write_handbook():

    count_inp = int(input("Введите количество вводимых данных: "))
    data = []
    for _ in range(count_inp):
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        phone_numb = input("Введите номер телефона: ")

        entry = {"Фамилия": last_name, "Имя": first_name,
                 "Отчество": middle_name, "НомерТелефона": phone_numb, }
        data.append(entry)

    with open("handbook.csv", "a", newline='', encoding='utf-8') as file:
        fieldnames = ["Фамилия", "Имя", "Отчество", "НомерТелефона"]
        csv_dict_writer = DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            csv_dict_writer.writeheader()
        csv_dict_writer.writerows(data)

    print("Данные успешно записаны в справочник!")


def read_handbook():
    result_data = []
    try:
        with open("handbook.csv", 'r', newline='', encoding='utf-8') as file:
            csv_reader = DictReader(file)

            for row in csv_reader:
                result_data.append(dict(row))

        print(result_data)
    except FileNotFoundError:
        print("В справочнике нет данных.")


def search_by_handbook():
    try:
        search_type = int(
            input("Введите 1 для поиска по имени, 2 - по фамилии: "))
        search_query = input("Введите значение для поиска: ").lower()

        if search_type not in [1, 2]:
            print("Некорректный ввод. Введите 1 или 2.")
            return

        with open("handbook.csv", 'r', newline='', encoding='utf-8') as file:
            csv_reader = DictReader(file)
            result_data = filter_data_by_search(
                csv_reader, search_type, search_query)
        print(result_data)

    except ValueError:
        print("Некорректный ввод. Введите целое число.")


def filter_data_by_search(csv_reader, search_type, search_query):
    result_data = []

    for row in csv_reader:
        if search_type == 1 and row["Имя"].lower() == search_query:
            result_data.append(dict(row))
        elif search_type == 2 and row["Фамилия"].lower() == search_query:
            result_data.append(dict(row))

    return result_data


def copy_row_between_handbook(output_file_path):
    try:
        with open("handbook.csv", 'r', newline='', encoding='utf-8') as input_file:
            csv_reader = DictReader(input_file)
            data = list(csv_reader)

        print("Доступные строки:")
        for i, row in enumerate(data, start=1):
            print(f"{i}. {row}")

        row_number = int(input("Введите номер строки для копирования: "))
        if 1 <= row_number <= len(data):
            selected_row = data[row_number - 1]

            with open(output_file_path, 'a', newline='', encoding='utf-8') as output_file:
                csv_writer = DictWriter(
                    output_file, fieldnames=csv_reader.fieldnames)

                if output_file.tell() == 0:
                    csv_writer.writeheader()

                csv_writer.writerow(selected_row)

            print("Строка успешно скопирована.")
        else:
            print("Некорректный номер строки.")
        print()

    except FileNotFoundError:
        print("Файл не найден.")
    except ValueError:
        print("Некорректный ввод номера строки.")


def clear_handbook(file_path):

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        file.truncate(0)
    print(f"Файл {file_path} успешно очищен.")


def main():
    while True:
        print("Выберете действие. При вводе иного значения выход!")
        print("1 - запись в справочник")
        print("2 - чтение справочника")
        print("3 - поиск по фамилии или имени")
        print("4 - скопировь справочник в другой файл")
        print("5 - очистить справочник")
        num = int(input("Ваш выбор? :"))

        if num not in (1, 2, 3, 4, 5):
            print("Выход из программы!")
            break
        else:
            if num == 1:
                write_handbook()
            elif num == 2:
                read_handbook()
            elif num == 3:
                search_by_handbook()
            elif num == 4:
                copy_file = input("Введите имя файла в который скопировать: ")
                copy_row_between_handbook(copy_file + ".csv")
            elif num == 5:
                clear_file = input("Введите имя файла который очистить: ")
                clear_handbook(clear_file + ".csv")


main()
