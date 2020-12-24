#!/bin/python3

print ("Task For CAT A. Mishka and Contest | BY Ibrahim Maher")

n_k= input("Enter the number of problems in the contest and Mishka's problem-solving skill : ").split()


n = int(n_k[0])
k = int(n_k[1])
sol = 0

a = list(map(int,input("Enter The problems : ").split()))


while a and a[0]<=k:
    a.pop(0)
    sol+=1
a.reverse()

while a and a[0]<=k:
    a.pop(0)
    sol+=1

if sol == 0:
    print ("The solution is :" ,  sol)
    print ("She cannot solve any problem")
else:
    print ("The solution is :" ,  sol)
    print ("Mishka can solve " , sol , "problems" )