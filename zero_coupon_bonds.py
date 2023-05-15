# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value
def calculate_present_value(future_value, discount_rate, compounding_periods, years):
    present_value = future_value / ((1 + (discount_rate / compounding_periods)) ** (compounding_periods * years))
    present_value_rounded = round(present_value, 2)
    
    return present_value_rounded

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variable
bond_value = calculate_present_value(future_value, discount_rate, compounding_periods, years)

# @TODO: Determine if the bond is worth it
if bond_value < price:
    print("Purchase the bond")
    
elif bond_value > price:
    print("Don't purchase the bond")
    
else:
    print("Bond is selling at fair market value, hold purchase or sale")