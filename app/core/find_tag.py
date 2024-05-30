import os
import sys

from bs4 import BeautifulSoup

tags_to_check = ["p", "button", "h2", "h"]

# Возвращаем все что есть в каталоге
dirt = os.listdir("../../app")


def get_html(dir):
    """Создаем пустой массив в который будем добавлять все HTML файлы"""
    html_list = []
    """Проходимся по всем папкам от первой до последней"""
    for i in range(len(dir)):
        path = f"../../app/{dir[i]}"  # получаем директорию i-ой папки
        os.chdir(path)  # перемещаемся в директорию i-ой папки
        path_file = os.listdir(path)  # получаем список файлов i-ой папки

        for x in path_file:  # цикле от первого до последнего файла i-ой папки
            if x.endswith(".html"):  # ищем HTML файлы
                cv = os.path.dirname(os.path.abspath(x))  # путь к папке
                """Проверяем ОС"""
                if sys.platform == "darwin":
                    html_list.append(cv + "/" + x)
                elif sys.platform == "win32":
                    html_list.append(cv + "//" + x)
    """Возращаем массив HTML файлов"""
    return html_list


li_html = get_html(dirt)


def read_html(html_list, mark, tags):
    """Проходимся по массиву"""
    for i in html_list:
        """Читаем данные из массива"""
        with open(i, "r") as f:
            """Читаем строчки"""
            lines = f.readlines()
            """Выводим строки с их номером"""
            for number_of_line, line in enumerate(lines, start=1):
                for tag in tags:
                    if tag in line:
                        soup = BeautifulSoup(line, "lxml")
                        """Проходимся по тегам"""
                        for elem in soup.find_all(tag):
                            """Если не находим атрибут с маркой то показываем где и какой тег, и на какой линии"""
                            if not elem.has_attr(mark):
                                print(
                                    f"Tag {tag} not contain {mark} in file {os.path.abspath(i)} at line {number_of_line}: {elem}"
                                )
