# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignupDialog(object):
    def setupUi(self, SignupDialog):
        SignupDialog.setObjectName("SignupDialog")
        SignupDialog.resize(339, 185)
        self.buttonBox = QtWidgets.QDialogButtonBox(SignupDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 140, 291, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(SignupDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 241, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.txtUsernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUsernameLineEdit.setObjectName("txtUsernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.txtPasswordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPasswordLineEdit.setObjectName("txtPasswordLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPasswordLineEdit)
        self.confirmLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.confirmLabel.setObjectName("confirmLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.confirmLabel)
        self.txtConfirmLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtConfirmLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmLineEdit.setObjectName("txtConfirmLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtConfirmLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)

        self.retranslateUi(SignupDialog)
        self.buttonBox.accepted.connect(SignupDialog.accept)
        self.buttonBox.rejected.connect(SignupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SignupDialog)

    def retranslateUi(self, SignupDialog):
        _translate = QtCore.QCoreApplication.translate
        SignupDialog.setWindowTitle(_translate("SignupDialog", "Sign Up"))
        self.passwordLabel.setText(_translate("SignupDialog", "Password"))
        self.confirmLabel.setText(_translate("SignupDialog", "Confirm"))
        self.usernameLabel.setText(_translate("SignupDialog", "Username"))

