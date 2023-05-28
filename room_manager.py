# class RoomManager:
#     def __init__(self):
#         self.rooms = []

#     def create_rooms(self):
#         mixed_dorm = MixedDorm()
#         deluxe_room = DeluxeRoom()
#         superior_room = SuperiorRoom()
#         self.rooms = [mixed_dorm, deluxe_room, superior_room]

#     def get_available_rooms(self, room_type):
#         for room in self.rooms:
#             if room.room_type == room_type:
#                 return room.rooms_available

#         return set()

#     def book_rooms(self, room_type, booked_room_quantity):
#         for room in self.rooms:
#             if room.room_type == room_type:
#                 return room.book_rooms(booked_room_quantity)

#         return set()

#     def list_available_rooms(self, room_type):
#         for room in self.rooms:
#             if room.room_type == room_type:
#                 room.list_available_rooms()

#     def get_cost(self, room_type, booked_room_quantity, days_booked):
#         for room in self.rooms:
#             if room.room_type == room_type:
#                 return room.get_cost(booked_room_quantity, days_booked)

#         return 0
