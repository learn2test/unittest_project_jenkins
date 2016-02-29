'''
Created on Feb 27, 2016

@author: User
'''
import unittest

class Test_1(unittest.TestCase):


    def setUp(self):
        print "Setting Up Environment"


    def tearDown(self):
        print "Tearing down Environment"


    def test_method_1(self):
        print "running test method #1"
        self.assertEqual(2, 3, "eerorrr")
 
    def test_method_2(self):
        print "running test method #2"
        pass

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    #suite = unittest.TestLoader().loadTestsFromTestCase(Test_1)
    #unittest.TextTestRunner(verbosity=2).run(suite)