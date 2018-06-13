import unittest,random
from Credential import Credential
class TestCredential(unittest.TestCase):
    """
    A class that will be used to testthe functionality of the behaviours in
    the Credential class
    """
    def setUp(self):
        '''
        method that runs before any test
        '''
        self.facebook=Credential(123456,'anilla','anilla@gmail','facebook')
        self.twitter=Credential(12357,'anilla','anilla@gmail','twitter')
        Credential.credentials_list.append(self.facebook)
        Credential.credentials_list.append(self.twitter)
    def tearDown(self):
        '''
        Method that runs after every test
        '''
    # def test_init(self):
    #     '''
    #     test to check whether the objects have been initialized correctly
    #     '''
    #     self.assertEqual(self.credentials_list.password,123456)
    #     self.assertEqual(self.credentials_list.username,"anilla")
    #     self.assertEqual(self.credentials_list.email,"anilla@gmail")
    #     self.assertEqual(self.credentials_list.account,"facebook")



    def test_generatenewpassword(self):
        '''
        Test to determine whether it is possible to generate new passwords
        '''
        self.facebook.gen_randompass()
        test_credential=Credential(123456,'anilla','anilla@gmail','facebook')
        self.assertEqual(self.facebook.password,123456)


    def test_accountexists(self):
        '''
        Test that determines whether an account exists,
        it returns a boolean value
        '''
        self.assertTrue(len(Credential.credentials_list)>0)
        fb = Credential.credentials_list[1]
        self.assertEqual(fb['Your Account'], 'twitter')


    def test_account_creation(self):
        '''
        Test to determine whether it is possible to create an account
        '''
        pass



    def test_display_credentials(self):
        '''
        This is a test to check whether credentials are being displayed
        '''
        pass
if __name__ == "__main__":
    unittest.main()
