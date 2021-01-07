#!/usr/bin/python
#Libraries
import sys
import tkinter

# Car brand/make/year/speed

class car:
    def __init__(self, brand, make, year):
        self.brand = brand
        self.make = make
        self.year = year
        self.speed = 0

    def car_brand(self):
        return self.brand

    def car_make(self):
        return self.make

    def car_year(self):
        return self.year

    def car_speed(self):
        return self.speed

    #Car functions
    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 10

def car():
    print("What car would you like to drive?")
    car_brand = input("Car Brand: ")
    car_model = input("Car Model: ")
    car_year = input("Car Year: ")
    def car_of_choice():
        print("Is", car_brand, car_model, car_year, "your car of choice? ")
        yes_no = input()

        if yes_no == "y":
            pass

        elif yes_no == "n":
            car()

        else:
            print("Invalid!")
            car_of_choice()

    car_of_choice()
    def road():
        print("+ to accelerate  | - to brake")
        pedal = input()

        if pedal == "+":
            car_of_choice == ""
        

# Program Flow
car()
