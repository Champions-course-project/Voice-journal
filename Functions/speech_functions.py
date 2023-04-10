"""
Модуль, осуществляющий распознавание всех существующих команд.
"""


import json
import os
from .check_name import check
import Functions.convert_number as convert_number
import Functions.request_functions


def choose_command(words_list: list):
    """
    Распознаватель ключевых команд.\n
    Входные аргументы:
    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk.\n
    Выходные данные:
    - натуральное число, характеризующее команду;
    - False в противном случае.
    """
    if words_list:
        code_phrase = words_list[0].lower()
        if code_phrase == "выбрать факультет":
            return 1
        if code_phrase == "выбрать курс":
            return 2
        if code_phrase == "выбрать группу":
            return 3
        if code_phrase == "сохранить":
            return 4
        if code_phrase == "отменить":
            return 5
    return False


def get_faculty(words_list: list, faculties_list: list[str] = []):
    """
    Распознаватель факультета на основе имеющегося списка.\n
    Входные аргументы:
    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk;
    - faculties_list - список факультетов, полученный из программы либо при помощи запроса.\n
    Выходные данные:
    - пара "число - название факультета" в случае успеха;
    - пара False - False в противном случае.
    """
    if not faculties_list:
        faculties_list = Functions.request_functions.get_faculties()

    try:
        if words_list:
            number = words_list[0]
            if not words_list[0].isdigit():
                number = convert_number.convert_string(number)
            number = int(number)
            assert number != -1 and number <= len(faculties_list)
            return number
        else:
            return False
    except Exception as exc:
        print(type(exc).__name__)
        print(exc.args)
        return False


def get_course(faculty: str, words_list: list, courses_list: list[str] = []):
    """
    Распознаватель номера курса на основе имеющегося списка.\n
    Входные аргументы:
    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk.\n
    - faculty - наименование факультета в списке;
    - courses - список курсов, полученный из программы либо при помощи запроса.\n
    Выходные данные:
    - число, соответствующее номеру курса в случае успеха;
    - False в противном случае.
    """
    if not courses_list:
        courses_list = Functions.request_functions.get_courses(faculty)

    try:
        if words_list:
            course = words_list[0]
            if not words_list[0].isdigit():
                course = convert_number.convert_course(course)
            course = int(course)
            return course
        else:
            return False
    except Exception as exc:
        print(type(exc).__name__)
        print(exc.args)
        return False


def get_group(faculty: str, course: str, words_list: list, groups_list: list[str] = []):
    """
    Распознаватель произнесенного номера группы на основе списка групп.\n
    Входные аргументы:
    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk.\n
    - faculty - наименование факультета в списке;
    - course - наименование курса в списке;
    - groups_list - список групп, полученный из программы либо при помощи запроса.\n
    Выходные данные:
    - номер группы в списке групп в случае успеха;
    - False в противном случае.
    """
    # Требуется изменение: список групп должен быть получен из сети, либо как аргумент
    if not groups_list:
        groups_list = Functions.request_functions.get_groups(faculty, course)
    if groups_list:
        try:
            if words_list:
                group = words_list[0]
                if not words_list[0].isdigit():
                    group = convert_number.convert_string(group)
                group = int(group)
                assert group > 0 and group <= len(groups_list)
                return group
            else:
                return False
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            return False
    else:
        return False


def get_date(words_list: list, faculty: str = "", course: str = "", group: str = "", dates_list: list[str] = []):
    """
    Распознаватель произнесённой даты.\n
    Входные аргументы:

    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk;
    - faculty - наименование факультета в списке;
    - course - наименование курса в списке;
    - group - наименование группы в списке; 
    - dates_list - список дат, полученный из программы либо при помощи запроса.\n
    Для успешного распознавания требуется наличие dates_list.\n
    При отсутствии списка дат происходит проверка на наличие faculty, course, group.\n
    Если и они отсутствуют, возвращается False.\n
    Выходные данные:
    - дата в формате ДД.ММ.ГГГГ в случае успеха;
    - False в противном случае.
    """
    try:
        if words_list:
            # Список дат должен быть получен из сети, либо как аргумент
            if not dates_list:
                assert faculty and course and group
                dates_list = Functions.request_functions.get_dates(
                    faculty, course, group)
            days_list = [
                'первое', 'второе', 'третье', 'четвертое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвертое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое'
            ]
            months_list = [
                'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
            ]

            date = ""
            for string in words_list:
                month = string.split(' ')[-1]
                if month.lower() in months_list:

                    # создание номера месяца
                    month = str(months_list.index(month) + 1)
                    if len(month) == 1:
                        month = "0" + month

                    string = string.split(' ')[:-1]
                    # возврат числа
                    if string[0].isdigit():
                        # если вернул число - дополняет его до даты
                        if len(string[0]) == 1:
                            day = "0" + string[0]
                        else:
                            day = string[0]
                        date = f"{day}.{month}."
                        # !!! Внимание на "2023" - это затычка
                        if date + "2023" in dates_list:
                            return date
                        print(f"Такой даты нет в журнале! | {date}2023")
                        return False

                    # если слово "первое", "второе", ..., но не "двадцать первое"
                    elif len(string) == 1:
                        day = string[0].lower().replace('ё', 'е')
                        if day in days_list:
                            # конвертировали в день
                            day = str(days_list.index(day) + 1)
                            if len(day) == 1:
                                day = "0" + day
                            date = f"{day}.{month}."
                            if date + "2023" in dates_list:
                                return date
                            else:
                                print(
                                    f"Такой даты нет в журнале! | {date}2023")
                                return False
                        print("Распознавание даты не прошло!")
                        return False

                    # если слова "двадцать первое", "двадцать второе", ...
                    elif len(string) == 2:
                        for element in string:
                            date += element.lower().replace('ё', 'е') + " "
                        if date[:-1] in days_list:
                            date = str(days_list.index(date[:-1]) + 1)
                            date = date + "." + month + "."
                            # !!! Внимание на "2023" - это затычка
                            if date + "2023" in dates_list:
                                return date
                            else:
                                print(
                                    f"Такой даты нет в журнале! | {date}2023")
                                return False
                        print("Распознавание даты не прошло!")
                        return False
        print("Не молчите в микрофон!")
        return False
    except AssertionError:
        return False


def get_student_name(words_list: list, faculty: str = "", course: str = "", group: str = "", students_list: list[str] = []):
    """
    Распознаватель произнесенных фамилий.\n
    Входные аргументы:
    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk;
    - faculty - наименование факультета в списке;
    - course - наименование курса в списке;
    - group - наименование группы в списке; 
    - students_list - список студентов, полученный из программы либо при помощи запроса. Формат: Фамилия Имя Отчество.\n
    Для успешного распознавания требуется наличие students_list.\n
    При отсутствии списка студентов происходит проверка на наличие faculty, course, group.\n
    Если и они отсутствуют, возвращается False.\n
    Выходные данные:
    - ФИО студента в случае успешного распознавания и совпадения;
    - False в противном случае.
    """
    try:
        if words_list:
            # Список студентов должен быть получен из сети, либо как аргумент
            if not students_list:
                assert faculty and course and group
                students_list = Functions.request_functions.get_students(
                    faculty, course, group)
            # распознавание фамилий: полное или частичное
            possible_names_list = set()
            definite_names_list = set()
            for student_name in students_list:

                for word in words_list:

                    status = check(student_name.split(" ")[0], word)

                    if status == 2:
                        definite_names_list.add(student_name)
                    elif status == 1:
                        possible_names_list.add(student_name)

            if definite_names_list:
                if len(definite_names_list) == 1:
                    return (str)((list)(definite_names_list)[0])
                return False

            elif possible_names_list:
                if len(possible_names_list) == 1:
                    return (str)((list)(possible_names_list)[0])
                return False

            print("Распознавание не прошло! Попробуйте еще раз!")
            return False
        print("Не молчите в микрофон!")
        return False
    except AssertionError:
        return False


def get_status(words_list: list):
    """
    Распознаватель произнесенных оценок и статусов студентов.\n
    Входные аргументы:
    - words_list - список слов и словосочетаний, расшифрованных при помощи SR или Vosk.\n
    Выходные данные:
    - строка, указывающая на состояние, в случае успеха;
    - False в противном случае.
    """
    if words_list:
        excellent_list = ['отлично', 'пять', 'пятерка']
        good_list = ['хорошо', 'четыре', 'четверка']
        satisfactory_list = ['удовлетворительно', 'три', 'тройка']
        bad_list = ['неудовлетворительно', 'два', 'двойка']
        absent_list = ['неявка', 'отсутствие', 'отсутствует']
        present_list = ['явка', 'присутствие', 'присутствует']
        reason_list = ['болеет', 'причина']
        exam_good_list = ['зачёт', 'зачет', 'зачтено']
        exam_bad_list = ['незачёт', 'незачет', 'не зачтено']
        status = words_list[0]
        if status in excellent_list:
            return "Отлично"
        elif status in good_list:
            return "Хорошо"
        elif status in satisfactory_list:
            return "Удовл."
        elif status in bad_list:
            return "Неудовл."
        elif status in absent_list:
            return "Неявка"
        elif status in present_list:
            return "Явка"
        elif status in reason_list:
            return "Болеет"
        elif status in exam_good_list:
            return "Зачёт"
        elif status in exam_bad_list:
            return "Незачёт"
    print("Попробуйте еще раз!")
    return False
