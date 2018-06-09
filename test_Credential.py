import unittest,Credential,random
class TestCredential(unittest.TestCase):
    """
    A class that will be used to testthe functionality of the behaviours in
    the Credential class
    """

    def setUp(self):
        '''
        method that runs before any test
        '''
        self.user0=Credential()
        self.newlist=[]
        self.newlist.append(self.user0)
    def test_generatenewpassword(self,new_password):
        '''
        Test to determine whether it is possible to generate new passwords
        '''
        self.new_password.generatenewpassword()
        new_password=random.randint(1,7)
        self.assertEqual(new_password,master_password)
        pass

    def test_accountexists(self):
        '''
        Test that determines whether an account exists,
        it returns a boolean value
        '''
        pass
    def test_account creation(self):
        '''
        Test to determine whether it is possible to create an account
        '''
        pass
    def test_storespass(self):
        '''
        test to determine whether it is possible to store passwords
        '''
    def test_copycredentials(self):
        '''
        test whether it is possible to copy the users input
        '''
        pass
if __name__ == "__main__":
    unittest.main()
