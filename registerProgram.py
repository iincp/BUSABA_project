import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from BusabaRegister import Ui_Form
from details_verifier import DetailsVerifier
from multiprocessing import connection
from typing import *
from persistent.mapping import PersistentMapping

class Register(QMainWindow, DetailsVerifier):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_SignUp.clicked.connect(self.handle_signUp)
        self.ui.pushButton_gotoSignIn.clicked.connect(self.goto_logIn)
        self.ui.pushButton_termsAndServices.clicked.connect(self.show_terms)

    def handle_signUp(self):
        # Retrieve user input from the QLineEdit fields on the register page
        user_name = self.ui.lineEdit_username.text()
        user_Fname = self.ui.lineEdit_name.text()
        user_Sname = self.ui.lineEdit_surname.text()
        user_tel = self.ui.lineEdit_phoneNumber.text()
        user_email = self.ui.lineEdit_email.text()
        user_password = self.ui.lineEdit_password.text()
        user_birth = self.ui.dateEdit_dateOfBirth.date().toString("yyyy-MM-dd")

        try:
            # Verify details for registration
            self.verify_details_for_register(
                user_name, user_email, user_tel, user_password)

            if self.terms_agreed():
                self.register(user_name, user_Fname, user_Sname,
                                      user_tel, user_email, user_password, user_birth)
                QMessageBox.information(
                    self, "Success", "Registration successful. Please log in.")
                self.clear_fields()
            else:
                QMessageBox.information(
                    self, "Failed", "Registration Failed. Please agree to our Terms and Services.")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def terms_agreed(self):
        return self.ui.checkBox_agreeOurTerms.isChecked()

    def clear_fields(self):
        self.ui.lineEdit_username.clear()
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_surname.clear()
        self.ui.lineEdit_phoneNumber.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_password.clear()
        self.ui.dateEdit_dateOfBirth.setDate(QDate.currentDate())

    def goto_logIn(self):
        from loginProgram import Login
        self.close()
        self.logIn_window = Login()
        self.logIn_window.show()

    def show_terms(self):
        QMessageBox.information(
            self, "Terms and Services", "Lorem ipsum dolor sit amet asda kimito yulo.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register_window = Register()
    register_window.show()

    sys.exit(app.exec())

# def logIn_valid(self, user_name, user_password):
#     if 'user_acc_info' in self.root:
#         user_acc_info = self.root
#         for user in user_acc_info.values():
#             if user['user_name'] == user_name:
#                 stored_password = user.get('user_password')
#                 if stored_password == user_password:
#                     return True
#                 else:
#                     return False
#     else:
#         return False
