# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_table_window(object):
    def setupUi(self, table_window):
        table_window.setObjectName("table_window")
        table_window.setEnabled(True)
        table_window.resize(1849, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(table_window.sizePolicy().hasHeightForWidth())
        table_window.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setBold(True)
        font.setWeight(75)
        table_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("output/main/ProgrammIcon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        table_window.setWindowIcon(icon)
        table_window.setAutoFillBackground(False)
        table_window.setStyleSheet("background-color: rgb(17, 17, 17);")
        table_window.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=table_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 25)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.title_bar = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMouseTracking(True)
        self.title_bar.setTabletTracking(False)
        self.title_bar.setAcceptDrops(True)
        self.title_bar.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.hide_button = QtWidgets.QPushButton(parent=self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hide_button.sizePolicy().hasHeightForWidth())
        self.hide_button.setSizePolicy(sizePolicy)
        self.hide_button.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(121, 121, 121);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"")
        self.hide_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/window/icons/hide_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.hide_button.setIcon(icon1)
        self.hide_button.setIconSize(QtCore.QSize(25, 25))
        self.hide_button.setObjectName("hide_button")
        self.horizontalLayout_4.addWidget(self.hide_button)
        self.close_button = QtWidgets.QPushButton(parent=self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"border-radius: 0px;\n"
"}\n"
"")
        self.close_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/window/icons/close_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setIconSize(QtCore.QSize(13, 13))
        self.close_button.setAutoDefault(False)
        self.close_button.setFlat(False)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_4.addWidget(self.close_button)
        self.horizontalLayout_4.setStretch(0, 90)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        self.verticalLayout_8.addWidget(self.title_bar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(19, -1, 19, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.faculty_label = QtWidgets.QLabel(parent=self.centralwidget)
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
        self.verticalLayout_4.addWidget(self.faculty_label)
        self.faculty_list = QtWidgets.QListWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_list.sizePolicy().hasHeightForWidth())
        self.faculty_list.setSizePolicy(sizePolicy)
        self.faculty_list.setMinimumSize(QtCore.QSize(158, 0))
        self.faculty_list.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(16)
        self.faculty_list.setFont(font)
        self.faculty_list.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
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
        self.faculty_list.setObjectName("faculty_list")
        self.verticalLayout_4.addWidget(self.faculty_list)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 20)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.year_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.year_label.setEnabled(True)
        self.year_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.verticalLayout_3.addWidget(self.year_label)
        self.year_list = QtWidgets.QListWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_list.sizePolicy().hasHeightForWidth())
        self.year_list.setSizePolicy(sizePolicy)
        self.year_list.setMinimumSize(QtCore.QSize(158, 0))
        self.year_list.setBaseSize(QtCore.QSize(0, 0))
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
        self.year_list.setObjectName("year_list")
        self.verticalLayout_3.addWidget(self.year_list)
        self.verticalLayout_3.setStretch(1, 20)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupe_label = QtWidgets.QLabel(parent=self.centralwidget)
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
        self.verticalLayout_2.addWidget(self.groupe_label)
        self.group_list = QtWidgets.QListWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_list.sizePolicy().hasHeightForWidth())
        self.group_list.setSizePolicy(sizePolicy)
        self.group_list.setMinimumSize(QtCore.QSize(158, 0))
        self.group_list.setBaseSize(QtCore.QSize(0, 0))
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
        self.group_list.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.group_list.setObjectName("group_list")
        self.verticalLayout_2.addWidget(self.group_list)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 20)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(140, 140, 140);")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_label.sizePolicy().hasHeightForWidth())
        self.table_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.table_label.setFont(font)
        self.table_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.table_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.table_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.table_label.setObjectName("table_label")
        self.verticalLayout.addWidget(self.table_label)
        self.group_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.group_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
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
        self.group_table.setMouseTracking(False)
        self.group_table.setTabletTracking(False)
        self.group_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.group_table.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.group_table.setAcceptDrops(False)
        self.group_table.setAutoFillBackground(False)
        self.group_table.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"font: 25 12pt \"Gotham Light\";\n"
"color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(179, 179, 179);\n"
"selection-background-color: rgb(30, 185, 85);\n"
"gridline-color: rgb(17, 17, 17);")
        self.group_table.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.group_table.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.group_table.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.group_table.setLineWidth(0)
        self.group_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.group_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.group_table.setAutoScroll(True)
        self.group_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.group_table.setTabKeyNavigation(False)
        self.group_table.setProperty("showDropIndicator", True)
        self.group_table.setDragEnabled(False)
        self.group_table.setDragDropOverwriteMode(False)
        self.group_table.setDefaultDropAction(QtCore.Qt.DropAction.CopyAction)
        self.group_table.setAlternatingRowColors(True)
        self.group_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.group_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.group_table.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
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
        self.verticalLayout.addWidget(self.group_table)
        self.help_label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_label.sizePolicy().hasHeightForWidth())
        self.help_label.setSizePolicy(sizePolicy)
        self.help_label.setMinimumSize(QtCore.QSize(0, 57))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        self.help_label.setFont(font)
        self.help_label.setStyleSheet("color: rgb(140, 140, 140);")
        self.help_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.help_label.setWordWrap(True)
        self.help_label.setObjectName("help_label")
        self.verticalLayout.addWidget(self.help_label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 90)
        self.horizontalLayout_2.setStretch(1, 200)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(20, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.last_word = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        self.last_word.setFont(font)
        self.last_word.setStyleSheet("color: rgb(255, 255, 255);")
        self.last_word.setObjectName("last_word")
        self.verticalLayout_10.addWidget(self.last_word)
        self.word = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        self.word.setFont(font)
        self.word.setStyleSheet("color: rgb(255, 255, 255);")
        self.word.setText("")
        self.word.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.word.setObjectName("word")
        self.verticalLayout_10.addWidget(self.word)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.save_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton::hover{\n"
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
        self.save_button.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferLowercase)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_11.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QPushButton::hover{\n"
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
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout_11.addWidget(self.cancel_button)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.checkBox_recognitionMode = QtWidgets.QCheckBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_recognitionMode.sizePolicy().hasHeightForWidth())
        self.checkBox_recognitionMode.setSizePolicy(sizePolicy)
        self.checkBox_recognitionMode.setStyleSheet("    QCheckBox::indicator:unchecked {\n"
"        image: url(switch_off.png);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"        image: url(switch_on.png);\n"
"    }")
        self.checkBox_recognitionMode.setText("")
        self.checkBox_recognitionMode.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_recognitionMode.setObjectName("checkBox_recognitionMode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBox_recognitionMode)
        self.checkBox_tableMode = QtWidgets.QCheckBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_tableMode.sizePolicy().hasHeightForWidth())
        self.checkBox_tableMode.setSizePolicy(sizePolicy)
        self.checkBox_tableMode.setStyleSheet("    QCheckBox::indicator:unchecked {\n"
"        image: url(switch_off.png);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"        image: url(switch_on.png);\n"
"    }")
        self.checkBox_tableMode.setText("")
        self.checkBox_tableMode.setObjectName("checkBox_tableMode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBox_tableMode)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.activate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.activate_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activate_button.sizePolicy().hasHeightForWidth())
        self.activate_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.activate_button.setFont(font)
        self.activate_button.setMouseTracking(True)
        self.activate_button.setTabletTracking(True)
        self.activate_button.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.activate_button.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.activate_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
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
        self.activate_button.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhPreferLowercase)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/in programm/icons/Mic.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.activate_button.setIcon(icon3)
        self.activate_button.setIconSize(QtCore.QSize(35, 35))
        self.activate_button.setAutoDefault(False)
        self.activate_button.setDefault(False)
        self.activate_button.setFlat(False)
        self.activate_button.setObjectName("activate_button")
        self.verticalLayout_6.addWidget(self.activate_button)
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.error_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.error_label.setWordWrap(False)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_6.addWidget(self.error_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(231, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_7.setContentsMargins(-1, -1, 18, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_7.addItem(spacerItem2)
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_button.setFont(font)
        self.exit_button.setMouseTracking(True)
        self.exit_button.setTabletTracking(True)
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
        self.verticalLayout_7.addWidget(self.exit_button)
        self.verticalLayout_7.setStretch(1, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 10)
        self.horizontalLayout_3.setStretch(3, 8)
        self.horizontalLayout_3.setStretch(4, 10)
        self.horizontalLayout_3.setStretch(5, 3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 40)
        table_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(table_window)
        QtCore.QMetaObject.connectSlotsByName(table_window)

    def retranslateUi(self, table_window):
        _translate = QtCore.QCoreApplication.translate
        table_window.setWindowTitle(_translate("table_window", "Voice journal"))
        self.faculty_label.setText(_translate("table_window", "Факультет "))
        self.year_label.setText(_translate("table_window", "Курс"))
        self.groupe_label.setText(_translate("table_window", "Группа"))
        self.label.setText(_translate("table_window", "Список голосовых команд:\n"
"\"Выбрать факультет\"\n"
"\"Выбрать курс\" \n"
"\"Выбрать группу\"\n"
"\"Сохранить\"\n"
"\"Отменить\""))
        self.table_label.setText(_translate("table_window", "Журнал обучающихся"))
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
        self.help_label.setText(_translate("table_window", "Примечание: для выбора факультета с помощью голосовых команд вам необходимо нажать на кнопку \"Голосовой ввод\" и назвать номер факультета, указанный в списке."))
        self.last_word.setText(_translate("table_window", "Последнее распознанное слово:"))
        self.save_button.setText(_translate("table_window", "Сохранить"))
        self.cancel_button.setText(_translate("table_window", "Отменить"))
        self.label_2.setText(_translate("table_window", "SR"))
        self.label_3.setText(_translate("table_window", "Лабораторные работы"))
        self.activate_button.setToolTip(_translate("table_window", "<html><head/><body><p><span style=\" color:#ffffff;\">Hotkey - Ctrl + Space</span></p></body></html>"))
        self.activate_button.setWhatsThis(_translate("table_window", "<html><head/><body><p>Hotkey - Ctrl + Space</p></body></html>"))
        self.activate_button.setText(_translate("table_window", "Голосовой ввод"))
        self.error_label.setText(_translate("table_window", "Ошибка ввода, попробуйте еще раз"))
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
