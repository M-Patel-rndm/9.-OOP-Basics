class Flight:

    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat Booked")
        else:
            print("No Seats Available")


flight = Flight(3)

flight.book_seat()
flight.book_seat()

print("Remaining Seats =", flight.seats)