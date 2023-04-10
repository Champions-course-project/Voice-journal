"""
Модуль для эмуляции запросов на сервер и получения ответов.\n
При необходимости все функции могут быть заменены на реальное обращение к серверу.\n
Основные запросы:
- GET - для получения информации с сервера;
- POST - для сохранения информации на сервере.
"""


import json


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


def request_get(URL: str = "", **kwargs):
    """
    Осуществляет запрос по указанному URL с заданным списком параметров.
    """
    args_list = []
    for key in kwargs:
        args_list.append("{0}={1}".format(key, kwargs[key]))
    # заглушка для будущих запросов
    request_URL = URL + "?" + "&".join(args_list)
    # запрос типа отправлен, получен ответ - нужный список
    list_to_return = get_from_file(request_URL)
    return list_to_return


def get_from_file(URL: str):
    """
    Реализует фиктивный запрос на сервер - открывает файл и выдает необходимую информацию.
    """
    with open("data.json", "r", encoding="UTF-8") as OF:
        data = (dict)(json.load(OF))
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
                        with open("students_list.json", "r", encoding="UTF-8") as OF:
                            students_data = (dict)(json.load(OF))
                        students_list = (list)(students_data[requests_dict["group"]])
                        return students_list
                    elif requests_dict["type"] == "dates":
                        dates_list = []
                        with open("Dates.txt", "r", encoding="UTF-8") as OF:
                            for line in OF:
                                dates_list.append(line.replace("\n", ""))
                        return dates_list
                    elif requests_dict["type"] == "statuses":
                        pass
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


def info_save(faculcy: str, course: str, group: str, **info):
    pass


def request_post():
    pass
