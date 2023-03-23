from .check_name import check
import os
import time
import json
import SR.full_record as full_record
import SR.convert_number as convert_number


def speech(bytes_array: bytes, framerate: int):
    try:
        result = full_record.STT.decode_bytestream(bytes_array, framerate)
        if result:
            words_list = []
            for transcript in result['alternative']:
                words_list.append(transcript['transcript'])
            return words_list
        else:
            return False
    except Exception as exc:
        print(type(exc).__name__)
        print(exc.args)
        return False


def get_faculty(bytestream: bytes, framerate: int):
    with open(os.path.join("SR", "pnu_info", "Факультеты и институты.json"), 'r', encoding='UTF-8') as file:
        faculties_dict = json.load(file)

    # Отображение факультетов и институтов
    faculties_list = list(faculties_dict.keys())

    # цикл выбора факультета
    try:
        words_list = speech(bytestream, framerate)
        if words_list:
            number = words_list[0]
            if not words_list[0].isdigit():
                number = convert_number.convert_string(number)
            number = int(number)

            return number, faculties_list[number]
        else:
            return False, False
    except Exception as exc:
        print(type(exc).__name__)
        print(exc.args)
        return False, False


def get_course(faculty: str, bytestream: bytes, framerate: int):
    with open(os.path.join("SR", "pnu_info", "groups_info.json"), 'r', encoding='UTF-8') as file:
        groups_dict = json.load(file)
    courses_list = []
    for course_number in groups_dict[faculty].keys():
        courses_list.append(course_number)

    try:
        words_list = speech(bytestream, framerate)
        if words_list:
            course = words_list[0]
            if not words_list[0].isdigit():
                # print(course)
                # print(type(course))
                course = convert_number.convert_course(course)
            assert str(course) + " курс" in courses_list
            course = int(course)
            # while (str(course) + " курс" not in courses_list) or not course:
            #     words_list = speech()
            #     if words_list:
            #         course = words_list[0]
            #         if not words_list[0].isdigit():
            #             course = convert_number.convert_course(course)

            return course
        else:
            return False
    except Exception as exc:
        print(type(exc).__name__)
        print(exc.args)
        return False


def get_group(faculty: str, course: int, bytestream: bytes, framerate: int):
    with open(os.path.join("SR", "pnu_info", "groups_info.json"), 'r', encoding='UTF-8') as file:
        groups_dict = json.load(file)
    groups_list = groups_dict[faculty].get(str(course) + ' курс')
    if groups_list:
        try:
            words_list = speech(bytestream, framerate)
            if words_list:
                group = words_list[0]
                if not words_list[0].isdigit():
                    group = convert_number.convert_string(group)
                group = int(group)
                # while group > len(groups_list) or group < 1 or not group:
                #     print("Выберите номер группы: ")
                #     words_list = speech()
                #     if words_list:
                #         group = words_list[0]
                #         if not words_list[0].isdigit():
                #             group = convert_number.convert_string(group)
                # print(group)
                return group
            else:
                return False
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            return False
    else:
        return False


def get_date(bytestream: bytes, framerate: int):
    """
    Возвращает произнесенную дату в формате: ДД.ММ.ГГГГ.\n
    В случае неверного распознавания возвращает False.
    """
    words_list = speech(bytestream, framerate)

    if words_list:

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
        # Список дат из журнала
        dates_list = []
        with open(os.path.join("SR", "Dates.txt"), 'r', encoding='UTF-8') as F:
            for date in F:
                dates_list.append(date.replace("\n", ""))

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
                            print(f"Такой даты нет в журнале! | {date}2023")
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
                            print(f"Такой даты нет в журнале! | {date}2023")
                            return False
                    print("Распознавание даты не прошло!")
                    return False
    print("Не молчите в микрофон!")
    return False


def get_student_name(students_list: list[str], bytestream: bytes, framerate: int):
    """
    Пытается распознать произнесенную фамилию и сравнивает с имеющимся списком.\n
    При совпадении (полном или частичном, но не более одной фамилии) возвращает её.\n
    Иначе возвращает False.
    """
    words_list = speech(bytestream, framerate)

    if words_list:

        # with open(os.path.join("SR", "students_status.json"), 'r', encoding='UTF-8') as file:
        #     students_dict = json.load(file)

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
                return (str)((list)(definite_names_list)[0])
            return False
            #     print(
            #         f"Возможно вы имели в виду фамилию {possible_names_list[0]}?(Да/Нет)")
            #     print("Ваш ответ: ")
            #     choice = input().lower()
            #     while choice != "да" and choice != "нет":
            #         print("Назовите корректный ответ(Да/Нет): ")
            #         choice = input().lower()
            #     if choice == "да":
            #         return possible_names_list[0]
            #     elif choice == "нет":
            #         print("Попробуйте еще раз!")
            #         return False
            # else:
            #     print("Выберите один из возможных вариантов фамилий(номер):")
            #     for name_index in range(len(possible_names_list)):
            #         print(
            #             f"{name_index + 1}. {possible_names_list[name_index]}")
            #     try:
            #         choice = int(input("Ваш выбор: "))
            #         while choice <= 0 or choice > len(possible_names_list):
            #             choice = int(input("Введите корректный номер: "))
            #     except ValueError:
            #         print("Введен недопустимый символ!")
            #         choice = int(input("Введите корректный номер: "))
            #         while choice <= 0 or choice > len(possible_names_list):
            #             choice = int(input("Введите корректный номер: "))
            #     print(
            #         f"Ваш выбор по номеру {choice} - {possible_names_list[choice - 1]}")
            #     return possible_names_list[choice - 1]
        print("Распознавание не прошло! Попробуйте еще раз!")
        return False
    print("Не молчите в микрофон!")
    return False


def get_status(bytestream: bytes, framerate: int):
    words_list = speech(bytestream, framerate)

    if words_list:
        excellent_list = ['отлично', 'пять', 'пятерка']
        good_list = ['хорошо', 'четыре', 'четверка']
        satisfactory_list = ['удовлетворительно', 'три', 'тройка']
        bad_list = ['неудовлетворительно', 'два', 'двойка']
        absent_list = ['неявка', 'отсутствие', 'отсутствует']
        present_list = ['явка', 'присутствие', 'присутствует']
        reason_list = ['болеет', 'причина']
        exam_good_list = ['зачёт', 'зачет']
        exam_bad_list = ['незачёт', 'незачет']
        status = words_list[0]
        if status in excellent_list:
            return "Отлично"
        elif status in good_list:
            return "Хорошо"
        elif status in satisfactory_list:
            return "Удовлетворительно"
        elif status in bad_list:
            return "Неудовлетворительно"
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


def update_status(date, student_name, status):
    with open(os.path.join("SR", "students_status.json"), 'r', encoding='UTF-8') as file:
        students_dict = json.load(file)
    students_dict[student_name][date] = status
    with open(os.path.join("SR", "students_status.json"), 'w', encoding='UTF-8') as file:
        json.dump(students_dict, file, indent=4, ensure_ascii=False)
    print(
        f"Статус на <{date}> студента <{student_name}> успешно изменен на <{status}>!")
    return True


def main():
    print("Вас приветствует голосовой ассистент!")
    time.sleep(2)
    faculty_input = get_faculty()
    if faculty_input:
        course_input = get_course(faculty_input)
        if course_input:
            print(get_group(faculty_input, course_input))
    print("Назовите <дату>...")
    date = get_date()
    if date:
        print("Назовите <фамилию студента>...")
        student_name = get_student_name()
        if student_name:
            print("Назовите <статус>...")
            status = get_status()
            if status:
                # !!! Внимание, затычка "2023"
                if update_status(date + "2023", student_name, status):
                    return True
    print("Ошибочка!")
    return False

# get_student_name()
