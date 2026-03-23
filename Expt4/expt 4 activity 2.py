# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 05:21:14 2026

@author: User
"""
prices = []

n = int(input("Enter number of products: "))

for i in range(n):
    p = float(input("Enter product price: "))
    prices.append(p)

total = sum(prices)

print("Product Prices:", prices)
print("Total Bill:", total)
