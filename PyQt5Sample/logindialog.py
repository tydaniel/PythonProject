from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from ui_logindialog import Ui_LoginDialog
from auth import Auth


class LoginDialog(QDialog, Ui_LoginDialog):
    Success, Failed, Rejected = range(0, 3)
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)

    def onAccept(self):
        auth = Auth()
        if auth.doLogin(self.txtUsername.text(), self.txtPassword.text()):
            self.setResult(self.Success)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("LoginDialog")
            msgBox.setText("Either incorrect username and/or password. Try again!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)


    def onReject(self):
        self.setResult(self.Rejected)
