import os

def check_i18n_tags(directory):
    """
    Функция проверяет все HTML файлы в папке и подпапках на отсутствие меток для перевода.
    Ищет теги <p>, <button>, <h2> и <h>, которые должны иметь метку 'i18n', но не имеют её.
    """
    # Перебираем все, что находится в папке: файлы и под папки
    for element in os.listdir(directory):
        # Собираем полный путь к элементу
        full_path = os.path.join(directory, element)
        # Если это папка, то проверяем и её содержимое
        if os.path.isdir(full_path):
            check_i18n_tags(full_path)
        elif element.endswith(".html"):  # Если это файл HTML, то открываем его
            # Открываем файл и смотрим его содержимое
            with open(full_path, 'r', encoding='utf-8') as file:
                line_number = 0  # Счетчик строк, чтобы знать, где ошибка
                for line in file:  # Смотрим файл по строкам
                    line_number += 1
                    # Если в строке есть тег <p> без метки 'i18n', сообщаем об ошибке
                    if '<p>' in line and 'i18n' not in line:
                        print(f"Ошибка в файле {full_path} на строке {line_number}: <p> без i18n")
                    # Проверяем и другие теги аналогичным образом
                    if '<button>' in line and 'i18n' not in line:
                        print(f"Ошибка в файле {full_path} на строке {line_number}: <button> без i18n")
                    if '<h2>' in line and 'i18n' not in line:
                        print(f"Ошибка в файле {full_path} на строке {line_number}: <h2> без i18n")
                    if '<h>' in line and 'i18n' not in line:
                        print(f"Ошибка в файле {full_path} на строке {line_number}: <h> без i18n")

def main():
    """
    Основная функция, спрашивает у пользователя, где находятся HTML файлы, и проверяет их.
    """
    # Спрашиваем у пользователя путь к папке с HTML файлами
    directory = input("Введите путь к директории с HTML файлами: ")
    # Проверяем файлы на ошибки
    check_i18n_tags(directory)

main()
