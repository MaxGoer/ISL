# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E-DE.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 303)
        MainWindow.setMinimumSize(QtCore.QSize(569, 303))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input_box = QtWidgets.QGroupBox(self.centralwidget)
        self.input_box.setObjectName("input_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.input_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input = QtWidgets.QPlainTextEdit(self.input_box)
        self.input.setObjectName("input")
        self.verticalLayout_4.addWidget(self.input)
        self.horizontalLayout_4.addWidget(self.input_box)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.output_box = QtWidgets.QGroupBox(self.centralwidget)
        self.output_box.setObjectName("output_box")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.output_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.output = QtWidgets.QPlainTextEdit(self.output_box)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout_5.addWidget(self.output)
        self.verticalLayout_6.addWidget(self.output_box)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.mode_box = QtWidgets.QGroupBox(self.centralwidget)
        self.mode_box.setMinimumSize(QtCore.QSize(81, 114))
        self.mode_box.setMaximumSize(QtCore.QSize(81, 114))
        self.mode_box.setObjectName("mode_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mode_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.encrypt_mode = QtWidgets.QRadioButton(self.mode_box)
        self.encrypt_mode.setChecked(True)
        self.encrypt_mode.setObjectName("encrypt_mode")
        self.verticalLayout.addWidget(self.encrypt_mode)
        self.decrypt_mode = QtWidgets.QRadioButton(self.mode_box)
        self.decrypt_mode.setObjectName("decrypt_mode")
        self.verticalLayout.addWidget(self.decrypt_mode)
        self.horizontalLayout_3.addWidget(self.mode_box)
        self.view_box = QtWidgets.QGroupBox(self.centralwidget)
        self.view_box.setMinimumSize(QtCore.QSize(81, 114))
        self.view_box.setMaximumSize(QtCore.QSize(114, 114))
        self.view_box.setObjectName("view_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.view_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.code_rb = QtWidgets.QRadioButton(self.view_box)
        self.code_rb.setChecked(True)
        self.code_rb.setObjectName("code_rb")
        self.verticalLayout_2.addWidget(self.code_rb)
        self.char_rb = QtWidgets.QRadioButton(self.view_box)
        self.char_rb.setObjectName("char_rb")
        self.verticalLayout_2.addWidget(self.char_rb)
        self.horizontalLayout_3.addWidget(self.view_box)
        self.crypt_settings_box = QtWidgets.QGroupBox(self.centralwidget)
        self.crypt_settings_box.setMinimumSize(QtCore.QSize(171, 114))
        self.crypt_settings_box.setMaximumSize(QtCore.QSize(171, 114))
        self.crypt_settings_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.crypt_settings_box.setObjectName("crypt_settings_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.crypt_settings_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.crypt_settings_box)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.key_input = QtWidgets.QLineEdit(self.crypt_settings_box)
        self.key_input.setMinimumSize(QtCore.QSize(83, 0))
        self.key_input.setMaximumSize(QtCore.QSize(83, 16777215))
        self.key_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.key_input.setText("")
        self.key_input.setMaxLength(9)
        self.key_input.setAlignment(QtCore.Qt.AlignCenter)
        self.key_input.setObjectName("key_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.key_input)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.rand_b = QtWidgets.QPushButton(self.crypt_settings_box)
        self.rand_b.setObjectName("rand_b")
        self.horizontalLayout.addWidget(self.rand_b)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.enable_encrypting_cb = QtWidgets.QCheckBox(self.crypt_settings_box)
        self.enable_encrypting_cb.setToolTip("")
        self.enable_encrypting_cb.setChecked(True)
        self.enable_encrypting_cb.setObjectName("enable_encrypting_cb")
        self.horizontalLayout_2.addWidget(self.enable_encrypting_cb)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.crypt_settings_box)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.view_box.setVisible(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E-DE"))
        self.input_box.setTitle(_translate("MainWindow", "Input"))
        self.input.setStatusTip(_translate("MainWindow", "Input area"))
        self.output_box.setTitle(_translate("MainWindow", "Encrypted"))
        self.output.setStatusTip(_translate("MainWindow", "Output view"))
        self.mode_box.setTitle(_translate("MainWindow", "Mode"))
        self.encrypt_mode.setStatusTip(_translate("MainWindow", "Toggle encrypt mode"))
        self.encrypt_mode.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt_mode.setStatusTip(_translate("MainWindow", "Toggle decrypt mode"))
        self.decrypt_mode.setText(_translate("MainWindow", "Decrypt"))
        self.view_box.setTitle(_translate("MainWindow", "View"))
        self.code_rb.setStatusTip(_translate("MainWindow", "Show character codes in output view"))
        self.code_rb.setText(_translate("MainWindow", "Code"))
        self.char_rb.setStatusTip(_translate("MainWindow", "Show characters in output view"))
        self.char_rb.setText(_translate("MainWindow", "Char"))
        self.crypt_settings_box.setTitle(_translate("MainWindow", "Crypt settings"))
        self.label.setText(_translate("MainWindow", "Key:"))
        self.key_input.setStatusTip(_translate("MainWindow", "Cypher key (max. 9 symbols)"))
        self.key_input.setPlaceholderText(_translate("MainWindow", "0"))
        self.rand_b.setStatusTip(_translate("MainWindow", "Set random cypher key"))
        self.rand_b.setText(_translate("MainWindow", "Random"))
        self.enable_encrypting_cb.setStatusTip(_translate("MainWindow", "Enable encrypting"))
        self.enable_encrypting_cb.setText(_translate("MainWindow", "Enable"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open input file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save output to text file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

