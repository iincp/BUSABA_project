# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BusabaWelcome.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form_BusabaWelcomePage(object):
    def setupUi(self, Form_BusabaWelcomePage):
        if not Form_BusabaWelcomePage.objectName():
            Form_BusabaWelcomePage.setObjectName(u"Form_BusabaWelcomePage")
        Form_BusabaWelcomePage.resize(1280, 720)
        self.label = QLabel(Form_BusabaWelcomePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1281, 721))
        self.label.setPixmap(QPixmap(u"BusabaImages/busaba-welcome.png"))
        self.pushButton_signInWelcomePage = QPushButton(Form_BusabaWelcomePage)
        self.pushButton_signInWelcomePage.setObjectName(u"pushButton_signInWelcomePage")
        self.pushButton_signInWelcomePage.setGeometry(QRect(570, 531, 141, 51))
        self.pushButton_signInWelcomePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_signInWelcomePage.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.pushButton_signUpWelcomePage = QPushButton(Form_BusabaWelcomePage)
        self.pushButton_signUpWelcomePage.setObjectName(u"pushButton_signUpWelcomePage")
        self.pushButton_signUpWelcomePage.setGeometry(QRect(570, 590, 141, 41))
        self.pushButton_signUpWelcomePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_signUpWelcomePage.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"}\n"
"")

        self.retranslateUi(Form_BusabaWelcomePage)

        QMetaObject.connectSlotsByName(Form_BusabaWelcomePage)
    # setupUi

    def retranslateUi(self, Form_BusabaWelcomePage):
        Form_BusabaWelcomePage.setWindowTitle(QCoreApplication.translate("Form_BusabaWelcomePage", u"Form", None))
        self.label.setText("")
        self.pushButton_signInWelcomePage.setText("")
        self.pushButton_signUpWelcomePage.setText("")
    # retranslateUi

