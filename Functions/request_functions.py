"""
Модуль для эмуляции запросов на сервер и получения ответов.\n
При необходимости все функции могут быть заменены на реальное обращение к серверу.\n
Основные запросы:
- GET - для получения информации с сервера;
- POST - для сохранения информации на сервере.
"""


import json
import requests

URL = 'localhost/table.html'


def get_faculties():
    """
    Возвращает список факультетов.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_get()


def get_courses(faculty: str):
    """
    Возвращает список курсов на основе выбранного факультета.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_get(faculty=faculty)


def get_groups(faculty: str, course: str):
    """
    Возвращает список групп на основе выбранных факультета и курса.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_get(faculty=faculty, course=course)


def get_students(faculty: str, course: str, group: str):
    """
    Возвращает список студентов на основе выбранных факультета, курса и группы.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_get(faculty=faculty, course=course, group=group, type="students")


def get_dates(faculty: str, course: str, group: str):
    """
    Возвращает список дат на основе выбранных факультета, курса и группы.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_get(faculty=faculty, course=course, group=group, type="dates")


def get_statuses(faculty: str, course: str, group: str):
    """
    Возвращает все выставленные статусы на основе выбранных факультета, курса и группы.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_get(faculty=faculty, course=course, group=group, type="statuses")


def request_get(**kwargs):
    """
    Осуществляет GET-запрос по указанному URL с заданным списком параметров.
    """
    args_list = []
    for key in kwargs:
        args_list.append("{0}={1}".format(key, kwargs[key]))
    # заглушка для будущих запросов
    request_URL = URL + "?" + "&".join(args_list)

    # Так как запрос отправляется на сервер, содержащий таблицу, то и ответ придет в виде таблицы.
    # Таким образом, потребуется осуществить ее парсинг.
    # ЛИБО: запрос GET вернет JSON-объект, который тоже необходимо пропарсить и вставить в таблицу через JS/PHP

    # answer = requests.request("GET", request_URL, allow_redirects=False)
    # list_to_return = json.loads(answer.text)

    # запрос типа отправлен, получен ответ - нужный список
    list_to_return = get_from_file(request_URL)
    return list_to_return


def get_from_file(URL: str):
    """
    Реализует фиктивный запрос на сервер - открывает файл и выдает необходимую информацию.
    """
    with open("data.json", "r", encoding="UTF-8") as IF:
        data = (dict)(json.load(IF))
    request_part = URL.split("?")[1]
    requests_dict = {}
    if request_part:
        requests_list = request_part.split("&")
        for line in requests_list:
            kw = line.split("=")[0]
            arg = line.split("=")[1]
            requests_dict[kw] = arg
    if "faculty" in requests_dict:
        if "course" in requests_dict:
            if "group" in requests_dict:
                if "type" in requests_dict:
                    if requests_dict["type"] == "students":
                        with open("students_list.json", "r", encoding="UTF-8") as IF:
                            students_data = (dict)(json.load(IF))
                        try:
                            students_list = (list)(
                                students_data[requests_dict["group"]])
                        except KeyError:
                            return []
                        return students_list
                    elif requests_dict["type"] == "dates":
                        dates_list = []
                        with open("Dates.txt", "r", encoding="UTF-8") as IF:
                            for line in IF:
                                dates_list.append(line.replace("\n", ""))
                        return dates_list
                    elif requests_dict["type"] == "statuses":
                        try:
                            with open("statuses.json", "r", encoding="UTF-8") as IF:
                                statuses = (dict)(json.load(IF))
                        except:
                            return {}
                        try:
                            return (dict)(statuses[requests_dict["faculty"]][requests_dict["course"]][requests_dict["group"]])
                        except:
                            return {}
                    else:
                        return
                else:
                    return
            else:
                # снова аналогично - группы нет, остальное есть, нужно вернуть группы.
                return (list)(data[requests_dict["faculty"]][requests_dict["course"]])
        else:
            # здесь аналогично - курса нет, факультет есть, значит нужно вернуть ключи, соответствующие курсам
            return (list)(data[requests_dict["faculty"]].keys())
    else:
        # что мне здесь нужно.... если факультета нет, то я должен вернуть список ключей, соответствующих
        # факультетам - причем нумерованный, как в data.json
        return (list)(data.keys())


# DONE
def save_statuses(statuses):
    """
    Сохраняет все выставленные статусы.\n
    Осуществляет фиктивный запрос на сервер.\n
    Возвращает состояние запроса.
    """
    return request_post(statuses=statuses)


def request_post(URL: str = "", **kwargs):
    """
    Осуществляет POST-запрос по указанному URL с заданным списком параметров.\n
    Возвращает состояние запроса.
    """
    # запрос типа отправлен, получен ответ - нужный список
    request_status = save_to_file(kwargs)
    return request_status


def save_to_file(statuses_input: dict):
    """
    Реализует фиктивный запрос на сервер - открывает файл и сохраняет новую информацию.
    """
    try:
        with open("statuses.json", "r", encoding="UTF-8") as IF:
            file_statuses = (dict)(json.load(IF))
    except:
        file_statuses = {}
    # структура словаря: словарь[faculty_name][course_name][
    # group_name][date_choose][student_choose]: status
    faculty_list = statuses_input["statuses"]
    for faculty in faculty_list:
        courses_dict = faculty_list[faculty]
        for course in courses_dict:
            groups_dict = courses_dict[course]
            for group in groups_dict:
                dates_dict = groups_dict[group]
                for date in dates_dict:
                    students_dict = dates_dict[date]
                    for student in students_dict:
                        status = students_dict[student]
                        if status != "":
                            try:
                                file_statuses[faculty]
                            except:
                                file_statuses[faculty] = {}
                            try:
                                file_statuses[faculty][course]
                            except:
                                file_statuses[faculty][course] = {}
                            try:
                                file_statuses[faculty][course][group]
                            except:
                                file_statuses[faculty][course][group] = {}
                            try:
                                file_statuses[faculty][course][group][date]
                            except:
                                file_statuses[faculty][course][group][date] = {}
                            file_statuses[faculty][course][group][date][student] = status
                        else:
                            try:
                                file_statuses[faculty][course][group][date].pop(
                                    student)
                            except:
                                pass
    with open("statuses.json", "w", encoding="UTF-8") as OF:
        json.dump(file_statuses, OF, ensure_ascii=False,
                  indent=4, sort_keys=True)
    return 200
