import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from welcome_program import Welcome
from account import Account
account = Account()


class Main(Welcome):
    def __init__(self):
        super().__init__()

        # Set Login window as the central widget
        # self.login_window = Login()

        # self.setCentralWidget(self.login_window)

        # # Center the window on the screen
        # screen_geometry = QGuiApplication.primaryScreen().geometry()
        # width, height = self.login_window.width(), self.login_window.height()
        # self.setGeometry(screen_geometry.width()//2 - width//2,
        #                  screen_geometry.height()//2 - height//2,
        #                  width, height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())
