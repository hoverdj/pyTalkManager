# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCongregationWindow.ui'
#
# Created: Wed Dec 10 16:47:09 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddCongregationWindow(object):
    def setupUi(self, AddCongregationWindow):
        AddCongregationWindow.setObjectName("AddCongregationWindow")
        AddCongregationWindow.resize(349, 369)
        self.gridLayout_8 = QtGui.QGridLayout(AddCongregationWindow)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame = QtGui.QFrame(AddCongregationWindow)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_4 = QtGui.QCheckBox(self.frame)
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_close = QtGui.QPushButton(self.frame)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout.addWidget(self.button_close)
        self.button_add = QtGui.QPushButton(self.frame)
        self.button_add.setDefault(True)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.gridLayout_8.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_7 = QtGui.QFrame(AddCongregationWindow)
        self.frame_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.frame_7)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_name = QtGui.QLineEdit(self.frame_2)
        self.line_name.setObjectName("line_name")
        self.gridLayout.addWidget(self.line_name, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.tab)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.line_phone = QtGui.QLineEdit(self.frame_3)
        self.line_phone.setObjectName("line_phone")
        self.gridLayout_4.addWidget(self.line_phone, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.line_email = QtGui.QLineEdit(self.frame_3)
        self.line_email.setObjectName("line_email")
        self.gridLayout_4.addWidget(self.line_email, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_5 = QtGui.QFrame(self.tab_2)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_9 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_8 = QtGui.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)
        self.line_latitude = QtGui.QLineEdit(self.frame_5)
        self.line_latitude.setObjectName("line_latitude")
        self.gridLayout_9.addWidget(self.line_latitude, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 1, 0, 1, 1)
        self.line_longitude = QtGui.QLineEdit(self.frame_5)
        self.line_longitude.setObjectName("line_longitude")
        self.gridLayout_9.addWidget(self.line_longitude, 1, 2, 1, 1)
        self.gridLayout_7.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)
        self.line_state = QtGui.QLineEdit(self.frame_4)
        self.line_state.setObjectName("line_state")
        self.gridLayout_2.addWidget(self.line_state, 6, 1, 1, 1)
        self.line_zipcode = QtGui.QLineEdit(self.frame_4)
        self.line_zipcode.setObjectName("line_zipcode")
        self.gridLayout_2.addWidget(self.line_zipcode, 8, 1, 1, 1)
        self.line_city = QtGui.QLineEdit(self.frame_4)
        self.line_city.setObjectName("line_city")
        self.gridLayout_2.addWidget(self.line_city, 4, 1, 1, 1)
        self.line_address = QtGui.QLineEdit(self.frame_4)
        self.line_address.setObjectName("line_address")
        self.gridLayout_2.addWidget(self.line_address, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtGui.QFrame(self.tab_4)
        self.frame_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtGui.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_10 = QtGui.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_10.addWidget(self.label_10, 2, 0, 1, 1)
        self.frame_10 = QtGui.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioSaturday = QtGui.QRadioButton(self.frame_10)
        self.radioSaturday.setCheckable(True)
        self.radioSaturday.setChecked(True)
        self.radioSaturday.setAutoExclusive(True)
        self.radioSaturday.setObjectName("radioSaturday")
        self.verticalLayout_3.addWidget(self.radioSaturday)
        self.radioSunday = QtGui.QRadioButton(self.frame_10)
        self.radioSunday.setObjectName("radioSunday")
        self.verticalLayout_3.addWidget(self.radioSunday)
        self.gridLayout_10.addWidget(self.frame_10, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.line_3 = QtGui.QFrame(self.tab_4)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.frame_9 = QtGui.QFrame(self.tab_4)
        self.frame_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_11 = QtGui.QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_11 = QtGui.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)
        self.timeEdit = QtGui.QTimeEdit(self.frame_9)
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_11.addWidget(self.timeEdit, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_6 = QtGui.QFrame(self.tab_3)
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.text_note = QtGui.QTextEdit(self.frame_6)
        self.text_note.setObjectName("text_note")
        self.gridLayout_6.addWidget(self.text_note, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_8.addWidget(self.frame_7, 0, 0, 1, 1)

        self.retranslateUi(AddCongregationWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), AddCongregationWindow.close)
        QtCore.QMetaObject.connectSlotsByName(AddCongregationWindow)
        AddCongregationWindow.setTabOrder(self.line_name, self.line_phone)
        AddCongregationWindow.setTabOrder(self.line_phone, self.line_email)
        AddCongregationWindow.setTabOrder(self.line_email, self.line_address)
        AddCongregationWindow.setTabOrder(self.line_address, self.line_city)
        AddCongregationWindow.setTabOrder(self.line_city, self.line_state)
        AddCongregationWindow.setTabOrder(self.line_state, self.line_zipcode)
        AddCongregationWindow.setTabOrder(self.line_zipcode, self.line_latitude)
        AddCongregationWindow.setTabOrder(self.line_latitude, self.line_longitude)
        AddCongregationWindow.setTabOrder(self.line_longitude, self.timeEdit)
        AddCongregationWindow.setTabOrder(self.timeEdit, self.text_note)
        AddCongregationWindow.setTabOrder(self.text_note, self.button_add)
        AddCongregationWindow.setTabOrder(self.button_add, self.button_close)
        AddCongregationWindow.setTabOrder(self.button_close, self.tabWidget)
        AddCongregationWindow.setTabOrder(self.tabWidget, self.checkBox_4)

    def retranslateUi(self, AddCongregationWindow):
        AddCongregationWindow.setWindowTitle(QtGui.QApplication.translate("AddCongregationWindow", "Add Congregation", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("AddCongregationWindow", "Batch", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("AddCongregationWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("AddCongregationWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddCongregationWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddCongregationWindow", "Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddCongregationWindow", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("AddCongregationWindow", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddCongregationWindow", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("AddCongregationWindow", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddCongregationWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddCongregationWindow", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddCongregationWindow", "State", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddCongregationWindow", "Zipcode", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("AddCongregationWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("AddCongregationWindow", "Meeting Days", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSaturday.setText(QtGui.QApplication.translate("AddCongregationWindow", "Saturday", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSaturday.setShortcut(QtGui.QApplication.translate("AddCongregationWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSunday.setText(QtGui.QApplication.translate("AddCongregationWindow", "Sunday", None, QtGui.QApplication.UnicodeUTF8))
        self.radioSunday.setShortcut(QtGui.QApplication.translate("AddCongregationWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("AddCongregationWindow", "Meeting Time", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("AddCongregationWindow", "Schedule", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("AddCongregationWindow", "Notes", None, QtGui.QApplication.UnicodeUTF8))

