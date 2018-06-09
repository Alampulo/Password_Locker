import random,string
class Credential:
    """class that create instances of the Credential class"""

    def __init__(self,master_password,username,email,account):
        credentials_list=[]
        '''
        method that allows us to define properties of our objects
        Args:
        master_password:random password generated to an individual
        '''
        self.master_password=master_password
        self.username=username
        self.email=email
        self.account=account
        Credential.credentials_list.append({'Your Account:'self.account,' Your Username:'self.username,'Enail:'self.email,'Password:'self.password})

    @classmethod
    def create_acount(cls):
        '''
        Method that creates an account
        '''
        pass
    @classmethod
    def gen_randompass(cls):
        '''
        Method that generates random master password of range 1 to 7
        '''
        master_password=Credential(random.randint(1,7))
        print(master_password)

    @classmethod
    def store_pass(cls):
        '''
        Method that stores generated passwords
        '''
        pass
    @classmethod
    def copy_credentials(cls):
        '''
        Method that allows one to copy and paste some credentials
        '''
        pass

    @classmethod
    def display_credentials(cls):
        '''
        This method enables us to display accounts for a given user
        '''
        if cls.credentials_list:
            print(account&&username&&email&&master_password)
        else:
            print("You have no accounts yet")
    @classmethod
    def delete_credentials(arg):
        '''
        This method allows the user to delete his or her credentials at will
        '''
        if cls.credentials_list:
            for cred in cls.credentials_list:
                if cred['account']==acount:
                    cls.credentials_list.remove(cred)
        else:
            print("Sorry no accont to be deleted!")
