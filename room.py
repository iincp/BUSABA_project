from abc import ABC, abstractmethod


class Room(ABC):
    
    def __init__(self, room_id, room_type, max_quantity, booked_room_quantity, days_booked):
        self.room_id = room_id
        self.room_type = room_type
        self.max_quantity = max_quantity
        self.booked_room_quantity = booked_room_quantity
        self.days_booked = days_booked
        self.rooms_available = set([f"{room_id}{i}" for i in range(1, max_quantity + 1)])

    # randomly books available rooms in the list called rooms_available
    def book_rooms(self, booked_room_quantity):
        from account import Account
        logged_in_user = Account.logged_in_user
        if len(self.rooms_available) >= booked_room_quantity:
            # Get the specified number of available rooms
            booked_rooms = set(list(self.rooms_available)[:booked_room_quantity])
            self.rooms_available -= booked_rooms
            booked_room_quantity = booked_room_quantity
            print(
                f"{logged_in_user}Successfully booked {booked_room_quantity} {self.room_type} room(s): {booked_rooms}")
            return booked_rooms  # Return the set of booked room IDs
        else:
            print(f"Not enough {self.room_type} rooms available.")
            return set()  # Return an empty set if booking failed

    def list_available_rooms(self):
        print(f"Available {self.room_type} rooms:")
        for room in self.rooms_available:
            print(room)

    @abstractmethod
    def get_cost(self):
        pass
 
class MixedDorm(Room):
    #innitialize days bookeds
    def __init__(self):
        #(room_id, room_type, max_quantity)
        super().__init__('M', 'Mixed Dorm', 10, 0, 0)

    def get_cost(self, booked_room_quantity, days_booked):
        cost = (800 * booked_room_quantity) * days_booked
        return cost

class DeluxeRoom(Room):
    def __init__(self):
        super().__init__('D', 'Deluxe', 5, 0, 0)

    def get_cost(self, booked_room_quantity, days_booked):
        cost = (3500 * booked_room_quantity) * days_booked
        return cost


class SuperiorRoom(Room):
    def __init__(self):
        super().__init__('S', 'Superior', 3, 0, 0)

    def get_cost(self, booked_room_quantity, days_booked):
        cost = (5000 * booked_room_quantity) * days_booked
        return cost
    
def calculate_total_price(Mcost, Dcost, Scost):
    total_price = Mcost + Dcost + Scost
    return total_price
    

# mixed_dorm = MixedDorm()

# mixed_dorm.list_available_rooms()
# print('\n')

# mixed_dorm.book_rooms(5)
# mixed_dorm.list_available_rooms()

# mixed_dorm.book_rooms(5)
# mixed_dorm.list_available_rooms()



# # deluxe_room = DeluxeRoom(0, 2)
# # superior_room = SuperiorRoom(0, 1)

# print(mixed_dorm.get_cost(3, 3))
# # print("Booked rooms:", mixed_dorm.book_rooms())
# print(mixed_dorm.get_room_type())
# print(mixed_dorm.get_booked_room_quantity())
# print('\n')


# deluxe_room.book_rooms()
# deluxe_room.list_available_rooms()
# print(deluxe_room.get_cost())
# print('\n')

# superior_room.book_rooms()
# superior_room.list_available_rooms()
# print(superior_room.get_cost())
# print('\n')

# superior_room.book_rooms()
# print('\n')

# print(calculate_total_price(mixed_dorm.get_cost(),
#       deluxe_room.get_cost(), superior_room.get_cost()))

# print('\n')

