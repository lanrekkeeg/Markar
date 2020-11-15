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
    def insert(self, node_list):
        bst = BST()
        for i in node_list:
            bst.Insertion(bst.Get_Root(), i)
        return bst
    
    def test1_A(self):
        try:
            node_list = [20,15,25]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        self.assertEqual(count_nodes(bst.Get_Root(),20),3)

    def test2_A(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        self.assertEqual(count_nodes(bst.Get_Root(),6),4)
        
    def test3_A(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        self.assertEqual(count_nodes(bst.Get_Root(),45),4)

    def test4_A(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        self.assertEqual(count_nodes(bst.Get_Root(),29),6)

    def test5_A(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        self.assertEqual(count_nodes(bst.Get_Root(),10),11)

    def test1_B(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4,54]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        self.assertEqual(left_most_node(bst.Get_Root()),4)

    def test2_B(self):
        try:
            node_list = [10,6,29,5]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        self.assertEqual(left_most_node(bst.Get_Root()),2)

    def test3_B(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4,54,56]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        self.assertEqual(left_most_node(bst.Get_Root()),5)

    def test4_B(self):
        try:
            node_list = [10,6,29,5,28,27,26,25,24,23,22]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        self.assertEqual(left_most_node(bst.Get_Root()),8)

    def test5_B(self):
        try:
            node_list = [20,15]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        self.assertEqual(left_most_node(bst.Get_Root()),1)
        
    def test1_C(self):
        try:
            node_list = [10,4,1,8,9,12]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        self.assertEqual(right_leaves(bst.Get_Root()),21)

    def test2_C(self):
        try:
            node_list = [8,5,6,20,10,12]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        self.assertEqual(right_leaves(bst.Get_Root()),18)

    def test3_C(self):
        try:
            node_list = [20,18,19,15,16,55]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        self.assertEqual(right_leaves(bst.Get_Root()),90)

    def test4_C(self):
        try:
            node_list = [50,65,60,62,45,46]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        self.assertEqual(right_leaves(bst.Get_Root()),108)

    def test5_C(self):
        try:
            node_list = [10,4,1,8,9]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        self.assertEqual(right_leaves(bst.Get_Root()),9)
    
    def test1_D(self):
        try:
            node_list = [10,6,29,22,45,44,55,66,5,8,4,54]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        self.assertEqual(min_diff(bst.Get_Root()),1)

    def test2_D(self):
        try:
            node_list = [10,6,29,5]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        self.assertEqual(min_diff(bst.Get_Root()),1)
    def test3_D(self):
        try:
            node_list = [20,15,25,11,14]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        self.assertEqual(min_diff(bst.Get_Root()),3)

    def test4_D(self):
        try:
            node_list = [10,6,29,5,28,27,26,25,24,23,22]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        self.assertEqual(min_diff(bst.Get_Root()),1)

    def test5_D(self):
        try:
            node_list = [9,5]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        self.assertEqual(min_diff(bst.Get_Root()),4)
############ DO NOT CHANGE #####################
if __name__ == "__main__":
    unittest.main(
    testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
    with open(report_dir, 'wb') as report:
        report.write(transform(out.getvalue()))