from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QApplication

import login_class
from autorization import *
from table import *
import json
import SR
import icons

ui = Ui_AuthWindow()
def new_win():
    year_cond = False
    group_cond = False
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
        nonlocal group_cond
        group_cond = True

    def addYearItems():
        n_ui.help_label.setText("Примечание: для выбора курса с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать <b>порядковый</b> номер курса.")
        n_ui.error_label.hide()
        n_ui.year_list.clear()
        n_ui.group_list.clear()
        nonlocal group_cond
        group_cond = False
        for key in var[n_ui.faculty_list.currentItem().text()]:
             n_ui.year_list.addItem(key)
        nonlocal year_cond
        year_cond = True

    def addStudents():
        try:
            n_ui.help_label.setText(
                "Примечание: для выбора учащегося с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать дату, фамилию, а затем оценку для студента.")
            n_ui.error_label.hide()
            n_ui.group_table.setRowCount(0)
            current = n_ui.group_list.currentItem().text()
            current = current.split('. ')[1]
            n_ui.group_table.setRowCount(len(s_var[current]))
            n_ui.group_list.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "selection-color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(83, 83, 83);\n"
                                          "selection-background-color: rgb(30, 185, 85);\n"
                                          "border-radius: 10px;\n"
                                          "")
            n_ui.group_table.setVerticalHeaderLabels(s_var[current])
        except KeyError:
            print(current)
            n_ui.group_list.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "selection-color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(83, 83, 83);\n"
                                           "selection-background-color: rgb(255, 29, 40);\n"
                                          "border-radius: 10px;\n"
                                           "")
            print("Такой группы нет!")
        except Exception as exc:
            print(type(exc).__name__)
            print(exc.args)
            return False

    def activate_voice():
        nonlocal faculty_name, course_choose
        n_ui.activate_button.hide()
        n_ui.activate_button.update()
        QApplication.processEvents()
        try:
            if year_cond and group_cond:
                group_choose = SR.get_group(faculty_name, str(course_choose))
                if type(group_choose) != bool and group_choose + 1:
                    n_ui.group_list.setCurrentRow(group_choose-1)
                    addStudents()
                else:
                    n_ui.error_label.show()
            elif year_cond:
                course_choose = SR.get_course(faculty_name)
                if type(course_choose) != bool and course_choose + 1:
                    n_ui.year_list.setCurrentRow(course_choose-1)
                    addGroupItems()
                else:
                    n_ui.error_label.show()
            else:
                faculty_choose, faculty_name = SR.get_faculty()
                if type(faculty_choose) != bool and faculty_choose + 1:
                    n_ui.faculty_list.setCurrentRow(faculty_choose-1)
                    addYearItems()
                else:
                    n_ui.error_label.show()
        finally:
            n_ui.activate_button.show()
            n_ui.activate_button.update()
            QApplication.processEvents()

    if success:
        global tableWindow
        tableWindow = QtWidgets.QMainWindow()
        n_ui = Ui_table_window()
        n_ui.setupUi(tableWindow)
        tableWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        n_ui.error_label.hide()
        tableWindow.showMaximized()
        MainWindow.close()
        n_ui.faculty_list.clear()

        for key in var:
            n_ui.faculty_list.addItem(key)
        n_ui.exit_button.clicked.connect(tableWindow.close)
        n_ui.faculty_list.itemClicked.connect(addYearItems)
        n_ui.activate_button.clicked.connect(activate_voice)
        n_ui.hide_button.clicked.connect(tableWindow.showMinimized)
        n_ui.close_button.clicked.connect(tableWindow.close)
        n_ui.activate_button.setShortcut(QKeySequence("Ctrl+Space"))
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
