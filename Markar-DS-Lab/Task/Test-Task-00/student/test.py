from pyunitreport import HTMLTestRunner
import unittest
import os
import requests
import cppyy
import logging

##### DO NOT CHANGE ########
code = open("task.cpp",'r').read().strip()
cppyy.cppdef(code)
#############################
### FOR TEACHER ONLY ##############
from cppyy.gbl import Sum
class Makar(unittest.TestCase):
    """ Marka Local Test """

    def test1(self):
        S1 = Sum()
        self.assertEqual(S1.sum(1,2), 3)

    def test2(self):
        S1 = Sum()
        self.assertEqual(S1.sum(3,2), 5)

    def test3(self):
        S1 = Sum()
        self.assertEqual(S1.sum(3,3), 6)

    def test4(self):
        S1 = Sum()
        self.assertEqual(S1.sum(123,2), 125)

    def test5(self):
        S1 = Sum()
        self.assertEqual(S1.sum(232,1), 233)

    def test6(self):
        S1 = Sum()
        self.assertEqual(S1.sum(231,1), 232)
    
    def test7(self):
        S1 = Sum()
        self.assertEqual(S1.sum(780,9), 789)

    def test8(self):
        S1 = Sum()
        self.assertEqual(S1.sum(332,1), 333)

    def test9(self):
        S1 = Sum()
        self.assertEqual(S1.sum(342,1),343)

    def test10(self):
        S1 = Sum()
        self.assertEqual(S1.sum(341,1), 342)

if __name__ == '__main__':
    kwargs = {
    "output": "final_output",
    "report_name": "final",
    "failfast": True }
    unittest.main(testRunner=HTMLTestRunner(os.getcwd()+"/report/", "comput"))