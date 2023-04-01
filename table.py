# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFontDatabase


class Ui_table_window(object):
    def setupUi(self, table_window):
        table_window.setObjectName("table_window")
        table_window.resize(1933, 1032)
        font = QtGui.QFont()
        QFontDatabase.addApplicationFont("gotham_black.otf")
        QFontDatabase.addApplicationFont("gotham_medium.otf")
        font.setFamily("Gotham Black")
        font.setBold(True)
        font.setWeight(75)
        table_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ProgrammIcon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        table_window.setWindowIcon(icon)
        table_window.setAutoFillBackground(False)
        table_window.setStyleSheet("background-color: rgb(17, 17, 17);")
        table_window.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonFollowStyle)
        table_window.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=table_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 160, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.faculty_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.faculty_layout.setContentsMargins(0, 0, 0, 0)
        self.faculty_layout.setObjectName("faculty_layout")
        self.faculty_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.faculty_label.setFont(font)
        self.faculty_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.faculty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.faculty_label.setObjectName("faculty_label")
        self.faculty_layout.addWidget(self.faculty_label)
        self.faculty_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(16)
        self.faculty_list.setFont(font)
        self.faculty_list.setMouseTracking(False)
        self.faculty_list.setTabletTracking(False)
        self.faculty_list.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.faculty_list.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.faculty_list.setAcceptDrops(False)
        self.faculty_list.setStyleSheet("QListWidget{\n"
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
        self.faculty_list.setAutoScroll(False)
        self.faculty_list.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.faculty_list.setProperty("showDropIndicator", False)
        self.faculty_list.setDragEnabled(False)
        self.faculty_list.setDragDropOverwriteMode(False)
        self.faculty_list.setDefaultDropAction(QtCore.Qt.DropAction.CopyAction)
        self.faculty_list.setAlternatingRowColors(False)
        self.faculty_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.faculty_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.faculty_list.setMovement(QtWidgets.QListView.Movement.Static)
        self.faculty_list.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.faculty_list.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.faculty_list.setObjectName("faculty_list")
        self.faculty_layout.addWidget(self.faculty_list)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 70, 161, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.year_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.year_layout.setContentsMargins(0, 0, 0, 0)
        self.year_layout.setObjectName("year_layout")
        self.year_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.year_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.year_layout.addWidget(self.year_label)
        self.year_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(16)
        self.year_list.setFont(font)
        self.year_list.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.year_list.setStyleSheet("QListWidget{\n"
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
        self.year_list.setAutoScroll(True)
        self.year_list.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.year_list.setProperty("showDropIndicator", False)
        self.year_list.setObjectName("year_list")
        self.year_layout.addWidget(self.year_list)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 70, 211, 531))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.group_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setObjectName("group_layout")
        self.groupe_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupe_label.setFont(font)
        self.groupe_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.groupe_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupe_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupe_label.setObjectName("groupe_label")
        self.group_layout.addWidget(self.groupe_label)
        self.group_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(16)
        self.group_list.setFont(font)
        self.group_list.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.group_list.setStyleSheet("QListWidget{\n"
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
        self.group_list.setObjectName("group_list")
        self.group_layout.addWidget(self.group_list)
        self.group_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.group_table.setEnabled(True)
        self.group_table.setGeometry(QtCore.QRect(650, 110, 1241, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_table.sizePolicy().hasHeightForWidth())
        self.group_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.group_table.setFont(font)
        self.group_table.setMouseTracking(True)
        self.group_table.setTabletTracking(False)
        self.group_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.group_table.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.group_table.setAcceptDrops(False)
        self.group_table.setAutoFillBackground(True)
        self.group_table.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"font: 25 12pt \"Gotham Light\";\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(30, 185, 85);\n"
"alternate-background-color: rgb(179, 179, 179);\n"
"gridline-color: rgb(17, 17, 17);")
        self.group_table.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.group_table.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.group_table.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.group_table.setLineWidth(0)
        self.group_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.group_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.group_table.setTabKeyNavigation(False)
        self.group_table.setProperty("showDropIndicator", False)
        self.group_table.setDragEnabled(False)
        self.group_table.setDragDropOverwriteMode(False)
        self.group_table.setAlternatingRowColors(True)
        self.group_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.group_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.group_table.setTextElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.group_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.group_table.setShowGrid(True)
        self.group_table.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.group_table.setWordWrap(False)
        self.group_table.setCornerButtonEnabled(False)
        self.group_table.setObjectName("group_table")
        self.group_table.setColumnCount(16)
        self.group_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        item.setFont(font)
        self.group_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(15, item)
        self.table_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.table_label.setGeometry(QtCore.QRect(1090, 70, 361, 32))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.table_label.setFont(font)
        self.table_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.table_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.table_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_label.setObjectName("table_label")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setEnabled(True)
        self.error_label.setGeometry(QtCore.QRect(1110, 870, 331, 32))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.help_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.help_label.setGeometry(QtCore.QRect(650, 880, 351, 141))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        self.help_label.setFont(font)
        self.help_label.setStyleSheet("color: rgb(140, 140, 140);")
        self.help_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.help_label.setWordWrap(True)
        self.help_label.setObjectName("help_label")
        self.title_bar = QtWidgets.QFrame(parent=self.centralwidget)
        self.title_bar.setGeometry(QtCore.QRect(-10, 0, 1951, 31))
        self.title_bar.setMouseTracking(True)
        self.title_bar.setTabletTracking(False)
        self.title_bar.setAcceptDrops(True)
        self.title_bar.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.close_button = QtWidgets.QPushButton(parent=self.title_bar)
        self.close_button.setGeometry(QtCore.QRect(1890, 0, 41, 31))
        self.close_button.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/window/icons/close_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QtCore.QSize(13, 13))
        self.close_button.setObjectName("close_button")
        self.hide_button = QtWidgets.QPushButton(parent=self.title_bar)
        self.hide_button.setGeometry(QtCore.QRect(1840, 0, 41, 31))
        self.hide_button.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(121, 121, 121);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.hide_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/window/icons/hide_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.hide_button.setIcon(icon2)
        self.hide_button.setIconSize(QtCore.QSize(25, 25))
        self.hide_button.setObjectName("hide_button")
        self.context_help = QtWidgets.QLabel(parent=self.centralwidget)
        self.context_help.setGeometry(QtCore.QRect(30, 650, 591, 361))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(18)
        self.context_help.setFont(font)
        self.context_help.setStyleSheet("color: rgb(140, 140, 140);")
        self.context_help.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.context_help.setWordWrap(True)
        self.context_help.setObjectName("context_help")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1160, 930, 751, 73))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutWidget.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.activate_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.activate_button.setEnabled(True)
        self.activate_button.setMinimumSize(QtCore.QSize(231, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.activate_button.setFont(font)
        self.activate_button.setMouseTracking(True)
        self.activate_button.setTabletTracking(True)
        self.activate_button.setAutoFillBackground(False)
        self.activate_button.setStyleSheet("QPushButton::hover{\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/in programm/icons/Mic.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.activate_button.setIcon(icon3)
        self.activate_button.setIconSize(QtCore.QSize(35, 35))
        self.activate_button.setAutoDefault(True)
        self.activate_button.setDefault(True)
        self.activate_button.setObjectName("activate_button")
        self.horizontalLayout.addWidget(self.activate_button)
        spacerItem = QtWidgets.QSpacerItem(58, 17, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exit_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setMinimumSize(QtCore.QSize(101, 49))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton::hover{\n"
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
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        table_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(table_window)
        QtCore.QMetaObject.connectSlotsByName(table_window)

    def retranslateUi(self, table_window):
        _translate = QtCore.QCoreApplication.translate
        table_window.setWindowTitle(_translate("table_window", "Voice journal"))
        self.faculty_label.setText(_translate("table_window", "Факультет"))
        self.year_label.setText(_translate("table_window", "Курс"))
        self.groupe_label.setText(_translate("table_window", "Группа"))
        self.group_table.setSortingEnabled(False)
        item = self.group_table.horizontalHeaderItem(0)
        item.setText(_translate("table_window", "14.01.2023"))
        item = self.group_table.horizontalHeaderItem(1)
        item.setText(_translate("table_window", "21.01.2023"))
        item = self.group_table.horizontalHeaderItem(2)
        item.setText(_translate("table_window", "28.01.2023"))
        item = self.group_table.horizontalHeaderItem(3)
        item.setText(_translate("table_window", "04.02.2023"))
        item = self.group_table.horizontalHeaderItem(4)
        item.setText(_translate("table_window", "11.02.2023"))
        item = self.group_table.horizontalHeaderItem(5)
        item.setText(_translate("table_window", "18.02.2023"))
        item = self.group_table.horizontalHeaderItem(6)
        item.setText(_translate("table_window", "25.02.2023"))
        item = self.group_table.horizontalHeaderItem(7)
        item.setText(_translate("table_window", "04.03.2023"))
        item = self.group_table.horizontalHeaderItem(8)
        item.setText(_translate("table_window", "11.03.2023"))
        item = self.group_table.horizontalHeaderItem(9)
        item.setText(_translate("table_window", "18.03.2023"))
        item = self.group_table.horizontalHeaderItem(10)
        item.setText(_translate("table_window", "25.03.2023"))
        item = self.group_table.horizontalHeaderItem(11)
        item.setText(_translate("table_window", "01.04.2023"))
        item = self.group_table.horizontalHeaderItem(12)
        item.setText(_translate("table_window", "08.04.2023"))
        item = self.group_table.horizontalHeaderItem(13)
        item.setText(_translate("table_window", "15.04.2023"))
        item = self.group_table.horizontalHeaderItem(14)
        item.setText(_translate("table_window", "22.04.2023"))
        item = self.group_table.horizontalHeaderItem(15)
        item.setText(_translate("table_window", "29.05.2023"))
        self.table_label.setText(_translate("table_window", "Журнал обучающихся"))
        self.error_label.setText(_translate("table_window", "Ошибка ввода, попробуйте еще раз"))
        self.help_label.setText(_translate("table_window", "Примечание: для выбора факультета с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать номер факультета, указанный в списке."))
        self.context_help.setText(_translate("table_window", "Список голосовых команд:\n"
"\"Выбрать факультет\"\n"
"\"Выбрать курс\" \n"
"\"Выбрать группу\"\n"
"\"Сохранить\"\n"
"\"Отменить\""))
        self.activate_button.setToolTip(_translate("table_window", "<html><head/><body><p><span style=\" color:#ffffff;\">Hotkey - Ctrl + Space</span></p></body></html>"))
        self.activate_button.setWhatsThis(_translate("table_window", "<html><head/><body><p>Hotkey - Ctrl + Space</p></body></html>"))
        self.activate_button.setText(_translate("table_window", "Голосовой ввод"))
        self.exit_button.setToolTip(_translate("table_window", "<html><head/><body><p><span style=\" color:#ffffff;\">Hotkey - Ctrl + Q</span></p></body></html>"))
        self.exit_button.setWhatsThis(_translate("table_window", "<html><head/><body><p>Hotkey - Ctrl + Q</p></body></html>"))
        self.exit_button.setText(_translate("table_window", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    table_window = QtWidgets.QMainWindow()
    ui = Ui_table_window()
    ui.setupUi(table_window)
    table_window.show()
    sys.exit(app.exec())
