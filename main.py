from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from PyQt6.QtGui import QKeySequence, QFont
from PyQt6.QtCore import Qt
import Functions
import SR.recorder as recorder
import SR as Recognizer
from autorization import *
from table import *
import login_class
import ctypes
import resources
import json
import sys

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
    # auth.login(ui.login_lineEdit.text(),ui.password_lineEdit.text())

    def activate_voice():
        try:
            nonlocal table_cond, group_cond, year_cond, buttonActive
            assert not buttonActive
            buttonActive = True
            buttonColor(2)
            bytes_array = recorder.Recorder.record_data()
            buttonColor(1)
            words_list = Recognizer.speech(bytes_array, recorder.Recorder.freq)
            print(words_list)
            try:
                assert words_list
                # вызов функций по распознаванию команды
                nonlocal row_choose, column_choose
                command = Functions.speech_functions.choose_command(words_list)
                if command == 1:
                    addFacultyItems()
                elif command == 2 and year_cond:
                    addYearItems()
                elif command == 3 and group_cond:
                    addGroupItems()
                elif command == 4:
                    pass
                elif command == 5:
                    pass
                # ЕЩЕ НЕ ИЗМЕНЕНО
                elif table_cond:
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
                            n_ui.group_table.setItem(
                                row_choose, column_choose, QTableWidgetItem(" "))
                            select_cell(row_choose, column_choose)
                    else:
                        try:
                            number = Functions.speech_functions.convert_number.convert_string(
                                words_list[0])
                            if number != -1:
                                word = n_ui.group_table.verticalHeaderItem(
                                    number - 1).text()
                                words_list[0] = word.split(". ")[1]
                            student_selected = Functions.speech_functions.get_student_name(
                                words_list, faculty_name, course_name, group_name)
                            if student_selected:
                                studentChoose(student_selected)
                                n_ui.group_table.update()
                                QApplication.processEvents()
                                if row_choose != -1 and column_choose != -1:
                                    n_ui.group_table.setItem(
                                        row_choose, column_choose, QTableWidgetItem(" "))
                                    select_cell(row_choose, column_choose)
                            elif row_choose > -1 and column_choose > -1:
                                mark_choose = Functions.speech_functions.get_status(
                                    words_list)
                                if mark_choose:
                                    n_ui.group_table.setItem(
                                        row_choose, column_choose, QTableWidgetItem(mark_choose))
                        except (AttributeError):
                            n_ui.error_label.show()

                elif year_cond and group_cond:
                    course_choose = n_ui.year_list.currentItem().text()
                    faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[
                        1]
                    group_choose = Functions.speech_functions.get_group(
                        faculty_name, course_choose, words_list)
                    if group_choose:
                        n_ui.group_list.setCurrentRow(group_choose - 1)
                        addDates()
                        addStudents()
                    else:
                        n_ui.error_label.show()

                elif year_cond:
                    faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[
                        1]
                    course_choose = Functions.speech_functions.get_course(
                        faculty_name, words_list)
                    n_ui.year_list.setCurrentRow(course_choose - 1)
                    addGroupItems()

                else:
                    faculty_choose = Functions.speech_functions.get_faculty(
                        words_list)
                    if type(faculty_choose) != bool and faculty_choose:
                        n_ui.faculty_list.setCurrentRow(faculty_choose - 1)
                        addYearItems()
                    else:
                        n_ui.error_label.show()
            except AssertionError:
                n_ui.error_label.show()
            finally:
                n_ui.activate_button.setEnabled(True)
                buttonColor(3)
                n_ui.activate_button.update()
                QApplication.processEvents()
                buttonActive = False
        except AssertionError:
            pass

    def buttonColor(f):
        if f == 1:
            n_ui.activate_button.setText("Распознавание...")
            n_ui.activate_button.setIconSize(QtCore.QSize(0, 0))
            n_ui.activate_button.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                               "border-radius: 10px;\n"
                                               "")
            n_ui.activate_button.update()
            QApplication.processEvents()
        if f == 2:
            n_ui.activate_button.setText("Идёт запись...")
            n_ui.activate_button.setStyleSheet(
                "background-color: rgb(255, 0, 0);\n"
                "border-radius: 10px;\n"
                "")
            n_ui.activate_button.setIconSize(QtCore.QSize(0, 0))
            n_ui.activate_button.update()
            QApplication.processEvents()
        if f == 3:
            n_ui.activate_button.setIconSize(QtCore.QSize(35, 35))
            n_ui.activate_button.setText("Голосовой ввод")
            n_ui.activate_button.setShortcut(QKeySequence("Ctrl+Space"))
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
            n_ui.activate_button.update()
            QApplication.processEvents()

    def addFacultyItems():
        n_ui.faculty_list.clear()
        n_ui.faculty_list.clearSelection()
        n_ui.group_list.clear()
        n_ui.group_list.clear()
        n_ui.help_label.setText(
            "Примечание: для выбора факультета с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой "
            "ввод\" и назвать номер факультета, указанный в списке.")
        n_ui.error_label.hide()
        n_ui.help_label.update()
        QApplication.processEvents()
        n_ui.group_table.setRowCount(0)
        nonlocal group_cond, year_cond, table_cond
        group_cond = False
        year_cond = False
        table_cond = False
        faculties_list = Functions.request_functions.get_faculties()
        for num in range(len(faculties_list)):
            n_ui.faculty_list.addItem(
                (str)(num + 1) + ". " + faculties_list[num])
        return

    def addYearItems():
        try:
            n_ui.year_list.clear()
            n_ui.year_list.clearSelection()
            n_ui.group_list.clear()
            n_ui.help_label.setText(
                "Примечание: для выбора курса с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой "
                "ввод\" и назвать <b>порядковый</b> номер курса.")
            n_ui.error_label.hide()
            n_ui.help_label.update()
            QApplication.processEvents()
            n_ui.group_table.setRowCount(0)
            nonlocal group_cond
            nonlocal table_cond
            table_cond = False
            group_cond = False
            current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[
                1]
            courses_list = Functions.request_functions.get_courses(
                current_faculty)
            for item in courses_list:
                n_ui.year_list.addItem(item)
            nonlocal year_cond
            year_cond = True
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            return False

    def addGroupItems():
        try:
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
            n_ui.error_label.hide()
            QApplication.processEvents()
            n_ui.help_label.update()
            n_ui.group_table.setRowCount(0)
            i = 0
            current_faculty = n_ui.faculty_list.currentItem().text().split(". ")[
                1]
            current_course = n_ui.year_list.currentItem().text()
            groups_list = Functions.request_functions.get_groups(
                current_faculty, current_course)
            for item in groups_list:
                i += 1
                n_ui.group_list.addItem(str(i) + ". " + item)
            nonlocal table_cond
            table_cond = False
            nonlocal group_cond
            group_cond = True
            n_ui.help_label.setText(
                "Примечание: для выбора группы с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой "
                "ввод\" и назвать номер группы, указанный в списке.")
            if i == 0:
                n_ui.help_label.setText(
                    "Примечание: на данном курсе нет групп, выберете другую!")
                n_ui.help_label.update()
                QApplication.processEvents()
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
                group_cond = False
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            n_ui.error_label.show()
            return False

    def addDates():
        pass

    def addStudents():
        try:
            nonlocal table_cond
            n_ui.help_label.setText(
                "Примечание: для выбора учащегося с помощью голосовых команд вам необходимо нажать на кнопку "
                "\"Голосовой ввод\" и назвать дату, фамилию, а затем оценку для студента.")
            n_ui.error_label.hide()
            n_ui.help_label.update()
            QApplication.processEvents()
            n_ui.group_table.setRowCount(0)
            faculty_name = n_ui.faculty_list.currentItem().text().split(". ")[
                1]
            course_name = n_ui.year_list.currentItem().text()
            group_name = n_ui.group_list.currentItem().text().split(". ")[1]
            students_list = Functions.request_functions.get_students(
                faculty_name, course_name, group_name)
            n_ui.group_table.setRowCount(len(students_list))
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
            n_ui.group_table.setVerticalHeaderLabels(students_list)
            for i in range(len(students_list)):
                n_ui.group_table.verticalHeaderItem(i).setText(
                    str(i + 1) + ". " + n_ui.group_table.verticalHeaderItem(i).text())
            table_cond = True
            nonlocal column_choose
            column_choose = -1
            nonlocal row_choose
            row_choose = -1
            if n_ui.group_table.rowCount() == 1:
                studentChoose(n_ui.group_table.verticalHeaderItem(
                    0).text().split(". ")[1])
                row_choose = 0

        except KeyError:
            n_ui.help_label.setText(
                "Примечание: в данной группе нет студентов, выберете другую!")
            n_ui.help_label.update()
            QApplication.processEvents()
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
            table_cond = False
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            return False

    def studentChoose(name):
        number = n_ui.group_table.verticalHeader().count()
        index = -1
        for i in range(number):
            if name == n_ui.group_table.verticalHeaderItem(i).text().split(". ")[1]:
                index = i
                break
        if index == -1:
            return
        n_ui.group_table.selectRow(index)
        nonlocal row_choose
        row_choose = index
        n_ui.group_table.clearSelection()
        if column_choose == -1:
            for i in range(n_ui.group_table.horizontalHeader().count()):
                n_ui.group_table.setItem(
                    row_choose, i, QTableWidgetItem(""))
                item = n_ui.group_table.item(row_choose, i)
                item.setSelected(True)
                n_ui.activate_button.update()
                QApplication.processEvents()

    def rowActivated():
        nonlocal column_choose
        column_choose = n_ui.group_table.currentColumn()
        n_ui.group_table.selectColumn(column_choose)
        if row_choose != -1 and column_choose != -1:
            n_ui.group_table.setItem(
                row_choose, column_choose, QTableWidgetItem(" "))
            select_cell(row_choose, column_choose)

    def dateChoose(date):
        number = n_ui.group_table.horizontalHeader().count()
        index = -1
        n_ui.group_table.clearSelection()
        for i in range(number):
            if date + "2023" == n_ui.group_table.horizontalHeaderItem(i).text():
                index = i
                break
        if index == -1:
            return
        n_ui.group_table.selectColumn(index)
        nonlocal column_choose
        column_choose = index
        if row_choose == -1:
            for i in range(n_ui.group_table.verticalHeader().count()):
                n_ui.group_table.setItem(
                    i, column_choose, QTableWidgetItem(""))
                item = n_ui.group_table.item(i, column_choose)
                item.setSelected(True)
                n_ui.activate_button.update()
                QApplication.processEvents()

    def columnActivated():
        nonlocal row_choose
        row_choose = n_ui.group_table.currentRow()
        if row_choose != -1 and column_choose != -1:
            n_ui.group_table.setItem(
                row_choose, column_choose, QTableWidgetItem(" "))
            select_cell(row_choose, column_choose)

    def select_cell(row_index, column_index):
        item = n_ui.group_table.item(row_index, column_index)
        n_ui.group_table.clearSelection()
        item.setSelected(True)
        n_ui.group_table.setItem(
            row_choose, column_choose, QTableWidgetItem(""))

    def cellCoord():
        nonlocal column_choose, row_choose
        column_choose = n_ui.group_table.currentColumn()
        row_choose = n_ui.group_table.currentRow()

    def cellActivated():
        nonlocal column_choose, row_choose
        column_choose = n_ui.group_table.currentColumn()
        row_choose = n_ui.group_table.currentRow()
        n_ui.group_table.setItem(
            row_choose, column_choose, QTableWidgetItem(" "))
        pass

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
        n_ui.faculty_list.clear()

        addFacultyItems()

        n_ui.group_table.cellClicked.connect(cellCoord)
        n_ui.group_table.horizontalHeader().sectionClicked.connect(rowActivated)
        n_ui.group_table.verticalHeader().sectionClicked.connect(columnActivated)
        n_ui.group_table.cellClicked.connect(cellActivated)
        n_ui.exit_button.clicked.connect(tableWindow.close)
        n_ui.faculty_list.currentItemChanged.connect(addYearItems)
        n_ui.activate_button.clicked.connect(activate_voice)
        n_ui.hide_button.clicked.connect(tableWindow.showMinimized)
        n_ui.close_button.clicked.connect(tableWindow.close)
        n_ui.exit_button.setShortcut(QKeySequence("Ctrl+Q"))
        n_ui.activate_button.setShortcut(QKeySequence("Ctrl+Space"))
        n_ui.year_list.currentItemChanged.connect(addGroupItems)
        n_ui.group_list.currentItemChanged.connect(addStudents)
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
