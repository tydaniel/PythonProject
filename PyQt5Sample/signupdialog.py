from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from ui_signupdialog import Ui_SignupDialog
from auth import Auth


class SignupDialog(QDialog, Ui_SignupDialog):
    Success, Failed, Rejected = range(0, 3)
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)

    def onAccept(self):
        auth = Auth()
        if self.txtPasswordLineEdit.text() == self.txtConfirmLineEdit.text():
            if auth.doSignUp(self.txtUsernameLineEdit.text(), self.txtPasswordLineEdit.text()):
                self.setResult(self.Success)
            else:
                msgBox = QMessageBox(self)
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Sign up")
                msgBox.setText("Sign up Error!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                self.setResult(self.Failed)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Sign up")
            msgBox.setText("Please set the same password!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)

    def onReject(self):
        self.setResult(self.Rejected)