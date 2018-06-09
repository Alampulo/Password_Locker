class UserData:
    """
    A class that geerates new instances of a user object
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
        pass
    def __repr(self):
        return self
        
