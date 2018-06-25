import random,string
class Credential:
    """class that create instances of the Credential class"""
    credentials_list=[]
    def __init__(self,password,username,email,account):

        '''
        method that allows us to define properties of our objects
        Args:
        :random password generated to an individual
        '''
        self.password=password
        self.username=username
        self.email=email
        self.account=account
        Credential.credentials_list.append({'Your Account':self.account, 'Your Username':self.username,'Email':self.email,'Password':self.password})

    
    @classmethod
    def gen_randompass(cls):
        '''
        Method that generates random master passwords
        '''
        password=random.randint(123454,789353)
        return(password)

    @classmethod
    def exit_account(cls):
        '''
        Method that alloow one to exist
        '''
        while True:
            print("Thank You")
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
        if Credential.credentials_list:
            print(f"account:{account}\n username:{username}\n email:{email}")
            y=1
            for creds in Credential.credentials_list:
                print(f'\n{y}')
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
            print("Sorry no account to be deleted!")
