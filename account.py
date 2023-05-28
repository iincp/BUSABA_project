from multiprocessing import connection
from persistent.mapping import PersistentMapping
import ZODB
import ZODB.FileStorage
import random
import string
from typing import *
import transaction
from connection import Connection


class Account(Connection):
    logged_in_user = None
    # logged_in_id = None
    def __init__(self):
        pass

    def register(self, user_name, user_Fname, user_Sname, user_tel, user_email, user_password, user_birth):
        id = self.generate_unique_id()
        user_acc_info = {
            'user_name': user_name,  # Change key to 'username' instead of 'user_name'
            'user_Fname': user_Fname,
            'user_Sname': user_Sname,
            'user_tel': user_tel,
            'user_email': user_email,
            'user_password': user_password,
            'user_birth': user_birth,
            'user_id': id,
            'booking_dict_info': {}
        }
        if 'user_acc_info' not in self.root:
            self.root['user_acc_info'] = {}
        self.root['user_acc_info'][id] = user_acc_info
        transaction.commit()

    def logIn_valid(self, name, password):
        if 'user_acc_info' in self.root:
            user_acc_info = self.root['user_acc_info']
            for user in user_acc_info.values():
                if user['user_name'] == name:
                    stored_password = user.get('user_password')
                    if stored_password == password:
                        Account.logged_in_user = name
                        print(
                            "User '{}' is already registered and the password is correct.".format(name))
                        print(Account.logged_in_user)
                        return True

                    else:
                        print(
                            "User '{}' is already registered but the password is incorrect.".format(name))
                        return False
                    # return  # Exit the function after processing a registered user
        else:
            print("User '{}' is not registered.".format(name))
            return False

    def get_user_info(self):
        logged_in_user = Account.logged_in_user
        user_info_list = []

        if 'user_acc_info' in self.root:
            user_acc_info = self.root['user_acc_info']

            for user_id, user_data in user_acc_info.items():
                if user_data.get('user_name') == logged_in_user:
                    user_info_list.append(user_data)

        return user_info_list

    def generate_unique_id(self):
        # Generate a random 6-character string
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Check if the ID is already in the database
        while self.root['user_acc_info'].get(id):
            id = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=6))

        return id

    def edit_info(self, name_edit, surname_edit, phone_edit, mail_edit, date_edit, password_edit):
        logged_in_user = Account.logged_in_user
        try:
            user_info = self.root['user_acc_info']

            # Find the matching user info dictionary
            for user_id, user_data in user_info.items():
                if user_data.get('user_name') == logged_in_user:
                    # Update the fields
                    user_data['user_Fname'] = name_edit
                    user_data['user_Sname'] = surname_edit
                    user_data['user_tel'] = phone_edit
                    user_data['user_email'] = mail_edit
                    user_data['user_password'] = password_edit
                    user_data['user_birth'] = date_edit

            # Debug: Verify the modified dictionary
            print("Modified user_edit_info:", user_data)
            # Save the modified user data back to the dictionary
            self.root['user_acc_info'][user_id] = user_data

            # Debug: Verify the updated dictionary
            print("Updated user_acc_info:", self.root['user_acc_info'])
            self.connection.transaction_manager.commit()

        except KeyError as e:
            print(f"Error occurred: {e}")

    def unique_userName(self, user_name):
        for user_id, user_acc_info in self.root['user_acc_info'].items():
            if user_acc_info['user_name'] == user_name:
                return True
        return False

    def unique_email(self, user_email):
        for user_id, user_acc_info in self.root['user_acc_info'].items():
            if user_acc_info['user_email'] == user_email:
                return True
        return False

    def unique_phone(self, user_tel):
        for user_id, user_acc_info in self.root['user_acc_info'].items():
            if user_acc_info['user_tel'] == user_tel:
                return True
        return False

    def list_all_data_for_account(self):
        # for user_id, user_acc_info in self.root['user_acc_info'].items():
        #     print(f"User ID: {user_id}")  # Print the user ID or identifier
        #     for key, value in user_acc_info.items():
        #         print(f"{key}: {value}")
        #     print("----------------------")
        print(self.root.items())


    # def __del__(self):
    #     try:
    #         self.connection.close()
    #     except Exception as e:
    #         print(f"Error closing ZODB connection: {e}")

    # def __close__(self):
    #     self.connection.close()
    #     self.db.close()
    #     self.storage.close()

    # def __del__(self):
    #     self.root._p_jar.db().close()  # Close the ZODB connection