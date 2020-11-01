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
#code = open("compute_sum.cpp",'r').read().strip()
cppyy.cppdef(code)

# FUNCTION OR CLASS FROM CODE, NOW YOU CAN TREAT THIS AS PYTHON CODE
from cppyy.gbl import compute_sum
out = io.BytesIO()

####### ONLY CLASS CAN BE CHANGE AS TEST CASES WILL BE ADDED HERE
class OutcomesTest(unittest.TestCase):
    def test_func1(self):
        out = compute_sum(1,3) 
        assert out == 6

    def test_func2(self):
        assert compute_sum(1,6) == 21

    def test_func3(self):
        assert compute_sum(1,3) == 6
     
    def test_func4(self):
        assert compute_sum(1,3) == 8
        
    def test_func5(self):
        assert compute_sum(1,3) == 9
        
        
############ DO NOT CHANGE #####################

if __name__ == "__main__":
    #unittest.main()
    #print(sys.argv.pop())
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
    with open(report_dir, 'wb') as report:
        report.write(transform(out.getvalue()))