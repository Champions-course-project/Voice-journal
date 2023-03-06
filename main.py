from autorization import *
from table import *
import json
import rc_rc


ui = Ui_AuthWindow()

def new_win():
    with open('data.json', "r", encoding="utf-8") as f:
        var = json.load(f)
    with open('students_list.json', "r", encoding="utf-8") as s_f:
        s_var = json.load(s_f)

    def addGroupItems():
        n_ui.group_list.clear()
        for key in var[n_ui.faculty_list.currentItem().text()][n_ui.year_list.currentItem().text()]:
             n_ui.group_list.addItem(key)
    def addYearItems():
        n_ui.year_list.clear()
        n_ui.group_list.clear()
        for key in var[n_ui.faculty_list.currentItem().text()]:
             n_ui.year_list.addItem(key)

    def addStudents():
        try:
            n_ui.group_table.setRowCount(len(s_var[n_ui.group_list.currentItem().text()]))
            n_ui.group_table.setVerticalHeaderLabels(s_var[n_ui.group_list.currentItem().text()])
        except KeyError:
            print("Такой группы нет!")

    if ui.login_lineEdit.text() == "1" and ui.password_lineEdit.text() == "1":
        global tableWindow
        tableWindow = QtWidgets.QMainWindow()
        n_ui = Ui_table_window()
        n_ui.setupUi(tableWindow)
        tableWindow.showMaximized()
        MainWindow.close()
        n_ui.faculty_list.clear()

        for key in var:
            n_ui.faculty_list.addItem(key)

        n_ui.exit_button.clicked.connect(tableWindow.close)
        n_ui.faculty_list.itemClicked.connect(addYearItems)
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
    ui.setupUi(MainWindow)
    ui.error_label.hide()
    MainWindow.show()
    ui.exit_button.clicked.connect(MainWindow.close)
    ui.auth_button.clicked.connect(new_win)


    sys.exit(app.exec())
