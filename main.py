from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from PyQt6.QtGui import QKeySequence, QFont
from PyQt6.QtCore import Qt
import Vosk.recorder as recorder
import Functions
import Vosk as Recognizer
from autorization import *
from table import *
import login_class
import ctypes
import resources
import json
import sys

import asyncio

myappid = "mycompany.myproduct.subproduct.version"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
ui = Ui_AuthWindow()


def new_win():
    year_cond = False
    group_cond = False
    table_cond = False
    buttonActive = False
    column_choose = -1
    row_choose = -1
    auth = login_class.LogIn()
    success = True
    partial_state = {}
    # auth.login(ui.login_lineEdit.text(),ui.password_lineEdit.text())

    def activate_voice():
        try:
            assert not buttonActive
            asyncio.run(async_activate_voice())
        except AssertionError:
            return

    async def async_activate_voice():
        """
        Основная функция по обработке распознавания речи.\n
        Последовательно производит несколько проверок:
        - специальные команды;
        - открыта таблица и произнесена дата;
        - открыта таблица и произнесен порядковый номер студента;
        - открыта таблица и произнесена фамилия студента;
        - открыта таблица, выбрана ячейка и произнесено состояние студента;
        - доступен выбор группы и произнесен номер группы в списке;
        - доступен выбор курса и произнесен порядковый номер курса;
        - доступен выбор факультета и произнесен номер факультета в списке.\n
        За счет этих проверок достигается работоспособность голосового управления.
        """
        nonlocal table_cond, group_cond, year_cond, buttonActive
        buttonActive = True
        buttonColor(2)
        bytes_array = recorder.Recorder.record_data()
        buttonColor(1)
        words_list = Recognizer.speech(bytes_array, recorder.Recorder.freq)
        print(words_list)
        try:
            assert words_list
            # вызов функций по распознаванию команды
            nonlocal row_choose, column_choose, partial_state
            command = Functions.speech_functions.choose_command(words_list)
            if command:  # если получена команда:
                if command == 1:  # выбрать факультет
                    addFacultyItems()
                elif command == 2 and year_cond:  # выбрать курс, открыта таблица курсов
                    addYearItems()
                elif command == 3 and group_cond:  # выбрать группу, открыта таблица групп
                    addGroupItems()
                elif command == 4:  # сохранить
                    Functions.request_functions.save_statuses(
                        partial_state)
                    partial_state = {}
                    n_ui.group_list.currentItemChanged.emit(None, None)
                elif command == 5:  # отменить
                    partial_state = {}
                    n_ui.group_list.currentItemChanged.emit(None, None)
                else:
                    n_ui.error_label.show()  # произнесли команду но ее выполнить нельзя

            elif table_cond:  # открыта таблица студентов - происходит выбор студента
                # для отправки запроса с получением дат и фамилий
                faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[
                    1]
                course_name = n_ui.year_list.currentItem().text()
                group_name = n_ui.group_list.currentItem().text().split(". ")[
                    1]
                date_choose = Functions.speech_functions.get_date(
                    words_list, faculty_name, course_name, group_name)
                if date_choose:
                    dateChoose(date_choose)
                    if row_choose != -1 and column_choose != -1:
                        selectCell(row_choose, column_choose)
                else:
                    number = Functions.speech_functions.convert_number.convert_string(
                        words_list[0])
                    if number != 0 and number <= n_ui.group_table.verticalHeader().count():
                        word = n_ui.group_table.verticalHeaderItem(
                            number - 1).text()
                        words_list[0] = word.split(". ")[1]
                    student_choose = Functions.speech_functions.get_student_name(
                        words_list, faculty_name, course_name, group_name)
                    if student_choose:
                        studentChoose(student_choose)
                        if row_choose != -1 and column_choose != -1:
                            selectCell(row_choose, column_choose)
                    elif row_choose > -1 and column_choose > -1:
                        mark_choose = Functions.speech_functions.get_status(
                            words_list)
                        if mark_choose:
                            n_ui.group_table.setItem(
                                row_choose, column_choose, QTableWidgetItem(mark_choose))
                            rememberState()
                        else:
                            n_ui.error_label.show()
                    else:
                        n_ui.error_label.show()

            elif group_cond:  # открыта таблица групп - происходит выбор группы
                course_choose = n_ui.year_list.currentItem().text()
                faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[
                    1]
                group_choose = Functions.speech_functions.get_group(
                    faculty_name, course_choose, words_list)
                if group_choose:
                    n_ui.group_list.setCurrentRow(group_choose - 1)
                else:
                    n_ui.error_label.show()

            elif year_cond:   # открыта таблица курсов - происходит выбор курса
                faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[
                    1]
                course_choose = Functions.speech_functions.get_course(
                    faculty_name, words_list)
                if course_choose:
                    n_ui.year_list.setCurrentRow(course_choose - 1)
                else:
                    n_ui.error_label.show()

            else:  # открыта только таблица с факультетами - происходит выбор факультета
                faculty_choose = Functions.speech_functions.get_faculty(
                    words_list)
                if type(faculty_choose) != bool and faculty_choose:
                    n_ui.faculty_list.setCurrentRow(faculty_choose - 1)
                else:
                    n_ui.error_label.show()

        except AssertionError:
            n_ui.error_label.show()

        finally:
            n_ui.activate_button.setEnabled(True)
            buttonColor(3)
            n_ui.activate_button.update()
            QApplication.processEvents()
            await asyncio.sleep(0.3)
            buttonActive = False

    def buttonColor(f: int):
        """
        Функция по смене состояний кнопки:
        - 1: желтая кнопка с текстом "Распознавание...";
        - 2: красная кнопка с текстом "Идёт запись...";
        - 3: белая кнопка с текстом "Голосовой ввод".
        """
        if f == 1:
            n_ui.activate_button.setText("Распознавание...")
            n_ui.activate_button.setIconSize(QtCore.QSize(0, 0))
            n_ui.activate_button.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                               "border-radius: 10px;\n"
                                               "")
        elif f == 2:
            n_ui.activate_button.setText("Идёт запись...")
            n_ui.activate_button.setIconSize(QtCore.QSize(0, 0))
            n_ui.activate_button.setStyleSheet(
                "background-color: rgb(255, 0, 0);\n"
                "border-radius: 10px;\n"
                "")
        elif f == 3:
            n_ui.activate_button.setText("Голосовой ввод")
            n_ui.activate_button.setIconSize(QtCore.QSize(35, 35))
            n_ui.activate_button.setStyleSheet("QPushButton::hover{\n"
                                               "background-color: rgb(194, 194, 194);\n"
                                               "}\n"
                                               "QPushButton{\n"
                                               "background-color: rgb(83, 83, 83);\n"
                                               "color: rgb(0, 0, 0);\n"
                                               "border-radius: 10px;\n"
                                               "background-color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "\n"
                                               "")
            n_ui.activate_button.setShortcut(QKeySequence("Ctrl+Space"))
        n_ui.activate_button.update()
        QApplication.processEvents()

    def addFacultyItems():
        """
        Функция для добавления списка факультетов.\n
        Осуществляет запрос на сервер для получения списка.
        """
        print("addFacultyItems")
        n_ui.group_table.setRowCount(0)
        n_ui.group_table.setColumnCount(0)
        n_ui.group_list.clear()
        n_ui.year_list.clear()
        n_ui.faculty_list.clear()
        n_ui.faculty_list.clearSelection()
        n_ui.help_label.setText(
            "Примечание: для выбора факультета с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой "
            "ввод\" и назвать номер факультета, указанный в списке.")
        n_ui.help_label.update()
        n_ui.error_label.hide()
        QApplication.processEvents()
        nonlocal table_cond, group_cond, year_cond
        table_cond = False
        group_cond = False
        year_cond = False
        faculties_list = Functions.request_functions.get_faculties()
        for num in range(len(faculties_list)):
            n_ui.faculty_list.addItem(
                (str)(num + 1) + ". " + faculties_list[num])
        return

    def addYearItems():
        """
        Функция для добавления списка курсов.\n
        Осуществляет запрос на сервер для получения списка.
        """
        print("addYearItems")
        try:
            current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[
                1]
        except AttributeError:
            return
        n_ui.group_table.setRowCount(0)
        n_ui.group_table.setColumnCount(0)
        n_ui.group_list.clear()
        n_ui.year_list.clear()
        n_ui.year_list.clearSelection()
        n_ui.help_label.setText(
            "Примечание: для выбора курса с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой "
            "ввод\" и назвать <b>порядковый</b> номер курса.")
        n_ui.help_label.update()
        n_ui.error_label.hide()
        QApplication.processEvents()
        nonlocal table_cond, group_cond
        table_cond = False
        group_cond = False
        courses_list = Functions.request_functions.get_courses(
            current_faculty)
        for item in courses_list:
            n_ui.year_list.addItem(item)
        nonlocal year_cond
        year_cond = True
        return

    def addGroupItems():
        """
        Функция для добавления списка групп.\n
        Осуществляет запрос на сервер для получения списка.
        """
        print("addGroupItems")
        try:
            current_course = n_ui.year_list.currentItem().text()
        except AttributeError:
            return
        n_ui.group_table.setRowCount(0)
        n_ui.group_table.setColumnCount(0)
        n_ui.group_list.clear()
        n_ui.group_list.clearSelection()
        n_ui.year_list.setStyleSheet("QListWidget{\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(83, 83, 83);\n"
                                     "selection-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(30, 185, 85);\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "QListWidget::item::hover{\n"
                                     "background-color: rgb(75, 75,75);\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "QListWidget::item::selected::hover{\n"
                                     "background-color: rgb(30, 185, 85);\n"
                                     "border-radius: 10px;\n"
                                     "}\n"
                                     "QListWidget::item::selected{\n"
                                     "background-color: rgb(30, 185, 85);\n"
                                     "border-radius: 10px;\n"
                                     "}")
        n_ui.help_label.setText(
            "Примечание: для выбора группы с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой "
            "ввод\" и назвать номер группы, указанный в списке.")
        n_ui.help_label.update()
        n_ui.error_label.hide()
        QApplication.processEvents()
        nonlocal table_cond
        table_cond = False
        i = 0
        current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[
            1]
        groups_list = Functions.request_functions.get_groups(
            current_faculty, current_course)
        for item in groups_list:
            i += 1
            n_ui.group_list.addItem(str(i) + ". " + item)
        nonlocal group_cond
        group_cond = True
        if i == 0:
            n_ui.year_list.setStyleSheet("QListWidget{\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(83, 83, 83);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(30, 185, 85);\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QListWidget::item::hover{\n"
                                         "background-color: rgb(75, 75,75);\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QListWidget::item::selected::hover{\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "border-radius: 10px;\n"
                                         "}\n"
                                         "QListWidget::item::selected{\n"
                                         "background-color: rgb(255, 0, 0);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(255, 0, 0);\n"
                                         "border-radius: 10px;\n"
                                         "}")
            n_ui.help_label.setText(
                "Примечание: на данном курсе нет групп, выберете другую!")
            n_ui.help_label.update()
            QApplication.processEvents()
            group_cond = False
        return

    def addDates():
        """
        Функция для добавления дат в таблицу.\n
        Осуществляет запрос на сервер для получения списка дат.
        """
        print("addDates")
        try:
            current_group = n_ui.group_list.currentItem().text().split(". ")[1]
        except AttributeError:
            return
        n_ui.group_table.setColumnCount(0)
        if not n_ui.group_table.rowCount():
            return
        current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[1]
        current_course = n_ui.year_list.currentItem().text()
        dates_list = Functions.request_functions.get_dates(
            current_faculty, current_course, current_group)
        if len(dates_list) == 0:
            # TODO: группа есть но занятий по предмету нет!
            nonlocal table_cond
            table_cond = False
            return
        n_ui.group_table.setColumnCount(len(dates_list))
        n_ui.group_table.setHorizontalHeaderLabels(dates_list)
        QApplication.processEvents()
        return

    def addStudents():
        """
        Функция для добавления студентов в таблицу.\n
        Осуществляет запрос на сервер для получения списка студентов.
        """
        print("addStudents")
        try:
            current_group = n_ui.group_list.currentItem().text().split(". ")[1]
        except AttributeError:
            return

        n_ui.group_table.setRowCount(0)
        n_ui.group_list.setStyleSheet("QListWidget{\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(83, 83, 83);\n"
                                      "selection-color: rgb(255, 255, 255);\n"
                                      "selection-background-color: rgb(30, 185, 85);\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QListWidget::item::hover{\n"
                                      "background-color: rgb(75, 75,75);\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QListWidget::item::selected::hover{\n"
                                      "background-color: rgb(30, 185, 85);\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QListWidget::item::selected{\n"
                                      "background-color: rgb(30, 185, 85);\n"
                                      "border-radius: 10px;\n"
                                      "}")
        n_ui.help_label.setText(
            "Примечание: для выбора учащегося с помощью голосовых команд вам необходимо нажать на кнопку "
            "\"Голосовой ввод\" и назвать дату, фамилию, а затем оценку для студента.")
        n_ui.help_label.update()
        n_ui.error_label.hide()
        nonlocal table_cond
        current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[
            1]
        current_course = n_ui.year_list.currentItem().text()
        students_list = Functions.request_functions.get_students(
            current_faculty, current_course, current_group)
        if len(students_list) == 0:
            n_ui.group_list.setStyleSheet("QListWidget{\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(83, 83, 83);\n"
                                          "selection-color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(30, 185, 85);\n"
                                          "border-radius: 10px;\n"
                                          "}\n"
                                          "QListWidget::item::hover{\n"
                                          "background-color: rgb(75, 75,75);\n"
                                          "border-radius: 10px;\n"
                                          "}\n"
                                          "QListWidget::item::selected::hover{\n"
                                          "background-color: rgb(255, 0, 0);\n"
                                          "border-radius: 10px;\n"
                                          "}\n"
                                          "QListWidget::item::selected{\n"
                                          "background-color: rgb(255, 0, 0);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "selection-color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(255, 0, 0);\n"
                                          "border-radius: 10px;\n"
                                          "}")
            n_ui.help_label.setText(
                "Примечание: в данной группе нет студентов, выберете другую!")
            n_ui.help_label.update()
            QApplication.processEvents()
            table_cond = False
            return
        n_ui.group_table.setRowCount(len(students_list))
        n_ui.group_table.setVerticalHeaderLabels(students_list)
        for i in range(len(students_list)):
            n_ui.group_table.verticalHeaderItem(i).setText(
                str(i + 1) + ". " + n_ui.group_table.verticalHeaderItem(i).text())
        table_cond = True
        nonlocal column_choose, row_choose
        column_choose = -1
        row_choose = -1
        if n_ui.group_table.rowCount() == 1:
            studentChoose(n_ui.group_table.verticalHeaderItem(
                0).text().split(". ")[1])
            row_choose = 0
        return

    def addStatuses():
        """
        Функция для добавления статусов в таблицу из сети и из локальных данных.\n
        Осуществляет запрос на сервер для получения статусов.
        """
        print("addStatuses")
        try:
            current_group = n_ui.group_list.currentItem().text().split(". ")[1]
        except AttributeError:
            return
        current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[1]
        current_course = n_ui.year_list.currentItem().text()
        # формат: словарь[дата][студент] = статус
        statuses_dict = Functions.request_functions.get_statuses(
            current_faculty, current_course, current_group)
        statuses_from_sourse(statuses_dict)
        nonlocal partial_state
        try:
            statuses_dict = partial_state[current_faculty][current_course][current_group]
            statuses_from_sourse(statuses_dict)
        except:
            return
        return

    def statuses_from_sourse(sourse: dict):
        """
        Добавляет статусы в таблицу, полученные из источника как словарь.
        """
        print("statuses_from_sourse")
        dates_list = []
        for i in range(n_ui.group_table.horizontalHeader().count()):
            dates_list.append(n_ui.group_table.horizontalHeaderItem(i).text())
        students_list = []
        for i in range(n_ui.group_table.verticalHeader().count()):
            students_list.append(
                n_ui.group_table.verticalHeaderItem(i).text().split(". ")[1])
        for date in sourse:
            for student in sourse[date]:
                status = sourse[date][student]
                row = students_list.index(student)
                col = dates_list.index(date)
                n_ui.group_table.setItem(row, col, QTableWidgetItem(status))
        return

    def studentChoose(name: str):
        """
        Осуществляет выбор студента по заданному ФИО.\n
        При неудаче ничего не изменяет.\n
        Ничего не возвращает.
        """
        print("studentChoose")
        number = n_ui.group_table.verticalHeader().count()
        index = -1
        for i in range(number):
            if name == n_ui.group_table.verticalHeaderItem(i).text().split(". ")[1]:
                index = i
                break
        if index == -1:
            n_ui.error_label.show()
            return
        n_ui.error_label.hide()
        n_ui.group_table.clearSelection()
        n_ui.group_table.selectRow(index)
        nonlocal row_choose
        row_choose = index
        if column_choose == -1:
            for i in range(n_ui.group_table.horizontalHeader().count()):
                item_prew = n_ui.group_table.item(row_choose, i)
                if item_prew == None:
                    n_ui.group_table.setItem(
                        row_choose, i, QTableWidgetItem(""))
                item = n_ui.group_table.item(row_choose, i)
                item.setSelected(True)
            QApplication.processEvents()
        return

    def dateChoose(date: str):
        """
        Осуществляет выбор даты по введенной строке.\n
        При неудаче ничего не изменяет.\n
        Ничего не возвращает.
        """
        print("dateChoose")
        number = n_ui.group_table.horizontalHeader().count()
        index = -1
        for i in range(number):
            if date + "2023" == n_ui.group_table.horizontalHeaderItem(i).text():
                index = i
                break
        if index == -1:
            n_ui.error_label.show()
            return
        n_ui.error_label.hide()
        n_ui.group_table.clearSelection()
        n_ui.group_table.selectColumn(index)
        nonlocal column_choose
        column_choose = index
        if row_choose == -1:
            for i in range(n_ui.group_table.verticalHeader().count()):
                item_prew = n_ui.group_table.item(i, column_choose)
                if item_prew == None:
                    n_ui.group_table.setItem(
                        i, column_choose, QTableWidgetItem(""))
                item = n_ui.group_table.item(i, column_choose)
                item.setSelected(True)
            QApplication.processEvents()
        return

    def selectCell(row: int = -1, col: int = -1):
        """
        Функция для выделения ячейки в таблице по заданным координатам.
        """
        print("selectCell")
        nonlocal row_choose, column_choose
        row_choose = row
        column_choose = col
        item_prew = n_ui.group_table.item(row, col)
        if item_prew == None:
            n_ui.group_table.setItem(
                row, col, QTableWidgetItem(""))
        n_ui.group_table.clearSelection()
        item = n_ui.group_table.item(row, col)
        item.setSelected(True)
        return

    def rememberState():
        """
        Функция для сохранения всех введенных состояний студентов.
        """
        print("rememberState")
        nonlocal row_choose, column_choose, partial_state
        mark_choose = n_ui.group_table.item(row_choose, column_choose).text()
        if mark_choose == "":
            return
        faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[1]
        course_name = n_ui.year_list.currentItem().text()
        group_name = n_ui.group_list.currentItem().text().split(". ")[1]
        date_choose = n_ui.group_table.horizontalHeaderItem(
            column_choose).text()
        student_choose = n_ui.group_table.verticalHeaderItem(
            row_choose).text().split(". ")[1]
        try:
            partial_state[faculty_name]
        except:
            partial_state[faculty_name] = {}
        try:
            partial_state[faculty_name][course_name]
        except:
            partial_state[faculty_name][course_name] = {}
        try:
            partial_state[faculty_name][course_name][group_name]
        except:
            partial_state[faculty_name][course_name][group_name] = {}
        try:
            partial_state[faculty_name][course_name][group_name][date_choose]
        except:
            partial_state[faculty_name][course_name][group_name][date_choose] = {}
        partial_state[faculty_name][course_name][group_name][date_choose][student_choose] = mark_choose
        return

    if success:
        global tableWindow
        tableWindow = QtWidgets.QMainWindow()
        n_ui = Ui_table_window()
        n_ui.setupUi(tableWindow)
        tableWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        n_ui.group_table.horizontalHeaderItem(
            0).setFont(QFont("Gotham Lite", 12))
        n_ui.group_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed)
        n_ui.group_table.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Fixed)
        n_ui.group_table.setStyleSheet(
            n_ui.group_table.styleSheet() + "font: 12pt \"Gotham Lite\";\n")
        n_ui.error_label.hide()
        tableWindow.showMaximized()
        AuthWindow.close()

        # отображение факультета
        n_ui.faculty_list.clear()
        addFacultyItems()

        n_ui.faculty_list.currentItemChanged.connect(addYearItems)
        n_ui.year_list.currentItemChanged.connect(addGroupItems)
        n_ui.group_list.currentItemChanged.connect(addStudents)
        n_ui.group_list.currentItemChanged.connect(addDates)
        n_ui.group_list.currentItemChanged.connect(addStatuses)

        # обработка нажатия на клетку таблицы
        n_ui.group_table.cellClicked.connect(selectCell)

        # обработка нажатия на кнопку выхода
        n_ui.exit_button.clicked.connect(tableWindow.close)

        # обработка нажатия на кнопку распознавания голоса
        n_ui.activate_button.clicked.connect(activate_voice)

        # обработка нажатий на кнопки закрытия окна и сворачивания
        n_ui.hide_button.clicked.connect(tableWindow.showMinimized)
        n_ui.close_button.clicked.connect(tableWindow.close)

        n_ui.exit_button.setShortcut(QKeySequence("Ctrl+Q"))
        n_ui.activate_button.setShortcut(QKeySequence("Ctrl+Space"))

    else:
        ui.error_label.show()
        ui.login_lineEdit.setText("")
        ui.password_lineEdit.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AuthWindow = QtWidgets.QDialog()
    QtGui.QFontDatabase.addApplicationFont('gotham_black.otf')
    QtGui.QFontDatabase.addApplicationFont('gotham_light.otf')
    QtGui.QFontDatabase.addApplicationFont('gotham_medium.otf')
    app.setStyle('Fusion')
    ui.setupUi(AuthWindow)
    ui.error_label.hide()
    AuthWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    ui.hide_button_2.clicked.connect(AuthWindow.showMinimized)
    ui.close_button_2.clicked.connect(AuthWindow.close)
    AuthWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    AuthWindow.show()
    ui.exit_button.clicked.connect(AuthWindow.close)
    ui.auth_button.clicked.connect(new_win)
    dragPos = 0
    mouse_original_pos = 0

    def mousePress(event):
        global dragPos, mouse_original_pos
        dragPos = AuthWindow.pos()
        mouse_original_pos = AuthWindow.mapToGlobal(event.pos())

    def moveWindow(event):
        if AuthWindow.isMaximized():
            AuthWindow.showNormal()
        else:
            if event.buttons() == Qt.MouseButton.LeftButton:
                AuthWindow_last_pos = dragPos + \
                    AuthWindow.mapToGlobal(event.pos()) - mouse_original_pos
                AuthWindow.move(AuthWindow_last_pos)

    ui.title_bar.mouseMoveEvent = moveWindow
    ui.title_bar.mousePressEvent = mousePress
    AuthWindow.setWindowIcon(QtGui.QIcon('ProgrammIcon.ico'))
    sys.exit(app.exec())
