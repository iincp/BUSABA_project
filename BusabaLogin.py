# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BusabaLogin.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form_Login(object):
    def setupUi(self, Form_Login):
        if not Form_Login.objectName():
            Form_Login.setObjectName(u"Form_Login")
        Form_Login.resize(1280, 720)
        Form_Login.setMaximumSize(QSize(1280, 720))
        self.whiteSpace = QLabel(Form_Login)
        self.whiteSpace.setObjectName(u"whiteSpace")
        self.whiteSpace.setGeometry(QRect(0, 0, 1280, 720))
        self.whiteSpace.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setFamilies([u"Maragsa"])
        self.whiteSpace.setFont(font)
        self.whiteSpace.setPixmap(QPixmap(u"BusabaImages/busaba-Login.png"))
        self.label_white = QLabel(Form_Login)
        self.label_white.setObjectName(u"label_white")
        self.label_white.setGeometry(QRect(490, 350, 58, 181))
        self.label_white.setPixmap(QPixmap(u"BusabaImages/White.png"))
        self.frame_UsernamePassword = QFrame(Form_Login)
        self.frame_UsernamePassword.setObjectName(u"frame_UsernamePassword")
        self.frame_UsernamePassword.setGeometry(QRect(150, 349, 341, 181))
        self.frame_UsernamePassword.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"}\n"
"")
        self.frame_UsernamePassword.setFrameShape(QFrame.StyledPanel)
        self.frame_UsernamePassword.setFrameShadow(QFrame.Raised)
        self.label_username = QLabel(self.frame_UsernamePassword)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(10, 20, 311, 16))
        font1 = QFont()
        font1.setFamilies([u"Maragsa"])
        font1.setPointSize(13)
        self.label_username.setFont(font1)
        self.label_username.setStyleSheet(u"font-family: Maragsa; \n"
"color: #002c3e;")
        self.label_password = QLabel(self.frame_UsernamePassword)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 70, 321, 16))
        self.label_password.setFont(font1)
        self.label_password.setStyleSheet(u"font-family: Maragsa; \n"
"color: #002c3e;")
        self.lineEdit_username = QLineEdit(self.frame_UsernamePassword)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(10, 40, 321, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.lineEdit_username.setFont(font2)
        self.lineEdit_username.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: red;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"")
        self.lineEdit_password = QLineEdit(self.frame_UsernamePassword)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(10, 90, 321, 21))
        self.lineEdit_password.setFont(font2)
        self.lineEdit_password.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: red;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"")
        self.lineEdit_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setReadOnly(False)
        self.checkBox = QCheckBox(self.frame_UsernamePassword)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 120, 181, 21))
        font3 = QFont()
        font3.setFamilies([u"Maragsa"])
        font3.setPointSize(11)
        self.checkBox.setFont(font3)
        self.checkBox.setStyleSheet(u"color: #002c3e;")
        self.whiteSpace2 = QLabel(Form_Login)
        self.whiteSpace2.setObjectName(u"whiteSpace2")
        self.whiteSpace2.setGeometry(QRect(240, 550, 161, 71))
        self.whiteSpace2.setPixmap(QPixmap(u"BusabaImages/White2.png"))
        self.pushButton_signIn = QPushButton(Form_Login)
        self.pushButton_signIn.setObjectName(u"pushButton_signIn")
        self.pushButton_signIn.setGeometry(QRect(160, 560, 321, 41))
        font4 = QFont()
        font4.setFamilies([u"Maragsa"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.pushButton_signIn.setFont(font4)
        self.pushButton_signIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_signIn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: #002c3e;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 17, 34);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_gotoSignUp = QPushButton(Form_Login)
        self.pushButton_gotoSignUp.setObjectName(u"pushButton_gotoSignUp")
        self.pushButton_gotoSignUp.setGeometry(QRect(180, 610, 271, 32))
        font5 = QFont()
        font5.setFamilies([u"Maragsa"])
        font5.setPointSize(12)
        font5.setUnderline(True)
        self.pushButton_gotoSignUp.setFont(font5)
        self.pushButton_gotoSignUp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_gotoSignUp.setStyleSheet(u"color: #002c3e;\n"
"border-style: none;")
        self.frame_logoWelcome = QFrame(Form_Login)
        self.frame_logoWelcome.setObjectName(u"frame_logoWelcome")
        self.frame_logoWelcome.setGeometry(QRect(150, 250, 341, 91))
        self.frame_logoWelcome.setStyleSheet(u"border: none;\n"
"background: white;")
        self.frame_logoWelcome.setFrameShape(QFrame.StyledPanel)
        self.frame_logoWelcome.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_logoWelcome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 40, 58, 16))
        self.label_welcome = QLabel(self.frame_logoWelcome)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setGeometry(QRect(0, 0, 341, 51))
        font6 = QFont()
        font6.setFamilies([u"Maragsa"])
        font6.setPointSize(34)
        font6.setBold(True)
        self.label_welcome.setFont(font6)
        self.label_welcome.setStyleSheet(u"color: #002c3e")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_logoWelcome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-5, 50, 351, 20))
        font7 = QFont()
        font7.setFamilies([u"Maragsa"])
        font7.setPointSize(16)
        font7.setBold(False)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: #002c3e;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.whiteSpace3 = QLabel(Form_Login)
        self.whiteSpace3.setObjectName(u"whiteSpace3")
        self.whiteSpace3.setGeometry(QRect(10, 690, 91, 16))
        self.whiteSpace3.setPixmap(QPixmap(u"BusabaImages/White2.png"))
        self.label_busabaCopyright = QLabel(Form_Login)
        self.label_busabaCopyright.setObjectName(u"label_busabaCopyright")
        self.label_busabaCopyright.setGeometry(QRect(20, 690, 121, 16))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        font8.setBold(False)
        self.label_busabaCopyright.setFont(font8)
        self.label_busabaCopyright.setStyleSheet(u"color: #002c3e;")

        self.retranslateUi(Form_Login)

        QMetaObject.connectSlotsByName(Form_Login)
    # setupUi

    def retranslateUi(self, Form_Login):
        Form_Login.setWindowTitle(QCoreApplication.translate("Form_Login", u"Form", None))
        self.whiteSpace.setText("")
        self.label_white.setText("")
        self.label_username.setText(QCoreApplication.translate("Form_Login", u"Username:", None))
        self.label_password.setText(QCoreApplication.translate("Form_Login", u"Password:", None))
        self.checkBox.setText(QCoreApplication.translate("Form_Login", u"Remember Me", None))
        self.whiteSpace2.setText("")
        self.pushButton_signIn.setText(QCoreApplication.translate("Form_Login", u"Sign In", None))
        self.pushButton_gotoSignUp.setText(QCoreApplication.translate("Form_Login", u"Don't have an account? Sign Up", None))
        self.label.setText("")
        self.label_welcome.setText(QCoreApplication.translate("Form_Login", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("Form_Login", u"Please Enter Your Details", None))
        self.whiteSpace3.setText("")
        self.label_busabaCopyright.setText(QCoreApplication.translate("Form_Login", u"\u00a9 BUSABA 2023", None))
    # retranslateUi

