import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Person:
    def __init__(self, name, last_name, ID, birthday, credit):
        self.name=name
        self.last_name=last_name
        self.ID=ID
        self.birthday=birthday
        self.credit=credit



def Check_ID():
    pass #Is it availabe? return int?
def Register(name, last_name, ID, birthday, credit):
    pass #write it in file
def Market():
    pass
def Assets():
    pass
def Buy():
    pass
def Sell():
    pass


print("Enter date:")
date=input()


#who are you?
print("1. sign in\n2. sign up")
order=input()
if order=='1':
    print("Enter your ID:", end=" ")
    if Check_ID():#check the is the ID valid or not
        pass
    else:
        print("ID not found.\n")
        #order='2'
if order=='2':
    print("Enter your name, last name, ID, birthday, and credit seprated with comma\n")
    name, last_name, ID, birthday, credit= input().split(",")
    Register(name, last_name, ID, birthday, credit) 


market=pd.read_csv("stock_market_data.csv")
market.head()

while True:
    order=input()
    print("1.Market\n2.Assets\n3.Buy\n4.Sell\n5.Next day\n6.Exit")
    if order=='1':
        Market()
    elif order=='2':
        Assets()
    elif order=='3':
        Buy()
    elif order=='4':
        Sell()
    elif order=='5':
        pass
    elif order=='6':
        print("Thank you for choosing us. Good luck.")
        break

    