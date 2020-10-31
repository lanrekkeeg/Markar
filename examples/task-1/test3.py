import random
import unittest
import xmlrunner

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))
    def test_sum(self):
        assert 1 == 2
    def test_sum2(self):
        assert True
    def test_sum3(self):
        assert True

#if __name__ == '__main__':
#    unittest.main(
#        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
#        failfast=False, buffer=False, catchbreak=False)
if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)