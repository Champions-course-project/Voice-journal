"""
Модуль для эмуляции запросов на сервер и получения ответов.\n
При необходимости все функции могут быть заменены на реальное обращение к серверу.\n
Основные запросы:
- GET - для получения информации с сервера;
- POST - для сохранения информации на сервере.
"""


import json
import requests

URL = 'http://85.15.66.62'

WITH_SERVER = False


def get_from_file(requests_dict: dict):
    """
    Реализует фиктивный запрос на сервер - открывает файл и выдает необходимую информацию.
    """
    with open("data.json", "r", encoding="UTF-8") as IF:
        data = (dict)(json.load(IF))
    ERR = {"error": True}
    requested_info = requests_dict["request"]
    given_args = requests_dict["args"]
    output_dict = {}
    try:
        if 'faculty' == requested_info:
            output_dict = {'error': False, 'data': (list)(data.keys())}

        elif 'course' == requested_info:
            if "faculty" in given_args:
                output_dict = {'error': False, 'data': (
                    list)(data[given_args["faculty"]].keys())}
            else:
                output_dict = ERR

        elif 'group' == requested_info:
            if "faculty" in given_args and "course" in given_args:
                output_dict = {'error': False, 'data': (list)(
                    data[given_args["faculty"]][given_args["course"]])}
            else:
                output_dict = ERR

        elif 'students' == requested_info:
            if "faculty" in given_args and "course" in given_args and "group" in given_args:
                with open("students_list.json", "r", encoding="UTF-8") as IF:
                    students_data = (dict)(json.load(IF))
                try:
                    students_list = (list)(
                        students_data[given_args["group"]])
                except:
                    students_list = []
                output_dict = {'error': False, 'data': students_list}
            else:
                output_dict = ERR

        elif 'dates' == requested_info:
            if "faculty" in given_args and "course" in given_args and "group" in given_args:

                dates_list = []
                with open("Dates.txt", "r", encoding="UTF-8") as IF:
                    for line in IF:
                        dates_list.append(line.replace("\n", ""))
                output_dict = {'error': False, 'data': dates_list}
            else:
                output_dict = ERR

        elif 'statuses' == requested_info:
            if "faculty" in given_args and "course" in given_args and "group" in given_args:

                with open("statuses.json", "r", encoding="UTF-8") as IF:
                    statuses = (dict)(json.load(IF))
                try:
                    output_dict = {'error': False, 'data': (dict)(
                        statuses[given_args["faculty"]][given_args["course"]][given_args["group"]])}
                except:
                    output_dict = {'error': False, 'data': {}}
            else:
                output_dict = ERR

    except:
        output_dict = ERR

    return output_dict


def get_faculties():
    """
    Возвращает список факультетов.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_send(requested_val='faculty', req_type='load')


def get_courses(faculty: str):
    """
    Возвращает список курсов на основе выбранного факультета.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_send(requested_val='course', req_type='load', faculty=faculty)


def get_groups(faculty: str, course: str):
    """
    Возвращает список групп на основе выбранных факультета и курса.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_send(requested_val='group', req_type='load', faculty=faculty, course=course)


def get_students(faculty: str, course: str, group: str):
    """
    Возвращает список студентов на основе выбранных факультета, курса и группы.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_send(requested_val="students", req_type='load', faculty=faculty, course=course, group=group)


def get_dates(faculty: str, course: str, group: str):
    """
    Возвращает список дат на основе выбранных факультета, курса и группы.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_send(requested_val="dates", req_type='load', faculty=faculty, course=course, group=group)


def get_statuses(faculty: str, course: str, group: str):
    """
    Возвращает все выставленные статусы на основе выбранных факультета, курса и группы.\n
    Осуществляет фиктивный запрос на сервер.
    """
    return request_send(requested_val="statuses", req_type='load', faculty=faculty, course=course, group=group)


def request_send(req_type: str, *, requested_val: str | None = None, **kwargs):
    """
    Осуществляет запрос для получеения информации с заданным списком параметров либо для сохранения.
    """
    ERR = {'error': 1}
    # заглушка для будущих запросов
    try:
        if req_type != 'save' and requested_val == None:
            raise ValueError(
                "Requested value cannot be None while not saving.")
        if req_type == 'load':
            args_list = \
                {
                    "data": {
                        "request": requested_val,
                        "args": kwargs
                    },
                    "type": req_type
                }
        elif req_type == 'save':
            args_list = \
                {
                    "data": {"args": kwargs['statuses']},
                    "type": req_type
                }
        else:
            raise ValueError("Invalid request type.")
        if WITH_SERVER:
            answer = requests.request(
                "POST", URL, allow_redirects=False, json=args_list)
            list_to_return = json.loads(answer.text)
        else:
            if req_type == 'load':
                list_to_return = get_from_file(args_list['data'])
            else:
                status = save_to_file(args_list['data'])
                if status == 200:
                    list_to_return = {'error': 0}
                else:
                    return ERR

    except:
        return ERR
    if 'error' in list_to_return:
        if not list_to_return['error'] and ('data' in list_to_return or req_type == 'save'):
            return list_to_return
        else:
            return ERR
    else:
        return ERR


# DONE
def save_statuses(statuses):
    """
    Сохраняет все выставленные статусы.\n
    Осуществляет фиктивный запрос на сервер.\n
    Возвращает состояние запроса.
    """
    return request_send(req_type='save', statuses=statuses)


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
    faculty_dict = statuses_input['args']
    for faculty in faculty_dict:
        courses_dict = faculty_dict[faculty]
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
