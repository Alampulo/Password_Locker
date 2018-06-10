import random
from User_data import UserData
from Credential import Credential
def main():
    '''
    A function that allows the user to choose what he wants
    '''
    print("Hello Welcome to Password Locker Apllication.What is your name?")
    username=input()
    print(f"Hello {username}.What would you like to do?")
    while True:
        print("Use these Short Codes provided below to decide on something:1-create new account,2-display contacts")
        Short_Code=int(input())
        if Short_Code==1:
            print("crete new account")
            print('\n')
            print("First Name.....")
            First_name=input()
            print("Second name...")
            Second_name=input()
