#script for car prices
#import numpy as np
cars = dict()
cars["toyota hilux"] =300000
cars["toyota corolla"] =40000
cars["toyota yaris"] =10000
cars["nissan navara"] =70000
cars["kia picanto"] =4000
cars["renault logan"] =7000
cars["toyota fortuner"] =20000
cars["mercedes g wagon"] =500000
cars["honda civic"] =35000
cars["mitsubishi pajero"] =40000
cars["toyota vitz"] =9000
cars["chevrolet camaro"] =30000
cars["toyota prius"] =50400
cars["hyundai elantra"] =85000
cars["hyundai accent"] =25000
cars["hyundai santa fe"] =40000
cars["ford escape"] =306000
cars["mitsubishi outlander"] =950000
cars["ford mustang"] =750000
cars["renault duster"] =95000
cars["audi a4"] =450000
cars["audi a6"] =550000
cars["chevrolet corvette"] =780000
cars["mini cooper"] =966000
cars["chevrolet trailblazer"] =550000
cars["chevrolet cruze"] =100400
cars["nissan rogue"] =30000
cars["toyota tacoma"] =60000
cars["acura mdx"] =750000
cars["acura rdx"] =260000
cars["acura nsx"] =95000
cars["acura ilx"] =706000

print("Welcome to Broni car dealership")

print("Which car would you like to purchase?")

order = input()
if cars.get(order):
    print("The "+order+" costs $" + str(cars.get(order)))
else:
    print("Sorry "+order+" is unavialable")



https://github.com/Kwabro66/cars-dealership.git




