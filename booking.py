from account import Account
from room import *
from datetime import * 
from  transaction import *

class BookingSystem(Account): #,(Account, Room)
    def __init__(self):
        # List to store booked rooms
        self.bookings = []  

    def is_date_not_between(self, ordered_date, db_checkIndate, db_checkOutdate):
        format_str = '%d-%m-%y'

        # Convert date strings to datetime objects
        date0_obj = datetime.strptime(ordered_date, format_str)
        date1_obj = datetime.strptime(db_checkIndate, format_str)
        date2_obj = datetime.strptime(db_checkOutdate, format_str)

        # Check if date0 is not between date1 and date2
        if date1_obj <= date0_obj <= date2_obj:
            return True
        else:
            return False

    def book_rooms_to_dictionary(self, room_id, room_type, booked_quantity, checkIn_date, checkOut_date, price, payment_status):
        logged_in_user = Account.logged_in_user
        print('booking', logged_in_user)
        try:
            user_info = self.root['user_acc_info']

            # Find the matching user info dictionary
            for user_id, user_data in user_info.items():
                if user_data.get('user_name') == logged_in_user:
                    # Create a new dictionary for booking data if it doesn't exist
                    if 'booking_dict_info' not in user_data:
                        user_data['booking_dict_info'] = {}

                    # Create a new dictionary entry for the user if room_id doesn't exist
                    if room_id not in user_data['booking_dict_info']:
                        user_data['booking_dict_info'][room_id] = {}

                    # Create a new booking entry
                    booking_entry = {
                        'user_id': user_id,
                        'room_id': room_id,
                        'room_type': room_type,
                        'booked_quantity': booked_quantity,
                        'checkIn': checkIn_date,
                        'checkOut': checkOut_date,
                        'price': price,
                        'payment_status': payment_status
                    }

                    # Add the booking entry to the user's dictionary
                    user_data['booking_dict_info'][room_id] = booking_entry

            # Save the modified user_data back to the root's user_acc_info
            self.root['user_acc_info'][user_id] = user_data
            self.connection.transaction_manager.commit()
            print("Room booked successfully!")

        except KeyError as e:
            print(f"Error occurred: {e}")

    # lists all data in booking_dict_info
    def booking_list_all_data(self):
        user_acc_info = self.root.get('user_acc_info', {})
        for user_id, user_data in user_acc_info.items():
            print(f"User ID: {user_id}")
            print(f"User Name: {user_data.get('user_name')}")
            print(f"User First Name: {user_data.get('user_Fname')}")
            print(f"User Last Name: {user_data.get('user_Sname')}")
            print(f"User Telephone: {user_data.get('user_tel')}")
            print(f"User Email: {user_data.get('user_email')}")
            print(f"User Password: {user_data.get('user_password')}")
            print(f"User Birth: {user_data.get('user_birth')}")
            print('\n')
            print("Booking Details:")
            
            booking_dict_info = user_data.get('booking_dict_info', {})
            for room_id, booking_entry in booking_dict_info.items():
                print(f"Room ID: {room_id}")
                print(f"Room Type: {booking_entry.get('room_type')}")
                print(f"Booked Quantity: {booking_entry.get('booked_quantity')}")
                print(f"Check-In Date: {booking_entry.get('checkIn')}")
                print(f"Check-Out Date: {booking_entry.get('checkOut')}")
                print(f"Price: {booking_entry.get('price')}")
                print("------------------")
            print("--------------------------------------")
        
    def get_current_userID(self):
        logged_in_user =  Account.logged_in_user  
        for user_id, user_data in self.root['user_acc_info'].items():
            if user_data['user_name'] == logged_in_user:
                user_id = user_data['user_id']
                break
        return (user_id)

    def get_booking_info(self):
        current_userID = self.get_current_userID()
        room_ids = list(self.root['user_acc_info'][current_userID]['booking_dict_info'].keys())
        booking_info_list = []

        for room_id in room_ids:
            room_data = self.root['user_acc_info'][current_userID]['booking_dict_info'][room_id]
            room_info = {
                'room_id': room_data['room_id'],
                'room_type': room_data['room_type'],
                'checkIn_date': room_data['checkIn'],
                'checkOut_date': room_data['checkOut'],
                'booked_quantity': room_data['booked_quantity'],
                'price': room_data['price'],
                'payment_status': room_data['payment_status']
            }
            booking_info_list.append(room_info)

        return booking_info_list
    
    def delete_selected_rooms(self, select_list):
        selected_list = select_list
        logged_in_user = Account.logged_in_user
        try:
            user_info = self.root['user_acc_info']

            # Find the matching user info dictionary
            for user_id, user_data in user_info.items():
                if user_data.get('user_name') == logged_in_user:
                    # Check if 'booking_dict_info' exists for the user
                    if 'booking_dict_info' in user_data:
                        # Iterate over the room IDs in the booking_dict_info
                        room_ids = list(user_data['booking_dict_info'].keys())
                        for room_id in room_ids:
                            # Check if the room ID and check-in date match the selected list
                            if room_id == selected_list[0] and user_data['booking_dict_info'][room_id]['checkIn'] == selected_list[1]:
                                del user_data['booking_dict_info'][room_id]
                                print(
                                    f"Room with ID {room_id} deleted successfully.")

            # Save the modified user_data back to the root's user_acc_info
            self.root['user_acc_info'][user_id] = user_data
            self.connection.transaction_manager.commit()

        except KeyError as e:
            print(f"Error occurred: {e}")
            
    
    # # retrieve data from booking_dict_info according to the current user logged in
    # def get_booking_data(self):
    #     current_userID = self.get_current_userID()
    #     user_info = self.root['user_acc_info'].get(current_userID)
    #     if user_info:
    #         booking_dict_info = user_info.get('booking_dict_info')
    #         if booking_dict_info:
    #             return list(booking_dict_info.values())
    #     return []

    # def check_availability(self, room, booked_quantity):
    #     return room.get_room_available() >= booked_quantity

    # def calculate_cost(self, room):
    #     return room.get_cost()

    # def get_bookings(self):
    #     return self.bookings
    
# rooms available(list or dict), check out: return the booked rooms back to the list, dict, get_booking_info(self):,  

# book = BookingSystem()
# book.booking_list_all_data()