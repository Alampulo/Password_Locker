import unittest,Credential,random
class TestCredential(unittest.TestCase):
    """
    A class that will be used to testthe functionality of the behaviours in
    the Credential class
    """
    def test_generatenewpassword(self,new_password):
        '''
        Test to determine whether it is possible to generate new passwords
        '''
        self.new_password.generatenewpassword()
        new_password=random.randint(1,7)
        self.assertEqual(new_password,master_password)

if __name__ == "__main__":
    unittest.main()
