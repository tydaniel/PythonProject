# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFetch_Info = QtWidgets.QMenu(self.menubar)
        self.menuFetch_Info.setObjectName("menuFetch_Info")
        self.menuAdmin_Panel = QtWidgets.QMenu(self.menubar)
        self.menuAdmin_Panel.setObjectName("menuAdmin_Panel")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSignup = QtWidgets.QAction(MainWindow)
        self.actionSignup.setObjectName("actionSignup")
        self.actionAbout_US = QtWidgets.QAction(MainWindow)
        self.actionAbout_US.setObjectName("actionAbout_US")
        self.menuFetch_Info.addAction(self.actionRun)
        self.menuFetch_Info.addSeparator()
        self.menuFetch_Info.addAction(self.actionSettings)
        self.menuAdmin_Panel.addAction(self.actionSignup)
        self.menuAbout.addAction(self.actionAbout_US)
        self.menubar.addAction(self.menuFetch_Info.menuAction())
        self.menubar.addAction(self.menuAdmin_Panel.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFetch_Info.setTitle(_translate("MainWindow", "Fetch Info"))
        self.menuAdmin_Panel.setTitle(_translate("MainWindow", "Admin Panel"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSignup.setText(_translate("MainWindow", "Sign up..."))
        self.actionAbout_US.setText(_translate("MainWindow", "About US"))

