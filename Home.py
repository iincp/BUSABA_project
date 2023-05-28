import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtGui import *
from HomeUi import Ui_MainWindow
from details_verifier import DetailsVerifier 
from booking import BookingSystem 
import re



class Home(QMainWindow, DetailsVerifier):
    payment_status = None 
    b = BookingSystem()
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.itemIdex = 0 

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.LeftMenu.setMaximumHeight(221)
        # self.ui.LeftMenu.setMinimumHeight(0) 
        self.ui.confirmCancelButton.setVisible(False)
        # set default page
        self.ui.Pages.setCurrentWidget(self.ui.Home)
        # cartwidgetlayout
        self.layout = QVBoxLayout(self.ui.itemCart)
        # overall oreder widgetlayout
        self.verticalLayout_2 = QVBoxLayout(self.ui.order_payment)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.layout2 = QVBoxLayout(self.ui.BookingWidget)
        # add to cart button in booking
        self.ui.mixAdd.clicked.connect(
            lambda: self.checkRepeatedOrder("MIXED DORM"))
        self.ui.deluxeAdd.clicked.connect(
            lambda: self.checkRepeatedOrder("DELUXE ROOM"))
        self.ui.superiorAdd.clicked.connect(
            lambda: self.checkRepeatedOrder("SUPERIOR ROOM"))

        self.ui.mixAdd.clicked.connect(lambda: self.toggleCart(411, True))
        self.ui.deluxeAdd.clicked.connect(lambda: self.toggleCart(411, True))
        self.ui.superiorAdd.clicked.connect(lambda: self.toggleCart(411, True))
        # go to home page
        self.ui.HomeButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Home))
        # go to About page
        self.ui.AboutButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.About))
        # go to Contact us page
        self.ui.ContactButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.ContactUs))
        # go to booking page
        self.ui.BookingButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Booking))
        # go to info page
        self.ui.Info.clicked.connect(lambda: self.infoClicked())
        # save editted info
        self.ui.SaveButton.clicked.connect(
            lambda: self.handle_save_editted_info())
        # go to Mybooking page
        self.ui.MyBooking.clicked.connect(lambda: self.MyBookingClicked())
        self.ui.MyBooking.clicked.connect(lambda:self.addMyBookingItem())
        # go to cancel page
        # self.ui.Cancellation.clicked.connect(
        #     lambda: self.CancellationClicked())
        # close cart widget
        self.ui.cartCloseButton.clicked.connect(lambda: self.closeCart())
        # Cart widget
        self.ui.cartButton.clicked.connect(lambda: self.toggleCart(411, True))
        # My Account extends menu
        self.ui.AccountButton.clicked.connect(
            lambda: self.toggleMenu(221, True))
        # go to infoEdit page
        self.ui.EditButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.editinfoClicked()))
        # go back to info page
        self.ui.BackButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.InfoPage))
        # log out
        self.ui.LogOut.clicked.connect(lambda: self.log_out())
        # Payment confirmation cliked
        self.ui.PaymentButton.clicked.connect(lambda: self.checkRadio()) 
        # self.ui.radioButton_2.clicked.connect(lambda: self.checkRadio())
        # self.ui.radioButton.clicked.connect(lambda: self.checkRadio())
        # self.ui.PaymentButton.clicked.connect(
        #     lambda: self.handle_payment_btn())

        # set minimum and maximum date
        self.ui.dateEdit.setMinimumDate(QDate.currentDate())
        self.ui.dateEdit_3.setMinimumDate(QDate.currentDate().addDays(1))
        self.ui.dateEdit.dateChanged.connect(lambda: self.nextMinDate())

        # go to payment page
        self.ui.ProceedButton.clicked.connect(lambda: self.ableProceed())
        self.ui.ProceedButton.clicked.connect(lambda: self.overall())

        # reset cart
        self.ui.resetCartButton.clicked.connect(lambda: self.reset_cart())
        # reset when order done
        # self.ui.PaymentButton.clicked.connect(lambda: self.reset_cart())

        # back to cart
        self.ui.ReturnCartButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Booking))

        # reset order in payment
        self.ui.ReturnCartButton.clicked.connect(lambda: self.reset_order())
        self.ui.BookingButton.clicked.connect(lambda: self.reset_order())

        # book now button
        self.ui.mixBook.clicked.connect(lambda: self.reset_cart())
        self.ui.mixBook.clicked.connect(
            lambda: self.checkRepeatedOrder("MIXED DORM"))
        self.ui.mixBook.clicked.connect(lambda: self.overall())
        self.ui.mixBook.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Payment))
        self.ui.deluxeBook.clicked.connect(lambda: self.reset_cart())
        self.ui.deluxeBook.clicked.connect(
            lambda: self.checkRepeatedOrder("DELUXE ROOM"))
        self.ui.deluxeBook.clicked.connect(lambda: self.overall())
        self.ui.deluxeBook.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Payment))
        self.ui.superiorBook.clicked.connect(lambda: self.reset_cart())
        self.ui.superiorBook.clicked.connect(
            lambda: self.checkRepeatedOrder("SUPERIOR ROOM"))
        self.ui.superiorBook.clicked.connect(lambda: self.overall())
        self.ui.superiorBook.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Payment))

    # check payment method
        # self.ui.PaymentButton.clicked.connect(lambda: self.checkRadio())
    # back to home
        self.ui.BackHomeButton.clicked.connect(
            lambda: self.ui.Pages.setCurrentWidget(self.ui.Home))  

        
    #color change  
        self.ui.AboutButton.clicked.connect(lambda: self.changeColor()) 
        self.ui.HomeButton.clicked.connect(lambda: self.defaultColor())
        self.ui.ContactButton.clicked.connect(lambda: self.defaultColor())
        self.ui.BookingButton.clicked.connect(lambda: self.defaultColor())
        self.ui.AccountButton.clicked.connect(lambda: self.defaultColor()) 

    #comboBox cancel 
        self.ui.comboBox.currentIndexChanged.connect(lambda:self.ui.confirmCancelButton.setVisible(True)) 
        self.ui.confirmCancelButton.clicked.connect(lambda:self.cancel())


    def infoClicked(self):
        # Fetch user info from the database using the Account object
        user_info_list = self.get_user_info()

        if user_info_list:
            user_info = user_info_list[0]  # Assuming only one matching user

            # Extract the individual data fields
            user_id = user_info.get('user_id')
            user_Fname = user_info['user_Fname']
            user_Sname = user_info['user_Sname']
            user_tel = user_info['user_tel']
            user_email = user_info['user_email']
            user_birth = user_info['user_birth']

            # Display the fetched user info in the UI
            self.ui.AccountIDLabel.setText(str(user_id) if user_id else '')
            self.ui.NameLabel.setText(user_Fname)
            self.ui.SurnameLabel.setText(user_Sname)
            self.ui.PhoneLabel.setText(user_tel)
            self.ui.BirthDateEdit.setText(user_birth)
            self.ui.EmailLabel.setText(user_email)
        else:
            # Handle the case when user info is not found in the database
            print("User info not found")

        self.toggleMenu(221, True)
        self.ui.Pages.setCurrentWidget(self.ui.InfoPage)

    def editinfoClicked(self):
        user_info_list = self.get_user_info()

        if user_info_list:
            user_info = user_info_list[0]  # Assuming only one matching user

            # Extract the individual data fields
            user_password = user_info['user_password']
            user_Fname = user_info['user_Fname']
            user_Sname = user_info['user_Sname']
            user_tel = user_info['user_tel']
            user_email = user_info['user_email']
            user_birth = user_info['user_birth']

            # Display the fetched user info in the UI
            self.ui.NameEdit.setText(user_Fname)
            self.ui.SurnameEdit.setText(user_Sname)
            self.ui.PasswordEdit.setText(user_password)
            self.ui.ComfirmPassEdit.setText(user_password)
            self.ui.PhoneNumEdit.setText(user_tel)
            self.ui.EmailEdit.setText(user_email)
            self.ui.dateEdit_2.setDate(QDate.currentDate())
        else:
            # Handle the case when user info is not found in the database
            print("User info not found")

        self.ui.Pages.setCurrentWidget(self.ui.InfoEdit)

    # save the edited information
    def handle_save_editted_info(self):
        user_info_list = self.get_user_info()

        if user_info_list:
            # Get the first (and only) user info dictionary
            user_info = user_info_list[0]
            name_edit = self.ui.NameEdit.text()
            surname_edit = self.ui.SurnameEdit.text()
            password_edit = self.ui.PasswordEdit.text()
            phone_edit = self.ui.PhoneNumEdit.text()
            email_edit = self.ui.EmailEdit.text()
            date_edit = self.ui.dateEdit_2.text()

            try:
                # Check if username, phone number, email already exist
                if self.logged_in_user == user_info['user_name'] and phone_edit == user_info['user_tel'] and email_edit == user_info['user_email']:
                    self.password_valid(password_edit)
                else:
                    self.verify_details_for_edit_info(
                        email_edit, phone_edit, password_edit)

                # If all checks pass (by verify details)
                self.edit_info(name_edit, surname_edit, phone_edit,
                               email_edit, date_edit, password_edit)

                # Display success message
                QMessageBox.information(self, "Success", "Information saved.")

                # Show the updated info in the QLineEdit fields
                self.ui.NameEdit.setText(user_info['user_Fname'])
                self.ui.SurnameEdit.setText(user_info['user_Sname'])
                self.ui.PasswordEdit.setText(user_info['user_password'])
                self.ui.ComfirmPassEdit.setText(user_info['user_password'])
                self.ui.PhoneNumEdit.setText(user_info['user_tel'])
                self.ui.EmailEdit.setText(user_info['user_email'])
                self.ui.dateEdit_2.setDate(QDate.currentDate())

                # # Debug: Verify the modified dictionary
                # print("Modified user_edit_info:", user_edit_info)
                # # Save the modified user data back to the dictionary
                # self.root['user_acc_info'] = user_edit_info

                # Debug: Verify the updated dictionary
                # print("Updated user_acc_info:", self.root['user_acc_info'])
                self.connection.transaction_manager.commit()

            except Exception as e:
                # Display error message
                QMessageBox.warning(self, "Error", str(e))
        else:
            # Handle the case when user info is not found
            QMessageBox.warning(self, "Error", "User info not found.")

    def nextMinDate(self):
        selected_date = self.ui.dateEdit.date()
        next_day = selected_date.addDays(1)
        self.ui.dateEdit_3.setMinimumDate(next_day)

    def MyBookingClicked(self):
        self.toggleMenu(221, True)
        self.ui.Pages.setCurrentWidget(self.ui.MyBookingPage)

    # def CancellationClicked(self):
    #     self.toggleMenu(221, True)
    #     self.ui.Pages.setCurrentWidget(self.ui.CancellationPage)

    def toggleMenu(self, maxHeight, enable):
        if enable:
            # Get current height
            currentHeight = self.ui.LeftMenu.height()

            # Define the start and end values for the animation
            startValue = currentHeight
            endValue = maxHeight if currentHeight == 0 else 0

            # Create the animation
            animation = QVariantAnimation(self)
            animation.setStartValue(startValue)
            animation.setEndValue(endValue)
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutQuart)

            # Define the function to be called on each animation frame
            def onValueChanged(value):
                self.ui.LeftMenu.setFixedHeight(value)

            # Connect the animation to the function
            animation.valueChanged.connect(onValueChanged)

            # Start the animation
            animation.start()

    def toggleCart(self, maxWidth, enable):
        self.ui.cartWidget.setVisible(True)
        if enable:
            # Get current height
            currentWidth = self.ui.cartWidget.width()

            # Define the start and end values for the animation
            startValue = currentWidth
            endValue = maxWidth

            # Create the animation
            animation = QVariantAnimation(self)
            animation.setStartValue(startValue)
            animation.setEndValue(endValue)
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutQuart)

            # Define the function to be called on each animation frame
            def onValueChanged(value):
                self.ui.cartWidget.setFixedWidth(value)

            # Connect the animation to the function
            animation.valueChanged.connect(onValueChanged)

            # Start the animation
            animation.start()

    def closeCart(self):
        self.ui.cartWidget.setVisible(False)
        self.ui.cartWidget.setFixedWidth(0)

    def addItem(self, roomname):

        self.itemIdex += 1
        self.diff_date = self.date_range()
        itemFrame = QFrame(self.ui.itemCart)
        itemFrame.setObjectName(u"itemFrame" + str(self.itemIdex))
        itemFrame.setGeometry(
            QRect(40, 110 + (self.itemIdex - 1) * 40, 301, 41))
        itemFrame.setStyleSheet(u"QWidget { \n"
                                "border: 0 px solid ;\n"
                                "\n"
                                "}")
        itemFrame.setFrameShape(QFrame.Shape.Box)
        itemFrame.setFrameShadow(QFrame.Shadow.Raised)

        itemLabel = QLabel(itemFrame)
        itemLabel.setText(QCoreApplication.translate(
            "MainWindow", roomname, None))
        itemLabel.setObjectName(u"itemLabel")
        itemLabel.setGeometry(QRect(10, 10, 101, 21))
        itemLabel.setStyleSheet(u"QWidget{ \n"
                                "	border-radius:10px;\n"
                                "	font: 8pt \"Maragsa\"; \n"
                                "	color:rgb(0,0,0);\n"
                                "	border: 1px solid black \n"
                                "	\n"
                                "} \n"
                                "")
        itemComboBox = QComboBox(itemFrame)
        itemComboBox.setObjectName(u"itemComboBox")
        itemComboBox.setGeometry(QRect(130, 10, 71, 21))
        itemComboBox.setStyleSheet(u"QcomboBox{\n"
                                   "	border-color: 1px solid rgb(255, 255, 255);\n"
                                   "}")
        itemPriceLabel = QLabel(itemFrame)
        itemPriceLabel.setObjectName(u"itemPriceLabel")

        itemPriceLabel.setGeometry(QRect(220, 10, 61, 21))
        itemPriceLabel.setStyleSheet(u"QWidget{ \n"
                                     "	border-radius:10px;\n"
                                     "	font: 8pt \"Maragsa\"; \n"
                                     "	color:rgb(0,0,0);\n"
                                     "	border: 1px solid black \n"
                                     "	\n"
                                     "} \n"
                                     "")
        if roomname == "MIXED DORM":
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.setItemText(
                0, QCoreApplication.translate("MainWindow", u"0", None))
            itemComboBox.setItemText(
                1, QCoreApplication.translate("MainWindow", u"1", None))
            itemComboBox.setItemText(
                2, QCoreApplication.translate("MainWindow", u"2", None))
            itemComboBox.setItemText(
                3, QCoreApplication.translate("MainWindow", u"3", None))
            itemComboBox.setItemText(
                4, QCoreApplication.translate("MainWindow", u"4", None))
            itemComboBox.setItemText(
                5, QCoreApplication.translate("MainWindow", u"5", None))
            itemComboBox.setItemText(
                6, QCoreApplication.translate("MainWindow", u"6", None))
            itemComboBox.setItemText(
                7, QCoreApplication.translate("MainWindow", u"7", None))
            itemComboBox.setItemText(
                8, QCoreApplication.translate("MainWindow", u"8", None))
            itemComboBox.setItemText(
                9, QCoreApplication.translate("MainWindow", u"9", None))
            itemComboBox.setItemText(
                10, QCoreApplication.translate("MainWindow", u"10", None))
            itemComboBox.setCurrentIndex(1)

        elif roomname == "DELUXE ROOM":
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.setItemText(
                0, QCoreApplication.translate("MainWindow", u"0", None))
            itemComboBox.setItemText(
                1, QCoreApplication.translate("MainWindow", u"1", None))
            itemComboBox.setItemText(
                2, QCoreApplication.translate("MainWindow", u"2", None))
            itemComboBox.setItemText(
                3, QCoreApplication.translate("MainWindow", u"3", None))
            itemComboBox.setItemText(
                4, QCoreApplication.translate("MainWindow", u"4", None))
            itemComboBox.setItemText(
                5, QCoreApplication.translate("MainWindow", u"5", None))
            itemComboBox.setCurrentIndex(1)

        elif roomname == "SUPERIOR ROOM":
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.addItem("")
            itemComboBox.setItemText(
                0, QCoreApplication.translate("MainWindow", u"0", None))
            itemComboBox.setItemText(
                1, QCoreApplication.translate("MainWindow", u"1", None))
            itemComboBox.setItemText(
                2, QCoreApplication.translate("MainWindow", u"2", None))
            itemComboBox.setItemText(
                3, QCoreApplication.translate("MainWindow", u"3", None))
            itemComboBox.setCurrentIndex(1)

        if roomname == "MIXED DORM":
            itemPriceLabel.setText(str(self.diff_date*800))
        if roomname == "DELUXE ROOM":
            itemPriceLabel.setText(str(self.diff_date*3500))
        if roomname == "SUPERIOR ROOM":
            itemPriceLabel.setText(str(self.diff_date*5000))

        itemComboBox.currentIndexChanged.connect(
            lambda index, itemPriceLabel=itemPriceLabel, roomname=roomname: self.updateItemPrice(
                itemPriceLabel, roomname, index)
        )

        self.layout.addWidget(itemFrame)
        # print(self.layout.itemAt(0).itemPriceLabel.text())

    def updateItemPrice(self, itemPriceLabel, roomname, quantity):
        self.diff_date = self.date_range()
        if roomname == "MIXED DORM":
            price = 800
        elif roomname == "DELUXE ROOM":
            price = 3500
        elif roomname == "SUPERIOR ROOM":
            price = 5000

        total_price = price * quantity * self.diff_date
        itemPriceLabel.setText(str(total_price))

        # itemFrame = self.layout.itemAt(0).widget()
        # print(itemFrame.findChild(QLabel, "itemPriceLabel").text())

    def date_range(self):
        checkIn_date = self.ui.dateEdit.date().toString("MM-dd-yy")
        checkOut_date = self.ui.dateEdit_3.date().toString("MM-dd-yy")
        num_of_days = int(checkOut_date.split(
            "-")[1]) - int(checkIn_date.split("-")[1])

        counter = 0
        daterange = []

        while (counter <= num_of_days):
            day = int(checkIn_date.split("-")[1]) + counter
            date_to_add = checkIn_date.split("-")
            date_to_add[1] = str(day)
            date_to_add = "-".join(date_to_add)
            daterange.append(date_to_add)
            counter += 1

        return counter - 1

    def getOrder(self, i):
        checkIn_date = self.ui.dateEdit.date().toString("dd-MM-yy")
        checkOut_date = self.ui.dateEdit_3.date().toString("dd-MM-yy")
        itemFrame = self.layout.itemAt(i).widget()
        price = itemFrame.findChild(QLabel, "itemPriceLabel").text()
        qty = itemFrame.findChild(QComboBox, "itemComboBox").currentText()
        room = itemFrame.findChild(QLabel, "itemLabel").text()
        order = (room, checkIn_date, checkOut_date, qty, price)

        return order
    
    def checkRadio(self):
        if self.ui.radioButton_2.isChecked() == True :
            Home.payment_status = "incomplete"
            self.handle_payment_btn()
        elif self.ui.radioButton.isChecked() == True :
            print("Credit cad is not yet avaliable") 
            Home.payment_status = "complete"
            pass
        else :
            msg_box = QMessageBox(self.ui.cartWidget)
            msg_box.setWindowTitle("Information")
            msg_box.setText("Select Payment")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet(u"QLabel { \n"
                                    "border: 0 px; \n"
                                    "	font: 10pt \"Maragsa\";\n"
                                    "\n"
                                    "}")
            msg_box.exec() 
            pass

    def handle_payment_btn(self):
        from room import Room, MixedDorm, DeluxeRoom, SuperiorRoom
        from booking import BookingSystem
        booking_system = BookingSystem()
        payment_status = Home.payment_status
        #initialize all available rooms
        m = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10']
        d = ['D1', 'D2', 'D3', 'D4', 'D5']
        s = ['S1', 'S2', 'S3']
        will_reserve = [] 
        total_qty = 0 
        # Retrieve the order tuple
        for i in range(self.layout.count()):   
            reserved_room = []
            all_rooms = []
            available_rooms = []
            # reserved_room = []
            first_letter_room = ''
            count = 0
            
            order_info = self.getOrder(i)
            # Unpack the order tuple
            print("loop" ) 
            print(i)
            get_room_type, get_checkIn_date, get_checkOut_date, get_qty, price = order_info

            if get_room_type == 'MIXED DORM':
                all_rooms = m
                first_letter_room = 'M'
                # each = 800
            elif get_room_type == 'DELUXE ROOM':
                all_rooms = d
                first_letter_room = 'D'
                # each = 3500
            elif get_room_type == 'SUPERIOR ROOM':
                all_rooms = s
                first_letter_room = 'S'
                # each = 5000

            if (int(order_info[3]) == 0):
                pass
            else:
                user_acc_info = self.root['user_acc_info']
                user_ids = list(user_acc_info.keys())
                for user_id in user_ids:
                    # all_rooms = []
                    # print("loop_userids" ) 
                    # print(user_id)
                    # available_rooms = []
                    # # reserved_room = []
                    # first_letter_room = ''
                    # count = 0

                    # if get_room_type == 'MIXED DORM':
                    #     all_rooms = m
                    #     first_letter_room = 'M'
                    #     each = 800
                    # elif get_room_type == 'DELUXE ROOM':
                    #     all_rooms = d
                    #     first_letter_room = 'D'
                    #     each = 3500
                    # elif get_room_type == 'SUPERIOR ROOM':
                    #     all_rooms = s
                    #     first_letter_room = 'S'
                    #     each = 5000

                    # print(f"User ID: {user_id}\n-------------------------\nBookings:\n")
                    room_ids = list(self.root['user_acc_info'][user_id]['booking_dict_info'].keys())
                    for room_id in room_ids:
                        # print(room_id)
                        db_checkIn_date = (self.root['user_acc_info'][user_id]['booking_dict_info'][room_id]['checkIn'])
                        db_checkOut_date = (self.root['user_acc_info'][user_id]['booking_dict_info'][room_id]['checkOut'])
                        db_room_type = (self.root['user_acc_info'][user_id]['booking_dict_info'][room_id]['room_type'])

                        # print(f"CheckIn: {db_checkIn_date}\nCheckOut: {db_checkOut_date}\nRoom Type: {db_room_type}\nRoom ID: {room_id}\n")
                        if booking_system.is_date_not_between(get_checkIn_date, db_checkIn_date, db_checkOut_date) and booking_system.is_date_not_between(get_checkOut_date, db_checkIn_date, db_checkOut_date) and str(db_room_type[0]) == first_letter_room:
                            reserved_room.append(room_id)
                    print(f"Reserved Rooms: {reserved_room}")

                result = [rooms for rooms in all_rooms if rooms not in reserved_room]
                # print('results: ', result)
                available_rooms = result
                print(f"Results(Available Rooms): {result}")

                for k in range(len(available_rooms)):
                    if count < int(get_qty):
                        will_reserve.append(available_rooms[k])
                        count += 1
            total_qty += int(get_qty)
            print("first_tqty:")
            print(total_qty)
            all_rooms.clear()
            available_rooms.clear()
            reserved_room.clear()
            first_letter_room = ''
            count = 0
                    #     print(f"User ID: {user_id}\nRoom ID: {room_id}")
            print('----------------------------------------------------')
            #changes here
            print(f"Will Reserve: {will_reserve}")
            print(total_qty)
            print(len(will_reserve))

        if total_qty == len(will_reserve):
            count1 = 0
            for i in range(self.layout.count()):
                order_info = self.getOrder(i)
                # Unpack the order tuple
                get_room_type, get_checkIn_date, get_checkOut_date, get_qty, price = order_info
                print("ggggggggggg")
                print(get_room_type)
                if get_room_type == 'MIXED DORM':
                    each1 = 800
                elif get_room_type == 'DELUXE ROOM':
                    each1 = 3500
                elif get_room_type == 'SUPERIOR ROOM':
                    each1 = 5000
                for j in range(int(get_qty)):
                    print("count")
                    print(count)
                    booking_system.book_rooms_to_dictionary(room_id=will_reserve[count1], room_type=get_room_type, booked_quantity=1,
                                                            checkIn_date=get_checkIn_date, checkOut_date=get_checkOut_date, price=each1, payment_status=payment_status)  # payment status
                    count1 += 1
            self.ui.Pages.setCurrentWidget(self.ui.bookingSuccess) 
            self.reset_cart()
        else:
            print("No available rooms")
            msg_box = QMessageBox(self.ui.PaymentMethod)
            msg_box.setWindowTitle("Caution!")
            msg_box.setText("No room avaliable on that date")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet(u"QLabel { \n"
                                    "border: 0 px; \n"
                                    "	font: 10pt \"Maragsa\";\n"
                                    "\n"
                                    "}")
            msg_box.exec() 
        will_reserve.clear()
            # BookingSystem.booking_list_all_data(self)

            # for reserve in will_reserve:
            #     booking_system.book_rooms_to_dictionary(room_id=reserve, room_type=get_room_type, booked_quantity=1,
            #                                             checkIn_date=get_checkIn_date, checkOut_date=get_checkOut_date, price=each)

    def log_out(self):
        # Create a QMessageBox instance
        msg_box = QMessageBox()
        # Set the dialog title
        msg_box.setWindowTitle("Logout Confirmation")
        # Set the dialog text
        msg_box.setText("Are you sure you want to logout?")
        # Set the dialog buttons
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        # Set the icon of the dialog
        msg_box.setIcon(QMessageBox.Question)
        # Execute the dialog and get the result
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            from loginProgram import Login
            self.close()
            self.logIn_window = Login()
            self.logIn_window.show()
            # Perform logout action
            print("Logging out...")
        else:
            # Cancel logout action
            print("Logout cancelled.")

    def overall(self):
        total_price = 0
        for i in range(self.layout.count()):
            order_info = self.getOrder(i)

            if (int(order_info[3]) == 0):
                pass
            else:
                self.orderFrame = QFrame(self.ui.order_payment)
                self.orderFrame.setObjectName(u"orderFrame")
                self.orderFrame.setStyleSheet(u"QFrame{\n"
                                              "background-color: rgb(255, 255, 255);\n"
                                              "border-radius: 0px\n"
                                              "}")
                self.orderFrame.setFrameShape(QFrame.StyledPanel)
                self.orderFrame.setFrameShadow(QFrame.Raised)
                self.roomPic = QLabel(self.orderFrame)
                self.roomPic.setObjectName(u"roomPic")
                self.roomPic.setGeometry(QRect(10, 10, 101, 61))
                self.roomPic.setPixmap(
                    QPixmap(u"BusabaImages/" + str(order_info[0] + ".jpg")))
                self.roomType = QLabel(self.orderFrame)
                self.roomType.setObjectName(u"roomType")
                self.roomType.setObjectName(u"" + str(order_info))
                self.roomType.setGeometry(QRect(10, 80, 101, 16))
                self.roomType.setStyleSheet(u"QLabel { \n"
                                            "	font: 10pt \"Maragsa\";\n"
                                            "\n"
                                            "}")
                self.Date = QLabel(self.orderFrame)
                self.Date.setObjectName(u"Date")
                self.Date.setGeometry(QRect(130, 40, 31, 16))
                self.Date.setStyleSheet(u"QLabel { \n"
                                        "	font: 10pt \"Maragsa\";\n"
                                        "\n"
                                        "}")
                self.dateCI = QLabel(self.orderFrame)
                self.dateCI.setObjectName(u"dateCI")
                self.dateCI.setGeometry(QRect(170, 40, 61, 16))
                self.dateCI.setStyleSheet(u"QLabel { \n"
                                          "	font: 10pt \"Maragsa\";\n"
                                          "\n"
                                          "}")
                self.toDate = QLabel(self.orderFrame)
                self.toDate.setObjectName(u"toDate")
                self.toDate.setGeometry(QRect(240, 40, 21, 16))
                self.toDate.setStyleSheet(u"QLabel { \n"
                                          "	font: 10pt \"Maragsa\";\n"
                                          "\n"
                                          "}")
                self.dateCO = QLabel(self.orderFrame)
                self.dateCO.setObjectName(u"dateCO")
                self.dateCO.setGeometry(QRect(270, 40, 61, 16))
                self.dateCO.setStyleSheet(u"QLabel { \n"
                                          "	font: 10pt \"Maragsa\";\n"
                                          "\n"
                                          "}")
                self.Amount = QLabel(self.orderFrame)
                self.Amount.setObjectName(u"Amount")
                self.Amount.setGeometry(QRect(360, 40, 51, 16))
                self.Amount.setStyleSheet(u"QLabel { \n"
                                          "	font: 10pt \"Maragsa\";\n"
                                          "\n"
                                          "}")
                self.qtyLabel = QLabel(self.orderFrame)
                self.qtyLabel.setObjectName(u"qtyLabel")
                self.qtyLabel.setGeometry(QRect(420, 40, 21, 16))
                self.qtyLabel.setStyleSheet(u"QLabel { \n"
                                            "	font: 10pt \"Maragsa\";\n"
                                            "\n"
                                            "}")
                self.roomPrice = QLabel(self.orderFrame)
                self.roomPrice.setObjectName(u"roomPrice")
                self.roomPrice.setGeometry(QRect(450, 40, 51, 16))
                self.roomPrice.setStyleSheet(u"QLabel { \n"
                                             "	font: 10pt \"Maragsa\";\n"
                                             "\n"
                                             "}")
                self.currencyLabel = QLabel(self.orderFrame)
                self.currencyLabel.setObjectName(u"currencyLabel")
                self.currencyLabel.setGeometry(QRect(550, 40, 21, 16))
                self.currencyLabel.setStyleSheet(u"QLabel { \n"
                                                 "border: 0 px; \n"
                                                 "	font: 10pt \"Maragsa\";\n"
                                                 "\n"
                                                 "}")
                self.priceConLabel = QLabel(self.orderFrame)
                self.priceConLabel.setObjectName(u"priceConLabel")
                self.priceConLabel.setGeometry(QRect(490, 40, 51, 16))
                self.priceConLabel.setStyleSheet(u"QLabel { \n"
                                                 "	font: 10pt \"Maragsa\";\n"
                                                 "\n"
                                                 "}")

                self.roomPic.setText("")
                self.roomType.setText(QCoreApplication.translate(
                    "MainWindow", u""+order_info[0], None))
                self.Date.setText(QCoreApplication.translate(
                    "MainWindow", u"Date", None))
                self.dateCI.setText(QCoreApplication.translate(
                    "MainWindow", u""+order_info[1], None))
                self.toDate.setText(QCoreApplication.translate(
                    "MainWindow", u"to", None))
                self.dateCO.setText(QCoreApplication.translate(
                    "MainWindow", u""+order_info[2], None))
                self.Amount.setText(QCoreApplication.translate(
                    "MainWindow", u"Amount", None))
                self.qtyLabel.setText(QCoreApplication.translate(
                    "MainWindow", u""+order_info[3], None))
                self.roomPrice.setText(QCoreApplication.translate(
                    "MainWindow", u"Price", None))
                self.currencyLabel.setText(
                    QCoreApplication.translate("MainWindow", u"\u0e3f", None))
                self.priceConLabel.setText(QCoreApplication.translate(
                    "MainWindow", u""+order_info[4], None))
                self.verticalLayout_2.addWidget(self.orderFrame)

                total_price += int(order_info[4])
        self.ui.priceLabel.setText(QCoreApplication.translate(
            "MainWindow", u"" + str(total_price), None))
        
    def checkRepeatedOrder(self, room):
        repeated = False
        for i in range(self.layout.count()):
            order = self.getOrder(i)
            if order[0] == room:
                repeated = True
                break
            else:
                pass
        if repeated == True:
            pass
        elif repeated == False:
            self.addItem(room)

    def addMyBookingItem(self): 
        book = BookingSystem() 
        booking_info = book.get_booking_info()
        self.reset_MyBooking()
        print(len(booking_info))
        for i in range (len(booking_info)) : 
            room_id   = booking_info[i]['room_id']
            room_type   = booking_info[i]['room_type']
            letter = list(booking_info[i]['room_id']) 
            first_letter = letter[0] 
            checkIn = booking_info[i]['checkIn_date']
            checkOut = booking_info[i]['checkOut_date'] 
            qty = booking_info[i]['booked_quantity']  
            price = booking_info[i]['price'] 
            status = booking_info[i]['payment_status']

            #able to cancel list
            self.ui.comboBox.setStyleSheet("""
    QComboBox {
        border: 1px solid rgb(0, 48, 145);
        color: rgb(0, 0, 0);
    }
    QComboBox::item {
        color: black;
    }

    QListView{
    color: rgb(0,0,0);
}
""")
            self.ui.comboBox.addItem("")
            self.ui.comboBox.setItemText(i, QCoreApplication.translate("Mainwindow", u""+room_id+":  "+checkIn,None))
            #show booking lists
            self.BookingItem = QFrame(self.ui.BookingWidget)
            self.BookingItem.setObjectName(u"BookingItem")
            self.BookingItem.setGeometry(QRect(-10, -10, 881, 181))
            self.BookingItem.setStyleSheet(u"QFrame{ \n"
    "border-bottom-color:1px solid black ;\n"
    "border: 1px solid black ;\n"
    "\n"
    "}")
            self.BookingItem.setFrameShape(QFrame.StyledPanel)
            self.BookingItem.setFrameShadow(QFrame.Raised)
            self.IdBooking = QLabel(self.BookingItem)
            self.IdBooking.setObjectName(u"IdBooking")
            self.IdBooking.setGeometry(QRect(160, 10, 51, 21))
            self.IdBooking.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.CheckInBooking = QLabel(self.BookingItem)
            self.CheckInBooking.setObjectName(u"CheckInBooking")
            self.CheckInBooking.setGeometry(QRect(160, 40, 51, 21))
            self.CheckInBooking.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.CheckOutBooking = QLabel(self.BookingItem)
            self.CheckOutBooking.setObjectName(u"CheckOutBooking")
            self.CheckOutBooking.setGeometry(QRect(380, 40, 61, 21))
            self.CheckOutBooking.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.qtyBooking = QLabel(self.BookingItem)
            self.qtyBooking.setObjectName(u"qtyBooking")
            self.qtyBooking.setGeometry(QRect(160, 70, 51, 21))
            self.qtyBooking.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.StatusBooking = QLabel(self.BookingItem)
            self.StatusBooking.setObjectName(u"StatusBooking")
            self.StatusBooking.setGeometry(QRect(160, 140, 81, 16))
            self.StatusBooking.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.PriceBooking = QLabel(self.BookingItem)
            self.PriceBooking.setObjectName(u"PriceBooking")
            self.PriceBooking.setGeometry(QRect(160, 100, 41, 21))
            self.PriceBooking.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.CurrencyTHB = QLabel(self.BookingItem)
            self.CurrencyTHB.setObjectName(u"CurrencyTHB")
            self.CurrencyTHB.setGeometry(QRect(310, 100, 31, 21))
            self.CurrencyTHB.setStyleSheet(u"QLabel {\n"
    "color: rgb(0, 48, 121);\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.RoomTypeBooking = QLabel(self.BookingItem)
            self.RoomTypeBooking.setObjectName(u"RoomTypeBooking")
            self.RoomTypeBooking.setGeometry(QRect(20, 120, 111, 21))
            self.RoomTypeBooking.setStyleSheet(u"QLabel { \n"
    "border: 0 px; \n"
    "font: 11pt \"Maragsa\"; \n"
    "color: rgb(0, 48, 145);\n"
    "}")
            self.idDB = QLabel(self.BookingItem)
            self.idDB.setObjectName(u"idDB")
            self.idDB.setGeometry(QRect(220, 10, 31, 21))
            self.idDB.setStyleSheet(u"QLabel {\n"
    "	color: rgb(223, 109, 114);\n"
    "\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.CheckInDB = QLabel(self.BookingItem)
            self.CheckInDB.setObjectName(u"CheckInDB")
            self.CheckInDB.setGeometry(QRect(220, 40, 71, 21))
            self.CheckInDB.setStyleSheet(u"QLabel {\n"
    "	color: rgb(223, 109, 114);\n"
    "\n"
    "	font: 11pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.CheckOutDB = QLabel(self.BookingItem)
            self.CheckOutDB.setObjectName(u"CheckOutDB")
            self.CheckOutDB.setGeometry(QRect(450, 40, 61, 21))
            self.CheckOutDB.setStyleSheet(u"QLabel {\n"
    "	color: rgb(223, 109, 114);\n"
    "\n"
    "	font: 11pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.qtyDB = QLabel(self.BookingItem)
            self.qtyDB.setObjectName(u"qtyDB")
            self.qtyDB.setGeometry(QRect(220, 70, 21, 21))
            self.qtyDB.setStyleSheet(u"QLabel {\n"
    "	color: rgb(223, 109, 114);\n"
    "\n"
    "	font: 11pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.PriceDB = QLabel(self.BookingItem)
            self.PriceDB.setObjectName(u"PriceDB")
            self.PriceDB.setGeometry(QRect(220, 100, 61, 21))
            self.PriceDB.setStyleSheet(u"QLabel {\n"
    "	color: rgb(223, 109, 114);\n"
    "\n"
    "	font: 11pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.StatusDB = QLabel(self.BookingItem)
            self.StatusDB.setObjectName(u"StatusDB")
            self.StatusDB.setGeometry(QRect(220, 140, 61, 16))
            self.StatusDB.setStyleSheet(u"QLabel {\n"
    "	color: rgb(124, 124, 124);\n"
    "\n"
    "	font: 10pt \"Maragsa\"; \n"
    "border: 0px ;\n"
    "}")
            self.PicBooking = QLabel(self.BookingItem)
            self.PicBooking.setObjectName(u"PicBooking")
            self.PicBooking.setGeometry(QRect(20, 10, 101, 101))
            self.PicBooking.setMinimumSize(QSize(101, 101))
            self.PicBooking.setMaximumSize(QSize(101, 101))
            self.PicBooking.setPixmap(QPixmap(u"BusabaImages/"+first_letter+".jpg"))

            # self.verticalLayout_4.addWidget(self.BookingWidget)
            # self.verticalLayout_4.addWidget(self.orderFrame) 
            
            self.IdBooking.setText(QCoreApplication.translate("MainWindow", u"ROOM ID  :", None))
            self.CheckInBooking.setText(QCoreApplication.translate("MainWindow", u"Check-In  :", None))
            self.CheckOutBooking.setText(QCoreApplication.translate("MainWindow", u"Check-Out  :", None))
            self.qtyBooking.setText(QCoreApplication.translate("MainWindow", u"Amount  :", None))
            self.StatusBooking.setText(QCoreApplication.translate("MainWindow", u"Status  :", None))
            self.PriceBooking.setText(QCoreApplication.translate("MainWindow", u"Price  :", None))
            self.CurrencyTHB.setText(QCoreApplication.translate("MainWindow", u"THB", None))
            self.RoomTypeBooking.setText(QCoreApplication.translate("MainWindow", u""+room_type, None))
            self.idDB.setText(QCoreApplication.translate("MainWindow", u""+room_id, None))
            self.CheckInDB.setText(QCoreApplication.translate("MainWindow", u""+checkIn, None))
            self.CheckOutDB.setText(QCoreApplication.translate("MainWindow", u""+checkOut, None))
            self.qtyDB.setText(QCoreApplication.translate("MainWindow", u""+ str(qty), None))
            self.PriceDB.setText(QCoreApplication.translate("MainWindow", u""+str(price), None))
            self.StatusDB.setText(QCoreApplication.translate("MainWindow", u""+status, None))
            self.PicBooking.setText("")

            self.layout2.addWidget(self.BookingItem)

    def reset_cart(self):
        while self.layout.count() > 0:
            item = self.layout.itemAt(0)
            widget = item.widget()
            self.layout.removeWidget(widget)
            widget.setParent(None)

    def reset_order(self):
        while self.verticalLayout_2.count() > 0:
            item = self.verticalLayout_2.itemAt(0)
            widget = item.widget()
            self.verticalLayout_2.removeWidget(widget)
            widget.setParent(None)

    def ableProceed(self):
        if self.layout.count() == 0:
            msg_box = QMessageBox(self.ui.cartWidget)
            msg_box.setWindowTitle("Information")
            msg_box.setText("No items in the cart")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStyleSheet(u"QLabel { \n"
                                  "border: 0 px; \n"
                                  "	font: 10pt \"Maragsa\";\n"
                                  "\n"
                                  "}")
            msg_box.exec()
        else:
            self.ui.Pages.setCurrentWidget(self.ui.Payment)

    def changeColor(self) : 
        self.ui.HomeButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(255,255,255);\n"
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
        self.ui.AboutButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(255,255,255);\n"
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
        self.ui.ContactButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(255,255,255);\n"
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
        self.ui.BookingButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(255,255,255);\n"
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
        self.ui.AccountButton.setStyleSheet(u"QPushButton{ \n"
"	font: 14pt \"Maragsa\"; \n"
"	color:rgb(255,255,255);\n"
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
        # self.ui.Logo.setPixmap(QPixmap(u"BusabaImages/Busaba-WhiteLogo.png"))

    def defaultColor(self) : 
        self.ui.HomeButton.setStyleSheet(u"QPushButton{ \n"
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
        self.ui.AboutButton.setStyleSheet(u"QPushButton{ \n"
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
        self.ui.ContactButton.setStyleSheet(u"QPushButton{ \n"
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
        self.ui.BookingButton.setStyleSheet(u"QPushButton{ \n"
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
        self.ui.AccountButton.setStyleSheet(u"QPushButton{ \n"
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
        # self.ui.Logo.setPixmap(QPixmap(u"BusabaImages/Busaba03.png"))
    def reset_MyBooking(self):
        while self.layout2.count() > 0:
            item = self.layout2.itemAt(0)
            widget = item.widget()
            self.layout2.removeWidget(widget)
            widget.setParent(None) 
        self.ui.comboBox.clear()

    def cancel(self): 
        selected_text = self.ui.comboBox.currentText()  
        elements = re.findall(r'(\S+)(?::|$)', selected_text)
        print(elements)
        self.b.delete_selected_rooms(elements)
        self.addMyBookingItem()



        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Home()
    w.show()

    sys.exit(app.exec())
