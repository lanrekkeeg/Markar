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
### FOR TEACHER ONLY ##############
class Makar(unittest.TestCase):
    """ Marka Local Test """

    def test1_A(self):
        from cppyy.gbl import reverse_from_special_character    
        self.assertEqual(reverse_from_special_character(".abcdef.sdssd",'.',0), "")
        
    def test2_A(self):
        
        from cppyy.gbl import reverse_from_special_character        
        self.assertEqual(reverse_from_special_character("abcdef.sds%sd",'%',0), "sds.fedcba")
        
    def test3_A(self):
        from cppyy.gbl import reverse_from_special_character
        self.assertEqual(reverse_from_special_character("abcde'fsdssd",'\'',0), "edcba")

    def test4_A(self):
        
        from cppyy.gbl import reverse_from_special_character
        self.assertEqual(reverse_from_special_character("abc-defsdssd",'-',0), "cba")

    def test5_A(self):
        
        from cppyy.gbl import reverse_from_special_character
        self.assertEqual(reverse_from_special_character("abcd.ef.sdssd",'.',0), "dcba")
    def test6_A(self):
        
        from cppyy.gbl import reverse_from_special_character
        self.assertEqual(reverse_from_special_character("/abcdef.sdssd",'/',0), "")

    def test7_A(self):
        
        from cppyy.gbl import reverse_from_special_character
        self.assertEqual(reverse_from_special_character("abc!def.sdssd",'!',0), "cba")

    def test8_A(self):
        
        from cppyy.gbl import reverse_from_special_character
        self.assertEqual(reverse_from_special_character("!abcdef.sdssd",'!',0), "")

    def test1_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("111122111112220000",2,0), 5)
        
    def test2_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("111122111112220000",9,0), 0)

    def test3_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("111.2323232",1,0), 3)

    def test4_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("11133333222255",5,0), 2)
    def test5_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("1111221111122333320000",3,0), 4)
    def test6_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("111122111112220000",0,0), 4)
    def test7_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("411112211111222000404",4,0), 3)
    def test8_B(self):
        
        from cppyy.gbl import count_specific_number
        self.assertEqual(count_specific_number("55511155551221115551122200005",5,0), 11)
        
############ DO NOT CHANGE #####################
if __name__ == "__main__":
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
    with open(report_dir, 'wb') as report:
        report.write(transform(out.getvalue()))