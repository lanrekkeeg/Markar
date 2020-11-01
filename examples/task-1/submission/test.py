import unittest
import os
import requests

class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(2, 2)

    def test_fail2(self):
        """ This test should fail. """
        self.assertEqual(2, 2)
    
    def test_pass(self):
        """ This test should Pass. """
        self.assertEqual(1, 1)

    def test_pass2(self):
        """ This test should fail. """
        self.assertEqual(1, 4)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(os.getcwd()+"/report/", "comput"))