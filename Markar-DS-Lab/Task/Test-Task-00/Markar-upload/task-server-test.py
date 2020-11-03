import unittest
import cppyy
import xmlrunner
import io
from xmlrunner.extra.xunit_plugin import transform
import sys

student_dir = sys.argv.pop()
report_dir = sys.argv.pop()

print("Studen Dir:{} \n Report Dir:{}".format(student_dir,report_dir))
#### DO NOT CHANGE #################
code = open(student_dir,'r').read().strip()
cppyy.cppdef(code)

# FUNCTION OR CLASS FROM CODE, NOW YOU CAN TREAT THIS AS PYTHON CODE
from cppyy.gbl import Sum
out = io.BytesIO()

####### ONLY CLASS CAN BE CHANGE AS TEST CASES WILL BE ADDED HERE

class Makar(unittest.TestCase):
    """ Marka Server Test """
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
        
        
############ DO NOT CHANGE #####################
if __name__ == "__main__":
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
    with open(report_dir, 'wb') as report:
        report.write(transform(out.getvalue()))