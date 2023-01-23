
from math import *
import time
import random 

#       Variant 1      #

#1

#Так и не нашел решения, каким образом сделать это горизонтально.

#try:
#        n = int(input("Mitu jõulupuud soovite joonistada? (0-9)\n "))
        
#        a1 ="    /V\    "   
#        a2 ="   \n   / V \   "
#        a3 ="  \n  / V V \  "  
#        a4 =" \n /VV V VV\ "       
 
#        c1=" "
#        c2=" "
#        c3=" "
#        c4=" "

#        if n> 0 and n<10:
#            for x in range(n):
#                print(c1,c2,c3,c4)
#                print(a1,a2,a3,a4)
#        else:
#            print("Rohkem kui 9 jõulupuud on võimatu välja panna")
#            time.sleep(1)
#except:
#    print("See ei ole number")
    

#2


#R = int(input("Sisestage number: "))
#x=0
#while True:
#    if x==R:
#        break
#    elif x%2==1:

#        print(x, end=" ")
#    x+=1
#ans = input("\nKas te soovite umnozit see?(Yah,Ei) ")
#while ans == "Yah":
#    c=R*suma
#    print(c)
#    break
#else:
#    print("ok")




#3

#Проблема только одно код считывает 0 тоже, даже если он не вывелся на экран.


#print("Numbrit:")
#e=random.randint(1,50)
#i=random.randint(-100,100)

#a=-100
#d=0
#while a !=i:
#    if a>100:
#        break
#    print(a)
#    a+=e
#    if a>0:
#        d+=1

#print(f"\nSiin on {d} Positivned arved ")
        


#4


#n = int(input("Sisestage arv: "))
#a=b=0
#while n>0:
#    if n%2 == 0:
#        a += 1
#    else:
#        b += 1
#    n = n//10
#print(f"Kümned - {a}, Paaritud - {b}")