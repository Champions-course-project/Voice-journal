from autorization import *
from table import *
import rc_rc

ui = Ui_AuthWindow()


def new_win():
    def addGroupItems():
        if  n_ui.year_list.currentItem().text() == "2":
            n_ui.group_list.clear()
            groupItems = ["АБД(м)-11", "ИС(б)-11", "ИСС(б)-11", "КСТ(б)-11", "КСТ(м)-11", "ОНГ(б)-11", "ОНГ(м)-11", "ТХОМ(б)-11", "УИТС(б)-11", "УК(б)-11", "УК(м)-11"]
            for i in range(len(groupItems)):
                n_ui.group_list.addItem(groupItems[i])
    def addYearItems():
        if n_ui.faculty_list.currentItem().text() == "ФАИТ":
            n_ui.year_list.clear()
            yearItems = ["1", "2", "3", "4", "5", "6"]
            for i in range(6):
                n_ui.year_list.addItem(yearItems[i])

    if ui.login_lineEdit.text() == "1" and ui.password_lineEdit.text() == "1":
        global tableWindow
        tableWindow = QtWidgets.QMainWindow()
        n_ui = Ui_table_window()
        n_ui.setupUi(tableWindow)
        tableWindow.showMaximized()
        MainWindow.close()
        n_ui.exit_button.clicked.connect(tableWindow.close)
        n_ui.faculty_list.itemClicked.connect(addYearItems)
        n_ui.year_list.itemClicked.connect(addGroupItems)
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
