from multiprocessing import connection
from persistent.mapping import PersistentMapping
import ZODB
import ZODB.FileStorage
from typing import *
import transaction
# from ZEO import zeoctl



class Connection:
    storage = ZODB.FileStorage.FileStorage("SEPdatabase/user_acc_info.fs")
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

    if 'user_acc_info' not in root:
        root['user_acc_info'] = PersistentMapping()

    def __init__(self):
        # Assign the class attribute to instance attribute
        self.connection = Connection.connection
        self.root = Connection.root  # Assign the class attribute to instance attribute
        # self.logged_in_user = None

    def __close_connection__(self):
        try:
            self.connection.close()
        except Exception as e:
            print(f"Error closing ZODB connection: {e}")

    def commit_changes(self):
        try:
            transaction.commit()
        except Exception as e:
            print(f"Error committing changes to ZODB: {e}")

    def __transactionCommit__(self):
        try:
            transaction.commit()
        except Exception as e:
            print(f"Error committing changes to ZODB: {e}")


    # def register(self, user_name, user_Fname, user_Sname, user_tel, user_email, user_password, user_birth):
    #     id = self.generate_unique_id()
    #     user_acc_info = {
    #         'user_name': user_name,
    #         'user_Fname': user_Fname,
    #         'user_Sname': user_Sname,
    #         'user_tel': user_tel,
    #         'user_email': user_email,
    #         'user_password': user_password,
    #         'user_birth': user_birth
    #     }
    #     self.root['user_acc_info'][id] = user_acc_info
    #     self.connection.transaction_manager.commit()
