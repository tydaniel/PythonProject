# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(328, 190)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 120, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(LoginDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 60, 221, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.txtUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUsername.setObjectName("txtUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsername)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.txtPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPassword)

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.usernameLabel.setText(_translate("LoginDialog", "Username"))
        self.passwordLabel.setText(_translate("LoginDialog", "Password"))

