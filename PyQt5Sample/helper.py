from PyQt5.QtCore import *
from PyQt5.QtSql import *

def dbConnect():
    db = QSqlDatabase.addDatabase("QSQLITE")
    filename = "pythonthusiast.db"
    database = QFile(filename)

    if not database.exists():
        qDebug("Database not found. Creating and openging.")
        db.setDatabaseName(filename)
        db.open()
        query = QSqlQuery()
        query.exec_("create table qtapp_users"
                    " (id integer primary key autoincrement,"
                    "username varchar(30),"
                    "password varchar(255))")
        query.prepare("insert into qtapp_users(username, password) values(:username, :password)")
        query.bindValue(":username", "pxj")
        query.bindValue(":password", computeHash("password"))
        query.exec_()
    else:
        qDebug("Database found. Opening")
        db.setDatabaseName(filename)
        db.open()
    return db.isOpen()

def computeHash(orininal):
    return QCryptographicHash.hash(QByteArray(bytes(orininal,"UTF8")), QCryptographicHash.Md5).toHex()
