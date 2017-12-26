import sys
from PyQt5.Qt import *
from logindialog import LoginDialog
from mainwindow import MainWindow

import helper


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helper.dbConnect()

    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()
        if result == LoginDialog.Success or LoginDialog.Rejected:
            isAuth = True
        else:
            isAuth = False

    if result == LoginDialog.Success:
        w = MainWindow()
        w.show()
        app.exec_()

    sys.exit(-1)

