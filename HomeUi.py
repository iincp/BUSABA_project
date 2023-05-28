# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BUSABA.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 720)
        MainWindow.setMinimumSize(QSize(1279, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"*{ \n"
" 	border:none; \n"
"	background-color: transparent; \n"
"	background: transparent; \n"
"	padding: 0 ;\n"
"	margin: 0;\n"
"	color:#fff; \n"
"} \n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MenuBar = QWidget(self.centralwidget)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setGeometry(QRect(220, 150, 841, 61))
        self.MenuBar.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.MenuBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.HomeButton = QPushButton(self.MenuBar)
        self.HomeButton.setObjectName(u"HomeButton")
        self.HomeButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	border-radius:10px;\n"
"	background-color:rgb(1,41,61);\n"
"	color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(1,41,61);  \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"	")

        self.horizontalLayout.addWidget(self.HomeButton)

        self.AboutButton = QPushButton(self.MenuBar)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	border-radius:10px;\n"
"	background-color:rgb(1,41,61);\n"
"	color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(1,41,61);  \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"	")

        self.horizontalLayout.addWidget(self.AboutButton)

        self.ContactButton = QPushButton(self.MenuBar)
        self.ContactButton.setObjectName(u"ContactButton")
        self.ContactButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	border-radius:10px;\n"
"	background-color:rgb(1,41,61);\n"
"	color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(1,41,61);  \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"	")

        self.horizontalLayout.addWidget(self.ContactButton)

        self.BookingButton = QPushButton(self.MenuBar)
        self.BookingButton.setObjectName(u"BookingButton")
        self.BookingButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	border-radius:10px;\n"
"	background-color:rgb(1,41,61);\n"
"	color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(1,41,61);  \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"	")

        self.horizontalLayout.addWidget(self.BookingButton)

        self.AccountButton = QPushButton(self.MenuBar)
        self.AccountButton.setObjectName(u"AccountButton")
        self.AccountButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	border-radius:10px;\n"
"	background-color:rgb(1,41,61);\n"
"	color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(1,41,61);  \n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"	")

        self.horizontalLayout.addWidget(self.AccountButton)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1280, 720))
        self.widget_2.setStyleSheet(u"")
        self.Pages = QStackedWidget(self.widget_2)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(0, 0, 1280, 720))
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.widget_3 = QWidget(self.Home)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 1280, 720))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.HomeContent = QWidget(self.widget_3)
        self.HomeContent.setObjectName(u"HomeContent")
        self.HomeContent.setGeometry(QRect(40, 230, 1201, 481))
        self.HomeContent.setMinimumSize(QSize(0, 0))
        self.HomeContent.setMaximumSize(QSize(2000, 2000))
        self.HomeWidget = QWidget(self.HomeContent)
        self.HomeWidget.setObjectName(u"HomeWidget")
        self.HomeWidget.setGeometry(QRect(0, 0, 591, 460))
        self.HomePic = QLabel(self.HomeWidget)
        self.HomePic.setObjectName(u"HomePic")
        self.HomePic.setGeometry(QRect(0, 0, 591, 461))
        self.HomePic.setPixmap(QPixmap(u"BusabaImages/HomePic.jpg"))
        self.Detail = QWidget(self.HomeContent)
        self.Detail.setObjectName(u"Detail")
        self.Detail.setGeometry(QRect(590, 0, 611, 471))
        self.HotelDescirption = QTextEdit(self.Detail)
        self.HotelDescirption.setObjectName(u"HotelDescirption")
        self.HotelDescirption.setGeometry(QRect(30, 10, 581, 331))
        self.HotelDescirption.setStyleSheet(u"QTextEdit { \n"
"	font: 10pt \"Maragsa\";\n"
"	color: rgb(1, 43, 64);\n"
"}")
        self.HotelDescirption.setReadOnly(True)
        self.pic1 = QLabel(self.Detail)
        self.pic1.setObjectName(u"pic1")
        self.pic1.setGeometry(QRect(30, 220, 185, 221))
        self.pic1.setStyleSheet(u"")
        self.pic1.setPixmap(QPixmap(u"BusabaImages/dorm.jpg"))
        self.pic2 = QLabel(self.Detail)
        self.pic2.setObjectName(u"pic2")
        self.pic2.setGeometry(QRect(230, 220, 185, 221))
        self.pic2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.pic2.setPixmap(QPixmap(u"BusabaImages/deluxe.jpg"))
        self.pic3 = QLabel(self.Detail)
        self.pic3.setObjectName(u"pic3")
        self.pic3.setGeometry(QRect(430, 220, 185, 221))
        self.pic3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.pic3.setPixmap(QPixmap(u"BusabaImages/superior.jpg"))
        self.mixedText = QLabel(self.Detail)
        self.mixedText.setObjectName(u"mixedText")
        self.mixedText.setGeometry(QRect(80, 450, 101, 20))
        self.mixedText.setStyleSheet(u"color: rgb(1, 41, 61);\n"
"font: 10pt \"Maragsa\";")
        self.deluxeText = QLabel(self.Detail)
        self.deluxeText.setObjectName(u"deluxeText")
        self.deluxeText.setGeometry(QRect(280, 450, 111, 20))
        self.deluxeText.setStyleSheet(u"color: rgb(1, 41, 61);\n"
"font: 10pt \"Maragsa\";")
        self.superiorText = QLabel(self.Detail)
        self.superiorText.setObjectName(u"superiorText")
        self.superiorText.setGeometry(QRect(470, 450, 121, 20))
        self.superiorText.setStyleSheet(u"color: rgb(1, 41, 61);\n"
"font: 10pt \"Maragsa\";")
        self.suggestLabel = QLabel(self.Detail)
        self.suggestLabel.setObjectName(u"suggestLabel")
        self.suggestLabel.setGeometry(QRect(20, 160, 221, 41))
        self.suggestLabel.setPixmap(QPixmap(u"BusabaImages/suggest_room.jpg"))
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(130, 150, 58, 16))
        self.label_11.setPixmap(QPixmap(u"../../../../../Busba-HomePageAesthetic/Busaba-HomePageCircle.png"))
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(-20, 170, 201, 321))
        self.label_12.setStyleSheet(u"QLabel{ \n"
"background-color: transparent;\n"
"\n"
"\n"
"}")
        self.label_12.setPixmap(QPixmap(u"BusabaImages/Busaba-HomePageCircle.png"))
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 190, 81, 51))
        font = QFont()
        font.setFamilies([u"Maragsa"])
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: transparent;\n"
"font: 17pt \"Maragsa\";")
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 230, 121, 51))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: transparent;\n"
"font: 17pt \"Maragsa\";")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 270, 141, 51))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background-color: transparent;\n"
"font: 17pt \"Maragsa\";")
        self.Pages.addWidget(self.Home)
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.label = QLabel(self.About)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-1, -10, 1291, 741))
        self.label.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"background-color: transparent;")
        self.label.setPixmap(QPixmap(u"BusabaImages/busabaAboutBG (1).png"))
        self.label_2 = QLabel(self.About)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 220, 401, 281))
        self.label_2.setPixmap(QPixmap(u"BusabaImages/AboutPic.png"))
        self.textEdit = QTextEdit(self.About)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 230, 481, 731))
        self.textEdit.setReadOnly(True)
        self.textEdit_2 = QTextEdit(self.About)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(950, 290, 271, 381))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_3 = QTextEdit(self.About)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(860, 460, 361, 151))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_4 = QTextEdit(self.About)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(590, 500, 581, 121))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_5 = QTextEdit(self.About)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(590, 580, 571, 171))
        self.textEdit_5.setReadOnly(True)
        self.Pages.addWidget(self.About)
        self.bookingSuccess = QWidget()
        self.bookingSuccess.setObjectName(u"bookingSuccess")
        self.widget_8 = QWidget(self.bookingSuccess)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 1279, 721))
        self.widget_8.setStyleSheet(u"QWidget{ \n"
"\n"
"background-color: white ;\n"
"\n"
"}")
        self.frame_12 = QFrame(self.widget_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(-1, 209, 1280, 511))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_46 = QLabel(self.frame_12)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, -40, 1280, 551))
        self.label_46.setPixmap(QPixmap(u"BusabaImages/busaba-purchaseSuccessfully(D).png"))
        self.BackHomeButton = QPushButton(self.frame_12)
        self.BackHomeButton.setObjectName(u"BackHomeButton")
        self.BackHomeButton.setGeometry(QRect(1180, 480, 75, 24))
        self.BackHomeButton.setStyleSheet(u"QPushButton{ \n"
"background-color:  rgb(3, 43, 61);\n"
"border:1px solid  rgb(14, 52, 70);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"")
        self.Pages.addWidget(self.bookingSuccess)
        self.ContactUs = QWidget()
        self.ContactUs.setObjectName(u"ContactUs")
        self.label_contactus = QLabel(self.ContactUs)
        self.label_contactus.setObjectName(u"label_contactus")
        self.label_contactus.setGeometry(QRect(0, 0, 1280, 720))
        self.label_contactus.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_contactus.setPixmap(QPixmap(u"BusabaImages/contactus.png"))
        self.Pages.addWidget(self.ContactUs)
        self.Booking = QWidget()
        self.Booking.setObjectName(u"Booking")
        self.widget = QWidget(self.Booking)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, 0, 1291, 721))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(40, 210, 1181, 471))
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 80, 321, 341))
        self.frame.setStyleSheet(u"QFrame{ \n"
"\n"
"border:1px solid  rgb(14, 52, 70);\n"
"\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 40, 321, 301))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 301, 191))
        self.label_4.setPixmap(QPixmap(u"BusabaImages/mixRoom_booking.jpg"))
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 200, 301, 91))
        self.frame_5.setStyleSheet(u"QFrame { \n"
"border: 0 px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 61, 16))
        self.label_5.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 91, 16))
        self.label_6.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 50, 81, 16))
        self.label_7.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 10, 111, 16))
        self.label_8.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 30, 191, 16))
        self.label_9.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(100, 50, 201, 16))
        self.label_10.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 321, 41))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Maragsa\";\n"
"	background-color: rgb(3, 43, 61);\n"
"}")
        self.mixAdd = QPushButton(self.widget_4)
        self.mixAdd.setObjectName(u"mixAdd")
        self.mixAdd.setGeometry(QRect(40, 420, 160, 41))
        self.mixAdd.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(3, 43, 61);\n"
"	font: 12pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	font: 12pt \"Maragsa\";\n"
"	color: rgb(3, 43, 61); \n"
"	background-color: rgb(218, 218, 218);\n"
"	border: 1px solid rgb(14, 52, 70); \n"
"\n"
"\n"
"}")
        self.mixBook = QPushButton(self.widget_4)
        self.mixBook.setObjectName(u"mixBook")
        self.mixBook.setGeometry(QRect(200, 420, 161, 41))
        self.mixBook.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 43, 61);\n"
"	font: 12pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Maragsa\";\n"
"	color: rgb(2, 43, 61); \n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(2, 43, 61); \n"
"\n"
"\n"
"}")
        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(430, 80, 321, 341))
        self.frame_2.setStyleSheet(u"QFrame{ \n"
"\n"
"border:1px solid  rgb(14, 52, 70);\n"
"\n"
"\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 40, 321, 301))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 301, 191))
        self.label_19.setPixmap(QPixmap(u"BusabaImages/deluxeRoom_booking.jpg"))
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 200, 301, 91))
        self.frame_9.setStyleSheet(u"QFrame { \n"
"border: 0 px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 81, 16))
        self.label_20.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 30, 91, 16))
        self.label_21.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 50, 81, 16))
        self.label_22.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(100, 10, 111, 16))
        self.label_23.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(100, 30, 191, 16))
        self.label_24.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_25 = QLabel(self.frame_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(100, 50, 201, 16))
        self.label_25.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_27 = QLabel(self.frame_9)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 70, 81, 16))
        self.label_27.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(100, 70, 201, 16))
        self.label_28.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 0, 321, 41))
        self.label_26.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Maragsa\";\n"
"	background-color: rgb(3, 43, 61);\n"
"}")
        self.deluxeAdd = QPushButton(self.widget_4)
        self.deluxeAdd.setObjectName(u"deluxeAdd")
        self.deluxeAdd.setGeometry(QRect(430, 420, 160, 41))
        self.deluxeAdd.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(3, 43, 61);\n"
"	font: 12pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Maragsa\";\n"
"	color: rgb(3, 43, 61); \n"
"	background-color: rgb(218, 218, 218);\n"
"	border: 1px solid rgb(14, 52, 70); \n"
"\n"
"\n"
"}")
        self.deluxeBook = QPushButton(self.widget_4)
        self.deluxeBook.setObjectName(u"deluxeBook")
        self.deluxeBook.setGeometry(QRect(590, 420, 161, 41))
        self.deluxeBook.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 43, 61);\n"
"	font: 12pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Maragsa\";\n"
"	color: rgb(2, 43, 61); \n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(2, 43, 61); \n"
"\n"
"\n"
"}")
        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(820, 80, 321, 341))
        self.frame_3.setStyleSheet(u"QFrame{ \n"
"\n"
"border:1px solid  rgb(14, 52, 70);\n"
"\n"
"\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 40, 321, 301))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_29 = QLabel(self.frame_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 301, 191))
        self.label_29.setPixmap(QPixmap(u"BusabaImages/superiorRoom_booking.jpg"))
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 200, 301, 91))
        self.frame_11.setStyleSheet(u"QFrame { \n"
"border: 0 px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 91, 16))
        self.label_31.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_32 = QLabel(self.frame_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 30, 81, 16))
        self.label_32.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_33 = QLabel(self.frame_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(100, 10, 111, 16))
        self.label_33.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_34 = QLabel(self.frame_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(100, 30, 191, 16))
        self.label_34.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_35 = QLabel(self.frame_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(100, 50, 201, 16))
        self.label_35.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_36 = QLabel(self.frame_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 50, 81, 16))
        self.label_36.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_37 = QLabel(self.frame_11)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(100, 70, 201, 16))
        self.label_37.setStyleSheet(u"QLabel{\n"
"border: 0 px; \n"
"color: rgb(3, 43, 61);\n"
"	font: 9pt \"Maragsa\";\n"
"}")
        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(0, 0, 321, 41))
        self.label_38.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Maragsa\";\n"
"	background-color: rgb(3, 43, 61);\n"
"}")
        self.superiorAdd = QPushButton(self.widget_4)
        self.superiorAdd.setObjectName(u"superiorAdd")
        self.superiorAdd.setGeometry(QRect(820, 420, 160, 41))
        self.superiorAdd.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(3, 43, 61);\n"
"	font: 12pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Maragsa\";\n"
"	color: rgb(3, 43, 61); \n"
"	background-color: rgb(218, 218, 218);\n"
"	border: 1px solid rgb(14, 52, 70); \n"
"\n"
"\n"
"}")
        self.superiorBook = QPushButton(self.widget_4)
        self.superiorBook.setObjectName(u"superiorBook")
        self.superiorBook.setGeometry(QRect(980, 420, 161, 41))
        self.superiorBook.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 43, 61);\n"
"	font: 12pt \"Maragsa\";\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	font: 12pt \"Maragsa\";\n"
"	color: rgb(2, 43, 61); \n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(2, 43, 61); \n"
"\n"
"\n"
"}")
        self.suggestLabel_2 = QLabel(self.widget_4)
        self.suggestLabel_2.setObjectName(u"suggestLabel_2")
        self.suggestLabel_2.setGeometry(QRect(-10, 0, 211, 51))
        self.suggestLabel_2.setPixmap(QPixmap(u"BusabaImages/suggest_room.jpg"))
        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(270, 20, 81, 31))
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(3, 43, 61);\n"
"	font: 11pt \"Adobe Devanagari\";\n"
"\n"
"}")
        self.dateEdit = QDateEdit(self.widget_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(360, 20, 141, 21))
        self.dateEdit.setStyleSheet(u"QDateEdit{ \n"
"    border:1 px solid  rgb(3, 43, 61);\n"
"	color: rgb(3, 43, 61);\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.dateEdit_3 = QDateEdit(self.widget_4)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(530, 20, 141, 21))
        self.dateEdit_3.setStyleSheet(u"QDateEdit{ \n"
"    border:1 px solid  rgb(3, 43, 61);\n"
"	color: rgb(3, 43, 61);\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.label_40 = QLabel(self.widget_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(510, 20, 16, 16))
        self.label_40.setStyleSheet(u"QLabel{\n"
"	color: rgb(3, 43, 61);\n"
"	font: 11pt \"Adobe Devanagari\";\n"
"\n"
"}")
        self.superiorBook.raise_()
        self.superiorAdd.raise_()
        self.frame.raise_()
        self.mixAdd.raise_()
        self.mixBook.raise_()
        self.frame_2.raise_()
        self.deluxeAdd.raise_()
        self.deluxeBook.raise_()
        self.frame_3.raise_()
        self.suggestLabel_2.raise_()
        self.label_30.raise_()
        self.dateEdit.raise_()
        self.dateEdit_3.raise_()
        self.label_40.raise_()
        self.cartWidget = QWidget(self.widget)
        self.cartWidget.setObjectName(u"cartWidget")
        self.cartWidget.setGeometry(QRect(920, 269, 0, 421))
        self.cartWidget.setStyleSheet(u"QWidget{ \n"
"	border-radius:50px;\n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border: 1px solid black \n"
"	\n"
"} \n"
"\n"
"")
        self.label_41 = QLabel(self.cartWidget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(50, 20, 131, 31))
        self.label_41.setStyleSheet(u"QLabel{ \n"
"border: 0px ;\n"
"font: 12pt \"Maragsa\";\n"
"	color: rgb(4, 54, 76);\n"
"\n"
"}")
        self.label_42 = QLabel(self.cartWidget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(50, 70, 281, 31))
        self.label_42.setStyleSheet(u"QLabel{ \n"
"border: 0px ;\n"
"font: 11pt \"Maragsa\";\n"
"background-color: rgb(4,54,76);\n"
"color: rgb(255 ,255, 255);\n"
"\n"
"}")
        self.ProceedButton = QPushButton(self.cartWidget)
        self.ProceedButton.setObjectName(u"ProceedButton")
        self.ProceedButton.setGeometry(QRect(140, 350, 121, 31))
        self.ProceedButton.setStyleSheet(u"QPushButton{ \n"
"border:1px solid  rgb(14, 52, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 43, 61);\n"
"	font: 11pt \"Maragsa\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 11pt \"Maragsa\";\n"
"	color: rgb(2, 43, 61); \n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(2, 43, 61); \n"
"\n"
"\n"
"}")
        self.cartCloseButton = QPushButton(self.cartWidget)
        self.cartCloseButton.setObjectName(u"cartCloseButton")
        self.cartCloseButton.setGeometry(QRect(331, 10, 20, 31))
        self.cartCloseButton.setStyleSheet(u"QPushButton { \n"
"border: 0 px solid ;\n"
"\n"
"\n"
"}")
        self.itemCart = QWidget(self.cartWidget)
        self.itemCart.setObjectName(u"itemCart")
        self.itemCart.setGeometry(QRect(20, 120, 341, 201))
        self.itemCart.setStyleSheet(u"QWidget{ \n"
"border: 0px\n"
"\n"
"\n"
"}")
        self.resetCartButton = QPushButton(self.cartWidget)
        self.resetCartButton.setObjectName(u"resetCartButton")
        self.resetCartButton.setGeometry(QRect(270, 350, 31, 31))
        self.resetCartButton.setStyleSheet(u"QPushButton { \n"
"border: 0 px;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"BusabaImages/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetCartButton.setIcon(icon)
        self.resetCartButton.setIconSize(QSize(31, 31))
        self.cartButton = QPushButton(self.widget)
        self.cartButton.setObjectName(u"cartButton")
        self.cartButton.setGeometry(QRect(1240, 10, 51, 41))
        icon1 = QIcon()
        icon1.addFile(u"BusabaImages/cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cartButton.setIcon(icon1)
        self.cartButton.setIconSize(QSize(41, 41))
        self.Pages.addWidget(self.Booking)
        self.Payment = QWidget()
        self.Payment.setObjectName(u"Payment")
        self.widget_5 = QWidget(self.Payment)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 1280, 720))
        self.widget_5.setStyleSheet(u"QWidget {\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.OverallWidget = QWidget(self.widget_5)
        self.OverallWidget.setObjectName(u"OverallWidget")
        self.OverallWidget.setGeometry(QRect(50, 270, 621, 401))
        self.OverallWidget.setStyleSheet(u"QWidget{ \n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius:20px;\n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border: 1px solid  rgb(0, 0, 76);\n"
"\n"
"	\n"
"	\n"
"} ")
        self.line = QFrame(self.OverallWidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 350, 621, 1))
        self.line.setStyleSheet(u"QFrame { \n"
"border-radius : 0px\n"
"\n"
"}")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)
        self.order_payment = QWidget(self.OverallWidget)
        self.order_payment.setObjectName(u"order_payment")
        self.order_payment.setGeometry(QRect(10, 10, 601, 331))
        self.order_payment.setStyleSheet(u"QWidget{ \n"
"\n"
"border : 0px\n"
"\n"
"}")
        self.TotalPrice = QLabel(self.OverallWidget)
        self.TotalPrice.setObjectName(u"TotalPrice")
        self.TotalPrice.setGeometry(QRect(180, 360, 81, 31))
        self.TotalPrice.setStyleSheet(u"QLabel { \n"
"border: 0 px; \n"
"	font: 13pt \"Maragsa\";\n"
"\n"
"}")
        self.Currency = QLabel(self.OverallWidget)
        self.Currency.setObjectName(u"Currency")
        self.Currency.setGeometry(QRect(410, 370, 21, 16))
        self.Currency.setStyleSheet(u"QLabel { \n"
"border: 0 px; \n"
"	font: 15pt \"Maragsa\";\n"
"\n"
"}")
        self.priceLabel = QLabel(self.OverallWidget)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setGeometry(QRect(290, 370, 111, 16))
        self.priceLabel.setStyleSheet(u"QLabel { \n"
"border: 0 px; \n"
"	font: 13pt \"Maragsa\";\n"
"\n"
"}")
        self.PaymentMethod = QWidget(self.widget_5)
        self.PaymentMethod.setObjectName(u"PaymentMethod")
        self.PaymentMethod.setGeometry(QRect(780, 360, 421, 111))
        self.PaymentMethod.setStyleSheet(u"QWidget{ \n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius:0px;\n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(0,0,0);\n"
"	border: 1px solid  rgb(0, 0, 76);\n"
"\n"
"	\n"
"	\n"
"} ")
        self.radioButton = QRadioButton(self.PaymentMethod)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 20, 101, 21))
        self.radioButton.setStyleSheet(u"QRadioButton{ \n"
"border : 0 px;\n"
"	font: 9pt \"Maragsa\";\n"
"\n"
"}")
        self.radioButton_2 = QRadioButton(self.PaymentMethod)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 70, 91, 20))
        self.radioButton_2.setStyleSheet(u"QRadioButton{ \n"
"border : 0 px;\n"
"	font: 9pt \"Maragsa\";\n"
"\n"
"}")
        self.label_39 = QLabel(self.PaymentMethod)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(110, 20, 51, 31))
        self.label_39.setPixmap(QPixmap(u"BusabaImages/mastercard.png"))
        self.label_43 = QLabel(self.PaymentMethod)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(180, 20, 61, 31))
        self.label_43.setPixmap(QPixmap(u"BusabaImages/visa.png"))
        self.PaymentButton = QPushButton(self.widget_5)
        self.PaymentButton.setObjectName(u"PaymentButton")
        self.PaymentButton.setGeometry(QRect(910, 490, 171, 21))
        self.PaymentButton.setStyleSheet(u"QPushButton{ \n"
"	font: 13pt \"Maragsa\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 43, 61);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 13pt \"Maragsa\";\n"
"	color: rgb(2, 43, 61); \n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(2, 43, 61); \n"
"\n"
"}")
        self.ReturnCartButton = QPushButton(self.widget_5)
        self.ReturnCartButton.setObjectName(u"ReturnCartButton")
        self.ReturnCartButton.setGeometry(QRect(910, 520, 171, 21))
        self.ReturnCartButton.setStyleSheet(u"QPushButton{ \n"
"	font: 13pt \"Maragsa\";\n"
"	color: rgb(2, 43, 61); \n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(2, 43, 61); \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 13pt \"Maragsa\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 43, 61);\n"
"\n"
"}")
        self.Pages.addWidget(self.Payment)
        self.MyBookingPage = QWidget()
        self.MyBookingPage.setObjectName(u"MyBookingPage")
        self.widget_6 = QWidget(self.MyBookingPage)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 0, 1281, 721))
        self.widget_6.setStyleSheet(u"QWidget { \n"
"\n"
"background-color: rgb(255,255,255) ;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(1263, 290))
        self.widget_7.setMaximumSize(QSize(1263, 250))
        self.widget_7.setStyleSheet(u"QWidget: { \n"
"border:1px solid rgb(0, 48, 145);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.MyBookingLabel = QLabel(self.widget_7)
        self.MyBookingLabel.setObjectName(u"MyBookingLabel")
        self.MyBookingLabel.setGeometry(QRect(180, 230, 121, 51))
        self.MyBookingLabel.setPixmap(QPixmap(u"BusabaImages/myBookingLabel.jpg"))
        self.cancel = QLabel(self.widget_7)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(710, 240, 81, 31))
        self.cancel.setStyleSheet(u"QLabel { \n"
"border: 0 px; \n"
"font: 13pt \"Maragsa\"; \n"
"color: rgb(0, 48, 145);\n"
"}")
        self.comboBox = QComboBox(self.widget_7)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(810, 241, 141, 31))
        self.comboBox.setStyleSheet(u"QComboBox: { \n"
"border:1px solid rgb(0, 48, 145);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.confirmCancelButton = QPushButton(self.widget_7)
        self.confirmCancelButton.setObjectName(u"confirmCancelButton")
        self.confirmCancelButton.setGeometry(QRect(960, 240, 61, 31))
        self.confirmCancelButton.setMinimumSize(QSize(31, 31))
        self.confirmCancelButton.setMaximumSize(QSize(234, 234))
        self.confirmCancelButton.setStyleSheet(u"QPushButton{ \n"
"\n"
"color: rgb(0, 0, 98);\n"
"} \n"
"\n"
"QPushBuutton : hover { \n"
"	background-color: rgb(218, 218, 218);\n"
"\n"
"} ")
        self.confirmCancelButton.setIconSize(QSize(41, 41))

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_3 = QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_9 = QWidget(self.widget_10)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.widget_9)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(900, 350))
        self.scrollArea.setMaximumSize(QSize(900, 350))
        self.scrollArea.setStyleSheet(u"QScrollArea { \n"
"border:1px solid black ;\n"
"background-color: rgb(245, 245, 245);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 888, 1568))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BookingWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.BookingWidget.setObjectName(u"BookingWidget")
        self.BookingWidget.setMinimumSize(QSize(870, 1550))
        self.BookingWidget.setMaximumSize(QSize(870, 1550))

        self.verticalLayout_4.addWidget(self.BookingWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.widget_9)


        self.verticalLayout_2.addWidget(self.widget_10)

        self.Pages.addWidget(self.MyBookingPage)
        self.InfoEdit = QWidget()
        self.InfoEdit.setObjectName(u"InfoEdit")
        self.InfoEditWidget = QWidget(self.InfoEdit)
        self.InfoEditWidget.setObjectName(u"InfoEditWidget")
        self.InfoEditWidget.setGeometry(QRect(0, 0, 1281, 721))
        self.InfoEditLabel = QLabel(self.InfoEditWidget)
        self.InfoEditLabel.setObjectName(u"InfoEditLabel")
        self.InfoEditLabel.setGeometry(QRect(0, 0, 1280, 720))
        self.InfoEditLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.InfoEditLabel.setPixmap(QPixmap(u"BusabaImages/busabaInformationBG-01.png"))
        self.InfoEditContent = QWidget(self.InfoEditWidget)
        self.InfoEditContent.setObjectName(u"InfoEditContent")
        self.InfoEditContent.setGeometry(QRect(310, 270, 661, 381))
        self.InfoEditContent.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.NameInfoEdit = QLabel(self.InfoEditContent)
        self.NameInfoEdit.setObjectName(u"NameInfoEdit")
        self.NameInfoEdit.setGeometry(QRect(50, 30, 51, 41))
        self.NameInfoEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.SurnameInfoEdit = QLabel(self.InfoEditContent)
        self.SurnameInfoEdit.setObjectName(u"SurnameInfoEdit")
        self.SurnameInfoEdit.setGeometry(QRect(350, 30, 71, 41))
        self.SurnameInfoEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.BirthDateInfoEdit = QLabel(self.InfoEditContent)
        self.BirthDateInfoEdit.setObjectName(u"BirthDateInfoEdit")
        self.BirthDateInfoEdit.setGeometry(QRect(50, 220, 81, 41))
        self.BirthDateInfoEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.PhoneNumInfoEdit = QLabel(self.InfoEditContent)
        self.PhoneNumInfoEdit.setObjectName(u"PhoneNumInfoEdit")
        self.PhoneNumInfoEdit.setGeometry(QRect(50, 280, 71, 41))
        self.PhoneNumInfoEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.EmailInfoEdit = QLabel(self.InfoEditContent)
        self.EmailInfoEdit.setObjectName(u"EmailInfoEdit")
        self.EmailInfoEdit.setGeometry(QRect(330, 280, 51, 41))
        self.EmailInfoEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.NameEdit = QLineEdit(self.InfoEditContent)
        self.NameEdit.setObjectName(u"NameEdit")
        self.NameEdit.setGeometry(QRect(100, 40, 201, 21))
        self.NameEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.SurnameEdit = QLineEdit(self.InfoEditContent)
        self.SurnameEdit.setObjectName(u"SurnameEdit")
        self.SurnameEdit.setGeometry(QRect(420, 40, 201, 21))
        self.SurnameEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.PhoneNumEdit = QLineEdit(self.InfoEditContent)
        self.PhoneNumEdit.setObjectName(u"PhoneNumEdit")
        self.PhoneNumEdit.setGeometry(QRect(120, 290, 171, 21))
        self.PhoneNumEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.EmailEdit = QLineEdit(self.InfoEditContent)
        self.EmailEdit.setObjectName(u"EmailEdit")
        self.EmailEdit.setGeometry(QRect(380, 290, 241, 21))
        self.EmailEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.dateEdit_2 = QDateEdit(self.InfoEditContent)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(140, 230, 221, 21))
        self.dateEdit_2.setStyleSheet(u"color: rgb(2, 43, 61);  \n"
"border-radius: 7px;\n"
"border: 0.5px solid rgb(0,0,0);")
        self.PasswordLabel = QLabel(self.InfoEditContent)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setGeometry(QRect(50, 90, 81, 41))
        self.PasswordLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.PasswordEdit = QLineEdit(self.InfoEditContent)
        self.PasswordEdit.setObjectName(u"PasswordEdit")
        self.PasswordEdit.setGeometry(QRect(150, 100, 201, 21))
        self.PasswordEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.ConfirmPassLabel = QLabel(self.InfoEditContent)
        self.ConfirmPassLabel.setObjectName(u"ConfirmPassLabel")
        self.ConfirmPassLabel.setGeometry(QRect(50, 150, 121, 41))
        self.ConfirmPassLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.ComfirmPassEdit = QLineEdit(self.InfoEditContent)
        self.ComfirmPassEdit.setObjectName(u"ComfirmPassEdit")
        self.ComfirmPassEdit.setGeometry(QRect(180, 160, 201, 21))
        self.ComfirmPassEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.BackButton = QPushButton(self.InfoEditWidget)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(770, 650, 91, 41))
        self.BackButton.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.SaveButton = QPushButton(self.InfoEditWidget)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(880, 660, 75, 24))
        self.SaveButton.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Pages.addWidget(self.InfoEdit)
        self.InfoPage = QWidget()
        self.InfoPage.setObjectName(u"InfoPage")
        self.InfoWidget = QWidget(self.InfoPage)
        self.InfoWidget.setObjectName(u"InfoWidget")
        self.InfoWidget.setGeometry(QRect(0, 0, 1280, 720))
        self.InfoLabel = QLabel(self.InfoWidget)
        self.InfoLabel.setObjectName(u"InfoLabel")
        self.InfoLabel.setGeometry(QRect(-1, 0, 1291, 720))
        self.InfoLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.InfoLabel.setPixmap(QPixmap(u"BusabaImages/busabaInformationBG-01.png"))
        self.InfoContent = QWidget(self.InfoWidget)
        self.InfoContent.setObjectName(u"InfoContent")
        self.InfoContent.setGeometry(QRect(310, 270, 661, 381))
        self.InfoContent.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.NameInfo = QLabel(self.InfoContent)
        self.NameInfo.setObjectName(u"NameInfo")
        self.NameInfo.setGeometry(QRect(50, 80, 41, 41))
        self.NameInfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.NameLabel = QLabel(self.InfoContent)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setGeometry(QRect(100, 90, 201, 21))
        self.NameLabel.setStyleSheet(u"QLabel{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.SurnameLabel = QLabel(self.InfoContent)
        self.SurnameLabel.setObjectName(u"SurnameLabel")
        self.SurnameLabel.setGeometry(QRect(420, 90, 201, 21))
        self.SurnameLabel.setStyleSheet(u"QLabel{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.SurnameInfo = QLabel(self.InfoContent)
        self.SurnameInfo.setObjectName(u"SurnameInfo")
        self.SurnameInfo.setGeometry(QRect(350, 80, 61, 41))
        self.SurnameInfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.BirthDateInfo = QLabel(self.InfoContent)
        self.BirthDateInfo.setObjectName(u"BirthDateInfo")
        self.BirthDateInfo.setGeometry(QRect(50, 140, 81, 41))
        self.BirthDateInfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.PhoneNumInfo = QLabel(self.InfoContent)
        self.PhoneNumInfo.setObjectName(u"PhoneNumInfo")
        self.PhoneNumInfo.setGeometry(QRect(50, 200, 71, 41))
        self.PhoneNumInfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.PhoneLabel = QLabel(self.InfoContent)
        self.PhoneLabel.setObjectName(u"PhoneLabel")
        self.PhoneLabel.setGeometry(QRect(120, 210, 171, 21))
        self.PhoneLabel.setStyleSheet(u"QLabel{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.EmailInfo = QLabel(self.InfoContent)
        self.EmailInfo.setObjectName(u"EmailInfo")
        self.EmailInfo.setGeometry(QRect(330, 200, 51, 41))
        self.EmailInfo.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.EmailLabel = QLabel(self.InfoContent)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setGeometry(QRect(380, 210, 241, 21))
        self.EmailLabel.setStyleSheet(u"QLabel{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.AccountID = QLabel(self.InfoContent)
        self.AccountID.setObjectName(u"AccountID")
        self.AccountID.setGeometry(QRect(50, 30, 71, 41))
        self.AccountID.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 11pt \"Maragsa\";")
        self.BirthDateEdit = QLineEdit(self.InfoContent)
        self.BirthDateEdit.setObjectName(u"BirthDateEdit")
        self.BirthDateEdit.setGeometry(QRect(140, 150, 221, 21))
        self.BirthDateEdit.setStyleSheet(u"QLineEdit{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:focus{ \n"
"border:2px solid rgb(2, 43, 61) ;\n"
"\n"
"}")
        self.AccountIDLabel = QLabel(self.InfoContent)
        self.AccountIDLabel.setObjectName(u"AccountIDLabel")
        self.AccountIDLabel.setGeometry(QRect(130, 40, 211, 21))
        self.AccountIDLabel.setStyleSheet(u"QLabel{ \n"
"border-radius:7px;\n"
"border:0.5px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.EditButton = QPushButton(self.InfoWidget)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setGeometry(QRect(890, 650, 75, 24))
        self.EditButton.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Pages.addWidget(self.InfoPage)
        self.Logo = QLabel(self.widget_2)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(490, -30, 291, 161))
        self.Logo.setStyleSheet(u"")
        self.Logo.setPixmap(QPixmap(u"BusabaImages/Busaba03.png"))
        self.LeftMenu = QWidget(self.widget_2)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.LeftMenu.setGeometry(QRect(890, 210, 161, 0))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftMenu.sizePolicy().hasHeightForWidth())
        self.LeftMenu.setSizePolicy(sizePolicy)
        self.LeftMenu.setMinimumSize(QSize(161, 0))
        self.LeftMenu.setMaximumSize(QSize(161, 0))
        self.LeftMenu.setStyleSheet(u"background-color: rgb(1, 43, 62);")
        self.verticalLayout = QVBoxLayout(self.LeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Info = QPushButton(self.LeftMenu)
        self.Info.setObjectName(u"Info")
        self.Info.setStyleSheet(u"\n"
"\n"
"QPushButton{ \n"
"	font: 10pt\"Maragsa\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(1, 43, 62);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(1, 43, 62);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(255,255,255);  \n"
"}\n"
"\n"
"\n"
"	")

        self.verticalLayout.addWidget(self.Info)

        self.MyBooking = QPushButton(self.LeftMenu)
        self.MyBooking.setObjectName(u"MyBooking")
        self.MyBooking.setStyleSheet(u"\n"
"\n"
"QPushButton{ \n"
"	font: 10pt\"Maragsa\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(1, 43, 62);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(1, 43, 62);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(255,255,255);  \n"
"}\n"
"\n"
"\n"
"	")

        self.verticalLayout.addWidget(self.MyBooking)

        self.LogOut = QPushButton(self.LeftMenu)
        self.LogOut.setObjectName(u"LogOut")
        self.LogOut.setStyleSheet(u"\n"
"\n"
"QPushButton{ \n"
"	font: 10pt\"Maragsa\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(1, 43, 62);\n"
"	border-bottom: 0.5px solid transparent \n"
"	\n"
"} \n"
"\n"
"QPushButton:hover{ \n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(1, 43, 62);\n"
"} \n"
"\n"
"QPushButton:pressed{ \n"
"	background-color:rgb(255,255,255);  \n"
"}\n"
"\n"
"\n"
"	")

        self.verticalLayout.addWidget(self.LogOut)

        self.Pages.raise_()
        self.LeftMenu.raise_()
        self.Logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_2.raise_()
        self.MenuBar.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.ContactButton.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.BookingButton.setText(QCoreApplication.translate("MainWindow", u"Booking", None))
        self.AccountButton.setText(QCoreApplication.translate("MainWindow", u"My Account", None))
        self.HomePic.setText("")
        self.HotelDescirption.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Maragsa'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:10px;\"><span style=\" font-size:12pt; font-weight:200;\">BUSABA  is  modernizing  an  old  Thai  house  by  the  water  into  a  conceptual   hotel  celebrates  Thainess  and  typical  Thai  lifestyles.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:20px;\"><span style=\" font-size:12pt; f"
                        "ont-weight:200;\">in  the  central  region   of  Thailand,  it  is  customary  for  individuals  to  build  their  homes   in  clusters  that  reflect  their  extended  family  tree. This  traditional  is  typically  observed  when  someone  in  the  family  gets  married,  prompting  the construction  of  a  new  house. The  houses  are  built  in  close  proximity  to  each  other  with  a  central  patio,  which  serves  as  a  communal  area  for  family members  together.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:200;\"><br /></span></p></body></html>", None))
        self.pic1.setText("")
        self.pic2.setText("")
        self.pic3.setText("")
        self.mixedText.setText(QCoreApplication.translate("MainWindow", u"MIXED DORM", None))
        self.deluxeText.setText(QCoreApplication.translate("MainWindow", u"DELUXE ROOM", None))
        self.superiorText.setText(QCoreApplication.translate("MainWindow", u"SUPERIOR ROOM", None))
        self.suggestLabel.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"AYUTTHAYA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"EXPERIENCE", None))
        self.label.setText("")
        self.label_2.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Maragsa'; font-size:28pt;\">&quot; Busaba  Ayutthaya  Hotel  was  inspired  by  the  rich  cultural  heritage  of  Ayutthaya, Thailand.  The  city  is  known  for  its  ancient  temples,  vibrant  markets, and  stunning  architecture,                                           and  we wanted  to  capture  the  essence  of  this  beautiful  place  in  our  hotel. &quot;</span"
                        "></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Maragsa'; font-size:13pt;\">Our  design  team  drew  insipiration  from  traditional  Thai  architecture,  incorporatinng  intricate  wood  carvings,  ornate  roofs,  and  elegant  arches  into  the  building's  structure.  The  result  is  a  modern  hotel  that  retians  the  charm  and  character  of  old - world  Thailand.    </span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Maragsa'; font-size:13pt;\">                    At  Busaba  Ayutthaya  Hotel,  we're  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Maragsa'; font-size:12pt;\">     passionate  about  hospitality.  Our team  of</span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Maragsa'; font-size:13pt;\">experienced  professionals  is  dedicated  to  providing  our  guests  with  the  highest  level  of  service  and  business  trip, we're  recommitted  to  making  your  stay  as  comfortable  and  enjoyable  as  possible.</span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Maragsa'; font-size:13pt;\">We're  proud  to  be  located  in  the  heart  of  Ayutthaya,  just  steps  away  from the  city's  top  attractions,  including  the  ancient  temples, night  merkets, and  local  restaurants. We  invite  you  to  come  and  experience  the  magicc  of  Ayutthaya  at Busaba  Ayutthaya  Hotel.</span></p></body></html>", None))
        self.label_46.setText("")
        self.BackHomeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_contactus.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u2022Free WiFi", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u2022Free Breafast", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u2022Non-Smoking", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u2022Air Conditioning", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u2022Secure Lockers for each guests", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u2022Privacy Curtains for each bunk bed", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MIXED DORM", None))
        self.mixAdd.setText(QCoreApplication.translate("MainWindow", u"ADD TO CART", None))
        self.mixBook.setText(QCoreApplication.translate("MainWindow", u"BOOK NOW", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u2022King-Sized bed", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u2022Free WiFi", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u2022Free Breakfast", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u2022Soundproofed room", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u2022Large flast-screen TV", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u2022Smoking Allowed", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u2022Free Breakfast", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u2022Air Conditioning", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"DELUXE ROOM", None))
        self.deluxeAdd.setText(QCoreApplication.translate("MainWindow", u"ADD TO CART", None))
        self.deluxeBook.setText(QCoreApplication.translate("MainWindow", u"BOOK NOW", None))
        self.label_29.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u2022Free WiFi", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u2022Free Breakfast", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u2022Air Conditioning", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u2022Baby Cribs or Cots", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u2022Child-Friendly amenities ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u2022Non-Smoking", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u" such as games, toys and books", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"SUPERIOR ROOM", None))
        self.superiorAdd.setText(QCoreApplication.translate("MainWindow", u"ADD TO CART", None))
        self.superiorBook.setText(QCoreApplication.translate("MainWindow", u"BOOK NOW", None))
        self.suggestLabel_2.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Booking Date", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"ADDED  TO  CART", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"   ROOMTYPE                   AMOUNT                 PRICE", None))
        self.ProceedButton.setText(QCoreApplication.translate("MainWindow", u"Proceed to cart", None))
        self.cartCloseButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.resetCartButton.setText("")
        self.cartButton.setText("")
        self.TotalPrice.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.Currency.setText(QCoreApplication.translate("MainWindow", u"\u0e3f", None))
        self.priceLabel.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Credit Card", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.label_39.setText("")
        self.label_43.setText("")
        self.PaymentButton.setText(QCoreApplication.translate("MainWindow", u"MAKE A PAYMENT", None))
        self.ReturnCartButton.setText(QCoreApplication.translate("MainWindow", u"Return to Cart", None))
        self.MyBookingLabel.setText("")
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel on:", None))
        self.confirmCancelButton.setText(QCoreApplication.translate("MainWindow", u"\u2714 confirm", None))
        self.InfoEditLabel.setText("")
        self.NameInfoEdit.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.SurnameInfoEdit.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.BirthDateInfoEdit.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.PhoneNumInfoEdit.setText(QCoreApplication.translate("MainWindow", u"Phone No.", None))
        self.EmailInfoEdit.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.ConfirmPassLabel.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.BackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.InfoLabel.setText("")
        self.NameInfo.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.NameLabel.setText("")
        self.SurnameLabel.setText("")
        self.SurnameInfo.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.BirthDateInfo.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.PhoneNumInfo.setText(QCoreApplication.translate("MainWindow", u"Phone No.", None))
        self.PhoneLabel.setText("")
        self.EmailInfo.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.EmailLabel.setText("")
        self.AccountID.setText(QCoreApplication.translate("MainWindow", u"Account ID", None))
        self.AccountIDLabel.setText("")
        self.EditButton.setText(QCoreApplication.translate("MainWindow", u"Edit ", None))
        self.Logo.setText("")
        self.Info.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.MyBooking.setText(QCoreApplication.translate("MainWindow", u"My booking", None))
        self.LogOut.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
    # retranslateUi

