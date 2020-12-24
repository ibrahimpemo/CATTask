#!/bin/python3

print ("Task For CAT A. Bear and Big Brother | BY Ibrahim Maher")

limak_bob= input("Enter Limak and Bob weigh : ").split()


a = int(limak_bob[0])
b = int(limak_bob[1])
years = 0
 
while a <= b:
    a *= 3
    b *= 2
    years += 1



print ("The solution is :" ,  years)    
print ("After" , years , "years, Limak will be larger (strictly heavier) than Bob")