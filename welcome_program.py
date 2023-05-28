import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from BusabaWelcome import Ui_Form_BusabaWelcomePage


class Welcome(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form_BusabaWelcomePage()
        self.ui.setupUi(self)

        self.ui.pushButton_signInWelcomePage.clicked.connect(lambda: self.goto_sign_in0())
        self.ui.pushButton_signUpWelcomePage.clicked.connect(lambda: self.goto_register0())
    
    def goto_sign_in0(self):
        from loginProgram import Login
        self.close()

        self.login_window = Login()
        self.login_window.show()
            
    def goto_register0(self):
        from registerProgram import Register
        self.close()

        self.register_window = Register()
        self.register_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_window = Welcome()
    welcome_window.show()

    sys.exit(app.exec())