from pyunitreport import HTMLTestRunner
import unittest
import os
import requests
import cppyy
import logging
from unittest.case import SkipTest

logging.basicConfig(level=logging.DEBUG)

##### DO NOT CHANGE ########
code = open("task.cpp",'r').read().strip()
cppyy.cppdef(code)
#############################
### FOR TEACHER ONLY ##############
class Makar(unittest.TestCase):
    """ Marka Local Test """

    def test1_A(self):
        try:
            from cppyy.gbl import reverse_from_special_character
        except:
            raise SkipTest
        self.assertEqual(reverse_from_special_character("abcdef.sdssd",'.',0), "fedcba")
        
    def test2_A(self):
        try:
            from cppyy.gbl import reverse_from_special_character
            
        except:
            raise SkipTest
        self.assertEqual(reverse_from_special_character("ab/cdefsdssd",'/',0), "ba")
        
    def test3_A(self):
        try:
            from cppyy.gbl import reverse_from_special_character
            
        except:
            raise SkipTest
        self.assertEqual(reverse_from_special_character("abcde.f.sds.sd",'.',0), "edcba")

    def test4_A(self):
        try:
            from cppyy.gbl import reverse_from_special_character

        except:
            raise SkipTest
        self.assertEqual(reverse_from_special_character("abcdef.sds,sd",',',0), "sds.fedcba")

    def test5_A(self):
        try:
            from cppyy.gbl import reverse_from_special_character
        except:
            raise SkipTest
        self.assertEqual(reverse_from_special_character("abcde!f.sdssd",'!',0), "edcba")

    def test1_B(self):
        try:
            from cppyy.gbl import count_specific_number
            
        except:
            raise SkipTest
        self.assertEqual(count_specific_number("111122111112220000",1,0), 9)
        
    def test2_B(self):
        try:
            from cppyy.gbl import count_specific_number
            
        except:
            raise SkipTest
        self.assertEqual(count_specific_number("11112211119999912220000",9,0), 5)

    def test3_B(self):
        try:
            from cppyy.gbl import count_specific_number
            
        except:
            raise SkipTest
        self.assertEqual(count_specific_number("8111122111112220000",8,0), 1)

    def test4_B(self):
        try:
            from cppyy.gbl import count_specific_number
            
        except:
            raise SkipTest
        self.assertEqual(count_specific_number("1111221111122200007",7,0), 1)
    def test5_B(self):
        try:
            from cppyy.gbl import count_specific_number
        except:
            raise SkipTest
        self.assertEqual(count_specific_number("61111221111122200006",6,0), 2)

if __name__ == '__main__':
    kwargs = {
    "output": "final_output",
    "report_name": "final",
    "failfast": True }
    unittest.main(testRunner=HTMLTestRunner(os.getcwd()+"/report/", "local"))