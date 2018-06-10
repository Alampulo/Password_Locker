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
            print("Email.....")
            Email=input()
            print("Master_Password..")
            Master_Password=int(input())
        else:
            print("Wrong password or email")
            print("In case you've forgotten ,sign up")
            print("Select an option:\n 1-login \n 2-try again")
            option=int(input())
            if option==1:
                main()
            elif option==2:
                sign_up()
            else:
                sign_up()


def sign_up():
    '''
    A function that allows one to sign up as new user or when one has forgotten the password
    '''
    username=input("Enter your user name here:")
    while True:
        master_password=gen_randompass()
