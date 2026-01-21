class Movie:
    def __init__(self,title,available_seats):
        self.title=title
        self.available_seats=available_seats
    def book_seats(self,seats):
        if seats<=self.available_seats:
            self.available_seats -=seats
            print(f"Booked {seats} seats for {self.title} Successfully.")
        else:
            print(F"Not enough seats for {self.title}")
title=input("Enter the movie:").strip()
available_seats=int(input("Enter available seats:"))
movie=Movie(title,available_seats)
while True:
    seat=int(input("Enter the seat to book:"))
    movie.book_seats(seat)
