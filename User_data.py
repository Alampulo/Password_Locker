class UserData:
    """
    A class that geerates new instances of a user account data
    """
    start=0
    users=dict()
    def __init__(self, username,master_password):
        '''
        Method for defining the instances of the object of the class
        '''
        self.username=username
        self.master_password=master_password
        Users.users={'username':self.username,'key':self.master_password}
        User.start+=1

    @classmethod
    def total_users(cls):
        return(f"We currently have {cls}users")
    @classmethod
    def list_of_users(cls):
        return cls.users
    def __repr(self):
        return self
class User:
    """docstring for [object Object]."""
    def new_user(self):
        print("Hello Welcome to Password Locker Apllication.What is your name?")
        username=input()
        password=gen_randompass()
        print(f"Hello {username}.Your password to access the offers of the application is {password}")

        file=open('Cred.txt','a')
        file.write(username)
        file.write('\n')
        file.write(password)
        file.close()
