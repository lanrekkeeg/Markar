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

    def test2_A(self):
        try:
            from cppyy.gbl import leave_2nd_print_reverse
        except Exception as exp:
            logging.warning("Exception raised:{}".format(exp))
            raise SkipTest
        self.assertEqual(leave_2nd_print_reverse("aabdfb",2,0), "fb")


    def test3_A(self):
        try:
            from cppyy.gbl import leave_2nd_print_reverse

        except:
            raise SkipTest
        self.assertEqual(leave_2nd_print_reverse("aabd",2,0), "b")

    def test4_A(self):
        try:
            from cppyy.gbl import leave_2nd_print_reverse

        except:
            raise SkipTest
        self.assertEqual(leave_2nd_print_reverse("sdcsrdcsds",2,0), "dcrc")


    def test5_A(self):
        try:
            from cppyy.gbl import leave_2nd_print_reverse

        except:
            raise SkipTest
        self.assertEqual(leave_2nd_print_reverse("a",2,0), "")


    def test1_B(self):
        try:
            from cppyy.gbl import count_after_specific
        except:
            raise SkipTest
        self.assertEqual(count_after_specific("111123112322311232000230",2,3,0), 5)

    def test2_B(self):
        try:
            from cppyy.gbl import count_after_specific
        except:
            raise SkipTest
        self.assertEqual(count_after_specific("111123112322311232000230",2,5,0), 0)


    def test3_B(self):
        try:
            from cppyy.gbl import count_after_specific
        except:
            raise SkipTest
        self.assertEqual(count_after_specific("111123112322311232000230",3,4,0), 0)


    def test4_B(self):
        try:
            from cppyy.gbl import count_after_specific
        except:
            raise SkipTest
        self.assertEqual(count_after_specific("111123112322311232000230999",9,9,0), 2)


    def test5_B(self):
        try:
            from cppyy.gbl import count_after_specific
        except:
            raise SkipTest
        self.assertEqual(count_after_specific("8111123112322311232000230",8,1,0), 1)

        
if __name__ == '__main__':
    kwargs = {
    "output": "final_output",
    "report_name": "final",
    "failfast": True }
    unittest.main(testRunner=HTMLTestRunner(os.getcwd()+"/report/", "local"))