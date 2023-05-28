from datetime import *
itemViews = {'user_acc_info': {'JJEHSE': {'user_name': 'asd', 'user_Fname': 'asd', 'user_Sname': 'asd', 'user_tel': 'asd', 'user_email': 'asd', 'user_password': 'Asd1234', 'user_birth': '2000-01-01', 'user_id': 'JJEHSE', 'booking_dict_info': {'S3': {'user_id': 'JJEHSE', 'room_id': 'S3', 'room_type': 'SUPERIOR ROOM', 'booked_quantity': 1, 'checkIn': '26-05-23', 'checkOut': '27-05-23', 'price': 5000}}}, 'BOJ5C7': {'user_name': 'qwe', 'user_Fname': 'qwe', 'user_Sname': 'qwe', 'user_tel': 'qwe', 'user_email': 'qwe', 'user_password': 'Qwe1234',
                                                                                                                                                                                                                                                                                                                                                                                                                                'user_birth': '2000-01-01', 'user_id': 'BOJ5C7', 'booking_dict_info': {'D4': {'user_id': 'BOJ5C7', 'room_id': 'D4', 'room_type': 'DELUXE ROOM', 'booked_quantity': 1, 'checkIn': '26-05-23', 'checkOut': '27-05-23', 'price': 3500}, 'D1': {'user_id': 'BOJ5C7', 'room_id': 'D1', 'room_type': 'DELUXE ROOM', 'booked_quantity': 1, 'checkIn': '26-05-23', 'checkOut': '27-05-23', 'price': 3500}, 'D5': {'user_id': 'BOJ5C7', 'room_id': 'D5', 'room_type': 'DELUXE ROOM', 'booked_quantity': 1, 'checkIn': '26-05-23', 'checkOut': '27-05-23', 'price': 3500}}}}}



# # for i in range(len(itemViews['user_acc_info'])):
# def is_date_not_between(date0, date1, date2):
#     format_str = '%d-%m-%y'

#     # Convert date strings to datetime objects
#     date0_obj = datetime.strptime(date0, format_str)
#     date1_obj = datetime.strptime(date1, format_str)
#     date2_obj = datetime.strptime(date2, format_str)

#     # Check if date0 is not between date1 and date2
#     if date1_obj <= date0_obj <= date2_obj:
#         return True
#     else:
#         return False


# loop to print the ID of the current logged in user
user = 'qwe'
for user_id, user_data in itemViews['user_acc_info'].items():
    if user_data['user_name'] == user:
        user_id = user_data['user_id']
        break

print(user_id)

# print(keys[-1])
# m = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10']
# d = ['D1', 'D2', 'D3', 'D4', 'D5']
# s = ['S1', 'S2', 'S3']
# qty = 1


# room = 'DELUXE ROOM'
# for user_id in user_ids:
#     all_rooms = []
#     available_rooms = []
#     reserved_room = []
#     first_letter_room = ''
#     will_reserve = []
#     count = 0
#     total_qty = 0

#     if room == 'MIXED DORM':
#         all_rooms = m
#         first_letter_room = 'M'
#     elif room == 'DELUXE ROOM':
#         all_rooms = d
#         first_letter_room = 'D'
#     elif room == 'SUPERIOR ROOM':
#         all_rooms = s
#         first_letter_room = 'S'

#     print(f"User ID: {user_id}\n-------------------------\nBookings:\n")
#     room_ids = list(itemViews['user_acc_info'][user_id]['booking_dict_info'].keys())
#     for room_id in room_ids:
#         # print(room_id)
#         checkIn_date = (itemViews['user_acc_info'][user_id]['booking_dict_info'][room_id]['checkIn'])
#         checkOut_date = (itemViews['user_acc_info'][user_id]['booking_dict_info'][room_id]['checkOut'])
#         room_type = (itemViews['user_acc_info'][user_id]['booking_dict_info'][room_id]['room_type'])
        
#         print(f"CheckIn: {checkIn_date}\nCheckOut: {checkOut_date}\nRoom Type: {room_type}\nRoom ID: {room_id}\n")
#         if is_date_not_between('26-05-23', checkIn_date, checkOut_date) and is_date_not_between('27-05-23', checkIn_date, checkOut_date) and str(room_type[0]) == first_letter_room:
#             reserved_room.append(room_id)

#     result = [rooms for rooms in all_rooms if rooms not in reserved_room]
#     # print('results: ', result)
#     available_rooms = result

#     for room in available_rooms:
#         if count < qty:
#             will_reserve.append(room)
#             count += 1
#     total_qty += qty
#         #     print(f"User ID: {user_id}\nRoom ID: {room_id}")
#     print('----------------------------------------------------')



# print(f"All Rooms: {all_rooms}")
# print(f"Reserved Room: {reserved_room}")
# print(f"Available Rooms: {available_rooms}")
# print(f"Will Reserve: {will_reserve}")
# print(f"Total Quantity: {total_qty}\n")


    #    if total_qty == len(will_reserve):
    #         for i in range(self.layout.count()):
    #             order_info = self.getOrder(i)
    #             # Unpack the order tuple
    #             get_room_type, get_checkIn_date, get_checkOut_date, get_qty, price = order_info
    #             booking_system.book_rooms_to_dictionary(room_id=will_reserve[i], room_type=get_room_type, booked_quantity=1,
    #                                                     checkIn_date=get_checkIn_date, checkOut_date=get_checkOut_date, price=each)
    #     else:
    #         print("No available rooms")


