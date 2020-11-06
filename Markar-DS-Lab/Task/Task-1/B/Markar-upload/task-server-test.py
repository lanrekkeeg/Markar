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
out = io.BytesIO()

####### ONLY CLASS CAN BE CHANGE AS TEST CASES WILL BE ADDED HERE

class Makar(unittest.TestCase):
    """ Marka Local Test """

    def test1_A(self):
        from cppyy.gbl import leave_2nd_print_reverse    
        self.assertEqual(leave_2nd_print_reverse("axxx32sabdfb",2,0), "fbs3x")
        
    def test2_A(self):
        
        from cppyy.gbl import leave_2nd_print_reverse        
        self.assertEqual(leave_2nd_print_reverse("23242$@@#@#@",2,0), "##@22")
        
    def test3_A(self):
        from cppyy.gbl import leave_2nd_print_reverse
        self.assertEqual(leave_2nd_print_reverse("23232323",2,0), "222")

    def test4_A(self):
        
        from cppyy.gbl import leave_2nd_print_reverse
        self.assertEqual(leave_2nd_print_reverse("dfdwewe",2,0), "eed")

    def test5_A(self):
        
        from cppyy.gbl import leave_2nd_print_reverse
        self.assertEqual(leave_2nd_print_reverse("adsdsrsd",2,0), "sss")
    def test6_A(self):
        
        from cppyy.gbl import leave_2nd_print_reverse
        self.assertEqual(leave_2nd_print_reverse("aabdfbsds",2,0), "ssfb")

    def test7_A(self):
        
        from cppyy.gbl import leave_2nd_print_reverse
        self.assertEqual(leave_2nd_print_reverse("aabdfbwew",2,0), "wwfb")

    def test8_A(self):
        
        from cppyy.gbl import leave_2nd_print_reverse
        self.assertEqual(leave_2nd_print_reverse("",2,0), "")

    def test1_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("111123112322311232000230",2,0,0), 1)
        
    def test2_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("1111231123223112320002309",9,9,0), 0)

    def test3_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("8111123112322311232000230",8,1,0), 1)

    def test4_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("111123112365566522311232000230",5,6,0), 1)
    def test5_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("111123112322311232000230",1,2,0), 3)
    def test6_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("1111231123223178787777781232000230",7,8,0), 3)
    def test7_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("111123112322311232000230",2,0,0), 1)
    def test8_B(self):
        
        from cppyy.gbl import count_after_specific
        self.assertEqual(count_after_specific("111123112322311232000230099",0,9,0), 1)
        
############ DO NOT CHANGE #####################
if __name__ == "__main__":
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
    with open(report_dir, 'wb') as report:
        report.write(transform(out.getvalue()))