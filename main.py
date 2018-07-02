import random
from User_data import UserData,User
from Credential import Credential

def main():
    '''
    A function that allows the user to choose what he wants
    '''
    print("Hello Welcome to Password Locker Apllication.What is your name?")
    username=input()
    username=open('Cred.txt','a').write(username)
    password=gen_randompass()
    print(f'Welcome your password to acces password locker in future is{password}')
    print("Use these Short Codes provided below to decide on something:1-create new account,2-display contacts,5-login,9-exit")
    Short_Code=int(input())
    if Short_Code==1:

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
#

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
    Function that creates an account of a user
    '''

    print('Enter your Username:')
    username=input()
    if username in open('Cred.txt').read():
        print('Add account details of your choice')
        print("Enter your Account:")
        account=input()
        print('your password:')
        password= input()
        email=input("Enter your email:")
        userdata= username,account,password
        print(userdata)
        f= open(f"{ username }.txt","w+")
        f.write(str(userdata))
        f.close()
    else:
        print('not found!')
# create_acount()


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
#     # account=Credential.account
#     # username=Credential.username
#     # email=Credential.email
#     # password=gen_randompass()
#     Credential(password,username,email,account)
#     # password=random.randint(123454,789353)
#     # Credential(password,username,email,account)
#     while True:
#         print(Credential.credentials_list)
#     else:
#         print("You have no accounts yet")
if __name__ == '__main__':
    main()
