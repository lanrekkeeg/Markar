import unittest
import cppyy
import xmlrunner
import io
from xmlrunner.extra.xunit_plugin import transform
import logging
logging.basicConfig(level=logging.DEBUG)
import sys

code = open("compute_sum.cpp",'r').read().strip()
try:
    status = cppyy.cppdef(code)
except:
#if status != True:
    sys.exit("*************************Compilation Error*************************")
from cppyy.gbl import compute_sum
out = io.BytesIO()

def sum(a, b):
    return a+b
class OutcomesTest(unittest.TestCase):
    def test_sum(self):
        assert sum(1,1) == 2

    def test_func1(self):
        out = compute_sum(1,3) 
        assert out == 6

    def d_test_func2(self):
        assert compute_sum(1,6) == 21

    def test_func3(self):
        self.fail()
        assert compute_sum(1,3) == 6

if __name__ == '__main__':
    #unittest.main()
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
    with open('report.xml', 'wb') as report:
        report.write(transform(out.getvalue()))