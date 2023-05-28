from account import Account
from connection import Connection
from booking import BookingSystem
from room import *

# Create an instance of the Account class 
account = Account()
conn = Connection()
book = BookingSystem()
 
# # Call the list_all_data method to retrieve and print all data
account.list_all_data_for_account()
print('\n')


book.booking_list_all_data()
list_booking_info = book.get_booking_info()
for i in range(len(list_booking_info)):
    print(list_booking_info[i])



# mixed_dormA = MixedDorm()
# booked_rooms = mixed_dormA.book_rooms(3)

# # mixed_dormB = MixedDorm()
# # booked_rooms = mixed_dormB.book_rooms(2)

# for room_id in booked_rooms:
#     print(room_id)
#     book.book_rooms_to_dictionary(room_id, 'Mixed', 1, 'check_in_date', 'check_out_date', '500')
    
# data = account.root['user_acc_info']



# account.logInvalid('fuku', 'Folk12345')
# print(conn.root['user_acc_info'].get('user_password'))

# Registering a user
# account.register('fukuu', 'asd', 'asd', 'asd', 'asd', 'Folk123456', '2000-01-01')

# Checking registration status
# account.logIn_valid('ssss', 'Ssss12345')
# account.get_user_info()
# for user_id, user_data in conn.root['user_acc_info'].items():
#     if user_data.get('user_name') == 'aaaa':
#         print(user_id, user_data)

# Close the ZODB connection
# account.close_connection()


#    def logIn_valid(self, user_name, password):
#        try:
#             # Check if the username exists in the database
#             if user_name in self.root:
#                 stored_password = self.root[user_name].get('ser_password')
#                 if stored_password == password:
#                     # Passwords match
#                     print('Credentials are valid.')
#                     # Set the logged-in user
#                     self.logged_in_user = user_name
#                     return True
#                 else:
#                     # Passwords do not match
#                     print('Invalid password.')
#             else:
#                 # Username does not exist in the database
#                 print('Invalid username.')
#         except Exception as e:
#             print(f"Error performing login: {e}")
#             return False
