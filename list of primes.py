# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:21:36 2024

@author: Anupam Nair
"""
num_tocheck=int(input("enter a number till where you want to check: "))
list_prime=[]

for num in range(2,num_tocheck+1):
    if num==2:
        list_prime.append(num)
    else:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            list_prime.append(num)    
print("the list of primes upto  ",num_tocheck, " are " , list_prime)                