from PyQt6.QtCore import Qt, QItemSelectionModel
from PyQt6.QtGui import QKeySequence, QFont
from PyQt6.QtWidgets import QApplication, QTableWidgetItem

import time
import login_class
from autorization import *
from table import *
import json
import SR
import SR.recorder as recorder
import icons


ui = Ui_AuthWindow()
def new_win():
    year_cond = False
    group_cond = False
    table_cond = False
    column_choose = -1
    row_choose = -1
    faculty_name = ""
    course_choose = ""
    auth = login_class.LogIn()
    success = True
    #auth.login(ui.login_lineEdit.text(),ui.password_lineEdit.text())
    with open('data.json', "r", encoding="UTF-8") as f:
        var = json.load(f)
    with open('students_list.json', "r", encoding="UTF-8") as s_f:
        s_var = json.load(s_f)
    # def movewindow(event):
    #     if MainWindow.isMaximized()== False:
    #         print(event.buttons)
    #         if event.button() == Qt.MouseButton.RightButton:
    #             MainWindow.move(MainWindow.pos() + event.globalPos() - MainWindow.clickPosition)
    #             MainWindow.clickPosition = event.globalPos()
    #             event.accept()
    # def mouseclickevent(event):
    #     clickPosition = event.globalPos()
    def addGroupItems():
        n_ui.help_label.setText("Примечание: для выбора группы с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать номер номер группы, указанный в списке.")
        n_ui.error_label.hide()
        n_ui.group_list.clear()
        print(n_ui.year_list.currentItem().text())
        i = 0
        for key in var[n_ui.faculty_list.currentItem().text()][n_ui.year_list.currentItem().text()]:
             i+=1
             n_ui.group_list.addItem(str(i) + ". " + key)
        nonlocal table_cond
        table_cond = False
        nonlocal group_cond
        group_cond = True

    def addYearItems():
        n_ui.help_label.setText("Примечание: для выбора курса с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать <b>порядковый</b> номер курса.")
        n_ui.error_label.hide()
        n_ui.year_list.clear()
        n_ui.group_list.clear()
        nonlocal group_cond
        nonlocal table_cond
        table_cond = False
        group_cond = False
        for key in var[n_ui.faculty_list.currentItem().text()]:
             n_ui.year_list.addItem(key)
        nonlocal year_cond
        year_cond = True

    def addStudents():
        try:
            nonlocal table_cond
            n_ui.help_label.setText(
                "Примечание: для выбора учащегося с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать дату, фамилию, а затем оценку для студента.")
            n_ui.error_label.hide()
            n_ui.group_table.setRowCount(0)
            current = n_ui.group_list.currentItem().text()
            current = current.split('. ')[1]
            n_ui.group_table.setRowCount(len(s_var[current]))
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
            n_ui.group_table.setVerticalHeaderLabels(s_var[current])
            table_cond = True
            nonlocal column_choose
            column_choose = -1
            nonlocal row_choose
            row_choose = -1
        except KeyError:
            print(current)
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
            print("Такой группы нет!")
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            return False
    def select_cell(row_index,column_index):
        item = n_ui.group_table.item(row_index,column_index)
        n_ui.group_table.clearSelection()
        # n_ui.group_table.setItem(row_index, column_index, QTableWidgetItem("1"))
        # if item.text() != " ":
        #     print(111111111)
        #     n_ui.group_table.setItem(row_index,column_index,QTableWidgetItem(" "))
        # print(item.text())
        item.setSelected(True)
        n_ui.group_table.setItem(row_choose, column_choose, QTableWidgetItem(""))
        # if item.text() == " ":
        #     n_ui.group_table.setItem(row_index,column_index,QTableWidgetItem(""))
        # print(item.text())
        # index = n_ui.group_table.model().index(row_index,column_index)
        # n_ui.group_table.selectionModel().select(index,QItemSelectionModel.select())
        # n_ui.group_table.item(row_index,column_index)
    def studentChoose(name):
        number = n_ui.group_table.verticalHeader().count()
        index = -1
        for i in range(number):
            if name == n_ui.group_table.verticalHeaderItem(i).text():
                index = i
                break
        if index == -1:
            return
        n_ui.group_table.selectRow(index)
        nonlocal row_choose
        row_choose = index
    def dateChoose(date):
        print(1)
        print(date)
        number = n_ui.group_table.horizontalHeader().count()
        index = -1
        for i in range(number):
            if date + "2023" == n_ui.group_table.horizontalHeaderItem(i).text():
                index = i
                break
        if index == -1:
            print(2)
            return
        print(3)
        n_ui.group_table.selectColumn(index)
        nonlocal column_choose
        column_choose = index

    def buttonColor(f):
        if f ==1:
            n_ui.activate_button.setText("Распознавание...")
            n_ui.activate_button.setIconSize(QtCore.QSize(0, 0))
            n_ui.activate_button.setStyleSheet("QPushButton::hover{\n"
                                               "background-color: rgb(255, 255, 0);\n"
                                               "}\n"
                                               "QPushButton{\n"
                                               "color: rgb(0, 0, 0);\n"
                                               "border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               "")
        if f ==2:
            n_ui.activate_button.setText("Идёт запись...")
            n_ui.activate_button.setStyleSheet(
                                                 "background-color: rgb(255, 29, 40);\n"
                                                 "border-radius: 10px;\n"
                                                 "")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(":/in programm/icons/Mic.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            n_ui.activate_button.setIcon(icon1)
            n_ui.activate_button.setIconSize(QtCore.QSize(0, 0))
        if f ==3:
            n_ui.activate_button.setIconSize(QtCore.QSize(35, 35))
            n_ui.activate_button.setText("Голосовой ввод")
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
    # def reset_lists():
    #     nonlocal year_cond
    #     nonlocal group_cond
    #     n_ui.help_label.setText("Примечание: для выбора факультета с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать номер факультета, указанный в списке.")
    #     n_ui.group_list.clear()
    #     year_cond = False
    #     group_cond = False
    #     n_ui.year_list.clear()
    #     n_ui.faculty_list.clearSelection()
    #     n_ui.group_table.setRowCount(0)
    def activate_voice():
        nonlocal faculty_name, course_choose, table_cond
        buttonColor(2)
        n_ui.activate_button.update()
        QApplication.processEvents()
        bytes_array = recorder.Recorder.record_data()
        buttonColor(1)
        n_ui.activate_button.update()
        QApplication.processEvents()
        try:
            nonlocal row_choose, column_choose
            if table_cond:
                date_choose = SR.get_date(bytes_array, recorder.Recorder.freq)
                if type(date_choose) != bool:
                    dateChoose(date_choose)
                    if row_choose != -1 and column_choose != -1:
                        n_ui.group_table.setItem(row_choose, column_choose, QTableWidgetItem(" "))
                        select_cell(row_choose,column_choose)
                else:
                    current = n_ui.group_list.currentItem().text()
                    current = current.split('. ')[1]
                    student_list = s_var[current]
                    student_selected = SR.get_student_name(student_list, bytes_array, recorder.Recorder.freq)
                    if type(student_selected) != bool:
                        studentChoose(student_selected)
                        if row_choose != -1 and column_choose != -1:
                            n_ui.group_table.setItem(row_choose, column_choose, QTableWidgetItem(" "))
                            select_cell(row_choose,column_choose)
                    else:
                        pass
            elif year_cond and group_cond:
                group_choose = SR.get_group(faculty_name, str(course_choose), bytes_array, recorder.Recorder.freq)
                if type(group_choose) != bool and group_choose + 1:
                    n_ui.group_list.setCurrentRow(group_choose-1)
                    addStudents()
                else:
                    n_ui.error_label.show()
            elif year_cond:
                course_choose = SR.get_course(faculty_name, bytes_array, recorder.Recorder.freq)
                if type(course_choose) != bool and course_choose + 1:
                    n_ui.year_list.setCurrentRow(course_choose-1)
                    addGroupItems()
                else:
                    n_ui.error_label.show()
            else:
                faculty_choose, faculty_name = SR.get_faculty(bytes_array, recorder.Recorder.freq)
                print(faculty_name)
                if type(faculty_choose) != bool and faculty_choose + 1:
                    n_ui.faculty_list.setCurrentRow(faculty_choose-1)
                    addYearItems()
                else:
                    n_ui.error_label.show()
        finally:
            buttonColor(3)
            n_ui.activate_button.update()
            QApplication.processEvents()

    def fade():
        for i in range(100):
            i = i / 10
            tableWindow.setWindowOpacity(1 - i)
            time.sleep(0.05)
        tableWindow.showMinimized

    if success:
        global tableWindow
        tableWindow = QtWidgets.QMainWindow()
        n_ui = Ui_table_window()
        n_ui.setupUi(tableWindow)
        tableWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        n_ui.group_table.horizontalHeaderItem(0).setFont(QFont("Gotham Lite", 12))
        n_ui.group_table.setStyleSheet(n_ui.group_table.styleSheet() + "font: 12pt \"Gotham Lite\";\n")
        n_ui.error_label.hide()
        tableWindow.showMaximized()
        MainWindow.close()
        n_ui.faculty_list.clear()

        for key in var:
            n_ui.faculty_list.addItem(key)
            n_ui.faculty_list.clearSelection()
            # reset_lists()

        n_ui.faculty_list.clearSelection()
        n_ui.activate_button.setShortcut(QKeySequence("Ctrl+W"))
        n_ui.exit_button.clicked.connect(tableWindow.close)
        n_ui.faculty_list.itemClicked.connect(addYearItems)
        n_ui.activate_button.clicked.connect(activate_voice)
        n_ui.hide_button.clicked.connect(tableWindow.showMinimized)
        #tableWindow.showMinimized
        # n_ui.reset_button.clicked.connect(reset_lists)
        n_ui.close_button.clicked.connect(tableWindow.close)
        n_ui.exit_button.setShortcut(QKeySequence("Ctrl+Q"))
        n_ui.year_list.itemClicked.connect(addGroupItems)
        n_ui.group_list.itemClicked.connect(addStudents)
    else:
        ui.error_label.show()
        ui.login_lineEdit.setText("")
        ui.password_lineEdit.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    app.setStyle('Fusion')
    ui.setupUi(MainWindow)
    ui.error_label.hide()
    ui.hide_button_2.clicked.connect(MainWindow.showMinimized)
    ui.close_button_2.clicked.connect(MainWindow.close)
    MainWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    MainWindow.show()

    ui.exit_button.clicked.connect(MainWindow.close)
    ui.auth_button.clicked.connect(new_win)


    sys.exit(app.exec())
