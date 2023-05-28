# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BusabaRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        Form.setMinimumSize(QSize(1280, 720))
        Form.setMaximumSize(QSize(1280, 720))
        self.whiteSpace5 = QLabel(Form)
        self.whiteSpace5.setObjectName(u"whiteSpace5")
        self.whiteSpace5.setGeometry(QRect(0, 0, 1280, 720))
        self.whiteSpace5.setPixmap(QPixmap(u"BusabaImages/busaba-Register.png"))
        self.frame_signup = QFrame(Form)
        self.frame_signup.setObjectName(u"frame_signup")
        self.frame_signup.setGeometry(QRect(150, 69, 341, 551))
        self.frame_signup.setStyleSheet(u"background: white;")
        self.frame_signup.setFrameShape(QFrame.NoFrame)
        self.frame_signup.setFrameShadow(QFrame.Raised)
        self.label_signUp = QLabel(self.frame_signup)
        self.label_signUp.setObjectName(u"label_signUp")
        self.label_signUp.setGeometry(QRect(0, -10, 341, 41))
        font = QFont()
        font.setFamilies([u"Maragsa"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_signUp.setFont(font)
        self.label_signUp.setStyleSheet(u"color: #002c3e")
        self.label_signUp.setAlignment(Qt.AlignCenter)
        self.label_enterDetails = QLabel(self.frame_signup)
        self.label_enterDetails.setObjectName(u"label_enterDetails")
        self.label_enterDetails.setGeometry(QRect(0, 30, 341, 21))
        font1 = QFont()
        font1.setFamilies([u"Maragsa"])
        font1.setPointSize(14)
        self.label_enterDetails.setFont(font1)
        self.label_enterDetails.setStyleSheet(u"color: #002c3e;")
        self.label_enterDetails.setAlignment(Qt.AlignCenter)
        self.frame_deatils = QFrame(self.frame_signup)
        self.frame_deatils.setObjectName(u"frame_deatils")
        self.frame_deatils.setGeometry(QRect(0, 60, 341, 431))
        self.frame_deatils.setFrameShape(QFrame.StyledPanel)
        self.frame_deatils.setFrameShadow(QFrame.Raised)
        self.label_username = QLabel(self.frame_deatils)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(20, 20, 301, 16))
        font2 = QFont()
        font2.setFamilies([u"Maragsa"])
        font2.setPointSize(13)
        self.label_username.setFont(font2)
        self.label_username.setStyleSheet(u"color: #002c3e;")
        self.label_name = QLabel(self.frame_deatils)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(20, 70, 311, 16))
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet(u"color: #002c3e;")
        self.label_surname = QLabel(self.frame_deatils)
        self.label_surname.setObjectName(u"label_surname")
        self.label_surname.setGeometry(QRect(20, 120, 311, 16))
        self.label_surname.setFont(font2)
        self.label_surname.setStyleSheet(u"color: #002c3e;")
        self.label_phoneNumber = QLabel(self.frame_deatils)
        self.label_phoneNumber.setObjectName(u"label_phoneNumber")
        self.label_phoneNumber.setGeometry(QRect(20, 170, 311, 16))
        self.label_phoneNumber.setFont(font2)
        self.label_phoneNumber.setStyleSheet(u"color: #002c3e;")
        self.label_email = QLabel(self.frame_deatils)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(20, 220, 311, 16))
        self.label_email.setFont(font2)
        self.label_email.setStyleSheet(u"color: #002c3e;")
        self.label_password = QLabel(self.frame_deatils)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(20, 270, 311, 16))
        self.label_password.setFont(font2)
        self.label_password.setStyleSheet(u"color: #002c3e;")
        self.label_dateOfBirth = QLabel(self.frame_deatils)
        self.label_dateOfBirth.setObjectName(u"label_dateOfBirth")
        self.label_dateOfBirth.setGeometry(QRect(20, 320, 311, 16))
        self.label_dateOfBirth.setFont(font2)
        self.label_dateOfBirth.setStyleSheet(u"color: #002c3e;")
        self.lineEdit_username = QLineEdit(self.frame_deatils)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(20, 40, 311, 21))
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
        self.lineEdit_name = QLineEdit(self.frame_deatils)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(20, 90, 311, 21))
        self.lineEdit_name.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: red;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"")
        self.lineEdit_surname = QLineEdit(self.frame_deatils)
        self.lineEdit_surname.setObjectName(u"lineEdit_surname")
        self.lineEdit_surname.setGeometry(QRect(20, 140, 311, 21))
        self.lineEdit_surname.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: red;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"")
        self.lineEdit_phoneNumber = QLineEdit(self.frame_deatils)
        self.lineEdit_phoneNumber.setObjectName(u"lineEdit_phoneNumber")
        self.lineEdit_phoneNumber.setGeometry(QRect(20, 190, 311, 21))
        self.lineEdit_phoneNumber.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: red;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"")
        self.lineEdit_email = QLineEdit(self.frame_deatils)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(20, 240, 311, 21))
        self.lineEdit_email.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: red;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid rgb(0, 17, 34);\n"
"}\n"
"")
        self.lineEdit_password = QLineEdit(self.frame_deatils)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(20, 290, 311, 21))
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
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.dateEdit_dateOfBirth = QDateEdit(self.frame_deatils)
        self.dateEdit_dateOfBirth.setObjectName(u"dateEdit_dateOfBirth")
        self.dateEdit_dateOfBirth.setGeometry(QRect(20, 340, 311, 22))
        self.dateEdit_dateOfBirth.setStyleSheet(u"color: #2B657C;\n"
"background-color: white;\n"
"border: 1px solid black; \n"
"border-radius: 5px;\n"
"\n"
"")
        self.checkBox_agreeOurTerms = QCheckBox(self.frame_deatils)
        self.checkBox_agreeOurTerms.setObjectName(u"checkBox_agreeOurTerms")
        self.checkBox_agreeOurTerms.setGeometry(QRect(20, 380, 141, 20))
        font3 = QFont()
        font3.setFamilies([u"Maragsa"])
        font3.setPointSize(12)
        self.checkBox_agreeOurTerms.setFont(font3)
        self.checkBox_agreeOurTerms.setStyleSheet(u"color: #002c3e;")
        self.pushButton_termsAndServices = QPushButton(self.frame_deatils)
        self.pushButton_termsAndServices.setObjectName(u"pushButton_termsAndServices")
        self.pushButton_termsAndServices.setGeometry(QRect(140, 380, 151, 21))
        font4 = QFont()
        font4.setFamilies([u"Maragsa"])
        font4.setPointSize(12)
        font4.setUnderline(True)
        self.pushButton_termsAndServices.setFont(font4)
        self.pushButton_termsAndServices.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_termsAndServices.setStyleSheet(u"color: #002c3e;\n"
"border-style: none;")
        self.pushButton_SignUp = QPushButton(self.frame_signup)
        self.pushButton_SignUp.setObjectName(u"pushButton_SignUp")
        self.pushButton_SignUp.setGeometry(QRect(20, 510, 311, 32))
        font5 = QFont()
        font5.setFamilies([u"Maragsa"])
        font5.setPointSize(16)
        self.pushButton_SignUp.setFont(font5)
        self.pushButton_SignUp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SignUp.setStyleSheet(u"QPushButton{\n"
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
        self.label_enterDetails.raise_()
        self.frame_deatils.raise_()
        self.label_signUp.raise_()
        self.pushButton_SignUp.raise_()
        self.whiteSpace1 = QLabel(Form)
        self.whiteSpace1.setObjectName(u"whiteSpace1")
        self.whiteSpace1.setGeometry(QRect(490, 180, 41, 301))
        self.whiteSpace1.setPixmap(QPixmap(u"BusabaImages/White.png"))
        self.whitespace2 = QLabel(Form)
        self.whitespace2.setObjectName(u"whitespace2")
        self.whitespace2.setGeometry(QRect(490, 430, 58, 201))
        self.whitespace2.setPixmap(QPixmap(u"BusabaImages/White.png"))
        self.whitespace3 = QLabel(Form)
        self.whitespace3.setObjectName(u"whitespace3")
        self.whitespace3.setGeometry(QRect(480, 180, 58, 201))
        self.whitespace3.setPixmap(QPixmap(u"BusabaImages/White.png"))
        self.whitespace4 = QLabel(Form)
        self.whitespace4.setObjectName(u"whitespace4")
        self.whitespace4.setGeometry(QRect(460, 220, 58, 201))
        self.whitespace4.setPixmap(QPixmap(u"BusabaImages/White.png"))
        self.whitespace6 = QLabel(Form)
        self.whitespace6.setObjectName(u"whitespace6")
        self.whitespace6.setGeometry(QRect(20, 630, 401, 81))
        self.whitespace6.setPixmap(QPixmap(u"BusabaImages/White2.png"))
        self.pushButton_gotoSignIn = QPushButton(Form)
        self.pushButton_gotoSignIn.setObjectName(u"pushButton_gotoSignIn")
        self.pushButton_gotoSignIn.setGeometry(QRect(210, 620, 241, 32))
        self.pushButton_gotoSignIn.setFont(font4)
        self.pushButton_gotoSignIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_gotoSignIn.setStyleSheet(u"color: #002c3e;\n"
"border-style: none;")
        self.label_busabaCopyright = QLabel(Form)
        self.label_busabaCopyright.setObjectName(u"label_busabaCopyright")
        self.label_busabaCopyright.setGeometry(QRect(20, 690, 121, 16))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.label_busabaCopyright.setFont(font6)
        self.label_busabaCopyright.setStyleSheet(u"color: #002c3e;")
        self.whitespace7 = QLabel(Form)
        self.whitespace7.setObjectName(u"whitespace7")
        self.whitespace7.setGeometry(QRect(210, 30, 221, 121))
        self.whitespace7.setPixmap(QPixmap(u"BusabaImages/White2.png"))
        self.whiteSpace5.raise_()
        self.whitespace7.raise_()
        self.whitespace3.raise_()
        self.whiteSpace1.raise_()
        self.whitespace2.raise_()
        self.whitespace4.raise_()
        self.frame_signup.raise_()
        self.whitespace6.raise_()
        self.pushButton_gotoSignIn.raise_()
        self.label_busabaCopyright.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.whiteSpace5.setText("")
        self.label_signUp.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.label_enterDetails.setText(QCoreApplication.translate("Form", u"Please Enter Your Details", None))
        self.label_username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_surname.setText(QCoreApplication.translate("Form", u"Surname", None))
        self.label_phoneNumber.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.label_email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_dateOfBirth.setText(QCoreApplication.translate("Form", u"Date of Birth", None))
        self.checkBox_agreeOurTerms.setText(QCoreApplication.translate("Form", u"Agree with our", None))
        self.pushButton_termsAndServices.setText(QCoreApplication.translate("Form", u"Terms and Services", None))
        self.pushButton_SignUp.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.whiteSpace1.setText("")
        self.whitespace2.setText("")
        self.whitespace3.setText("")
        self.whitespace4.setText("")
        self.whitespace6.setText("")
        self.pushButton_gotoSignIn.setText(QCoreApplication.translate("Form", u"Already Registered? Sign In", None))
        self.label_busabaCopyright.setText(QCoreApplication.translate("Form", u"\u00a9 BUSABA 2023", None))
        self.whitespace7.setText("")
    # retranslateUi

