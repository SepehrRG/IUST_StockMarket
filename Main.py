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



def Check_ID(ID):
    f = open("Accounts.txt")
    while True:
        s=f.readline()
        if s[0:10]==ID:
            print("HIIIIII")
            f.close()
            return True
        elif s=="":
            f.close()
            return False
def Register(ID, name, last_name, birthday, credit):
    f = open("Accounts.txt", "a")
    f.write('\n'+ID+','+name+','+last_name+','+birthday+','+credit)
    f.close()
def Market():
    pass
def Assets():
    pass
def Buy():
    pass
def Sell():
    pass
def Rewrite_credit():
    pass


print("Enter date:")
date=input()
f = open("Accounts.txt", "a")
f.close()
f = open("temp_Accounts.txt", "a")
f.close()
market=pd.read_csv("stock_market_data.csv")
market.head()



#who are you?
print("1. sign in\n2. sign up")
order=input()
if order=='1':
    print("Enter your ID:", end=" ")
    ID=input()
    if Check_ID(ID):#check the is the ID valid or not
        pass
    else:
        print("ID not found.\n")
        order='2'
if order=='2':
    print("Enter your ID, name, last name, birthday, and credit seprated with comma\n")
    ID, name, last_name, birthday, credit= input().split(",")
    Register(ID, name, last_name, birthday, credit) 


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
        Rewrite_credit()
        break

    