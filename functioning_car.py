#!/usr/bin/python
#Libraries
import sys
import tkinter

#Car brand/make/year/speed

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
