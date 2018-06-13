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
        print("Use these Short Codes provided below to decide on something:1-create new account,2-display contacts,5-login,9-exit")
        Short_Code=int(input())
        if Short_Code==1:
            # print("crete new account")
            # print('\n')
            # print("Email.....")
            # Email=input()
            # Master_Password=gen_randompass()
            # print(f"Your Master Password is {Master_Password}")
            create_acount()
        elif Short_Code==2:
            display_credentials()
        elif Short_Code==5:
            login()
    else:
        print("Wrong password or email")
        print("In case you've forgotten ,sign up")
        print("Select an option:\n 3-login \n 4-try again")
        option=int(input())
        if option==3:
            login()
        elif option==4:
            login()
        else:
            create_acount()
        if Short_Code==9:
            exit_account()


def login():
    '''
    A function that allows one to login to their current account
    '''
    if Credential==True:
        print(Credential.credentials_list)
    else:
        print("Sorry you have no account yet")

def create_acount():
    '''
    Method that creates an account of a user
    '''
    account=input("Enter your Account:")
    username=input("Enter your user name:")
    email=input("Enter your email:")
    password=gen_randompass()
    Credential(password,username,email,account)
    print(f"You have successfully created an account your masterpassword will be:{password}")
    print(Credential.credentials_list)


def gen_randompass():
    '''
    Method that generates random master password of range 1 to 6
    '''
    password=random.randint(123454,789353)
    return(password)

# def display_credentials():
#     '''
#     This method enables us to display accounts for a given user
#     '''
#     if Credential.credentials_list:
#         print(f"account:{account}\n username:{username}\n email:{email}")
#         y=1
#         for creds in Credential.credentials_list:
#             print(f'\n{y}')
#     else:
#         print("You have no accounts yet")
def display_credentials():
    '''
    This method enables us to display accounts for a given user
    '''
    Creedential(password,username,email,account)
    while True:
        print(Credential.credentials_list)
    else:
        print("You have no accounts yet")
if __name__ == '__main__':
    main()
