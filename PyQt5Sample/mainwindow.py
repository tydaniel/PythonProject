from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox, QMainWindow
from ui_mainwindow import Ui_MainWindow
from signupdialog import SignupDialog
from auth import Auth


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.actionAbout_US.triggered.connect(self.onAbout)
        self.actionSignup.triggered.connect(self.onSignup)

    def onAbout(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("About...")
        msgBox.setText("Welcome here!")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def onSignup(self):
        signupDialog = SignupDialog()

        isSignup = False
        result = -1
        while not isSignup:
            result = signupDialog.exec_()
            if result == SignupDialog.Success:
                isSignup = True
            elif result == SignupDialog.Rejected:
                return
            else:
                isSignup = False

