# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:11:57 2019

@author: james
"""

#Import our custom package
from shopping_cart import ShoppingCart

#Initialize an instance of our shopping cart class
shopping_cart = ShoppingCart()
shopping_cart = ShoppingCart() #Add a line to reinitialize an instance of the class
print(shopping_cart.total)
print(shopping_cart.employee_discount)
print(shopping_cart.items)

shopping_cart.add_item("rainbow sandals", 45.99) # 45.99
shopping_cart.add_item("agyle socks", 10.50) # 56.49
shopping_cart.add_item("jeans", 50.00, 3) # 206.49
shopping_cart.mean_item_price() # 41.29
