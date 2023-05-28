import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from BusabaLogin import Ui_Form_Login
from PySide6.QtWidgets import QVBoxLayout

from account import Account


class Login(QMainWindow, Account):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form_Login()
        self.ui.setupUi(self)

        # # Create a central widget and set its layout
        # central_widget = QWidget()
        # central_widget.setLayout(Ui_Form)

        # # Set the central widget of the main window
        # self.setCentralWidget(central_widget)

        self.ui.pushButton_signIn.clicked.connect(lambda: self.handle_login())
        self.ui.pushButton_gotoSignUp.clicked.connect(lambda: self.goto_register1())

    def handle_login(self):
        user_name = self.ui.lineEdit_username.text()
        user_password = self.ui.lineEdit_password.text()
        if self.logIn_valid(user_name, user_password):
            print(user_name)
            print(user_password)
            # QMessageBox.information(self, "Success", "Login successful!")
            from Home import Home
            self.close()

            self.home_window = Home()
            self.home_window.show()
        else:
            print(user_name)
            print(user_password)
            QMessageBox.warning(self, "Error", "Invalid username or password.")
            
    def goto_register1(self):
        from registerProgram import Register
        self.close()

        self.register_window = Register()
        self.register_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()

    sys.exit(app.exec())