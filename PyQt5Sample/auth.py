from PyQt5.QtSql import *
import helper

class Auth:
    def doLogin(self, username, password):
        query = QSqlQuery()
        query.prepare("select id from qtapp_users where username = :username and password = :password")
        query.bindValue(":username", username)
        query.bindValue(":password", helper.computeHash(password))
        query.exec_()
        if query.next():
            return True
        return False

    def doSignUp(self, username, password):
        query = QSqlQuery()
        query.prepare("select id from qtapp_users where username = :username")
        query.bindValue(":username", username)
        query.exec_()
        if query.next():
            return False

        query.prepare("insert into qtapp_users(username, password) values(:username, :password)")
        query.bindValue(":username", username)
        query.bindValue(":password", helper.computeHash(password))
        query.exec_()

        query.prepare("select id from qtapp_users where username = :username")
        query.bindValue(":username", username)
        query.exec_()
        if query.next():
            return True
        return False
