from pyunitreport import HTMLTestRunner
import unittest
import os
import requests
import cppyy
import logging
from unittest.case import SkipTest
import cppyy.ll

logging.basicConfig(level=logging.DEBUG)

##### DO NOT CHANGE ########
code = open("assignment.cpp",'r').read().strip()
cppyy.cppdef(code)
from cppyy.gbl import BST

#############################
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
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),16)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),16),4)

    def test2_A(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),32)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),32),2)
        
    def test3_A(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),24)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),24),7)

    def test4_A(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),19)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),19),2)

    def test5_A(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),9)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),9),1)
    
    def test6_A(self):
        try:
            node_list =  [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),18)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),18),7)
    
    def test7_A(self):
        try:
            node_list =  [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),3)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),3),4)
    
    def test8_A(self):
        try:
            node_list =  [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),27)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),27),2)
        
    def test9_A(self):
        try:
            node_list =  [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),34)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),34),1)
        
        
    def test10_A(self):
        try:
            node_list =  [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            count_nodes = bst.count_nodes
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                count_nodes(bst.Get_Root(),14)
        except:
            self.fail()
        self.assertEqual(count_nodes(bst.Get_Root(),14),0)

    def test1_B(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),3)

    def test2_B(self):
        try:
            node_list = [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),3)

    def test3_B(self):
        try:
            node_list = [10]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),0)

    def test4_B(self):
        try:
            node_list = [10,8]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),1)

    def test5_B(self):
        try:
            node_list = [10,11]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),0)
    
    def test6_B(self):
        try:
            node_list =  [10,9,13,8,11]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),2)

    def test7_B(self):
        try:
            node_list =  [10,13,18,12]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),2)

    def test8_B(self):
        try:
            node_list =  [78,79,34,28,14,32,80]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),3)

    def test9_B(self):
        try:
            node_list = [4,2,6,1,3,5,7]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),2)

    def test10_B(self):
        try:
            node_list = [10,15,20]
            bst = self.insert(node_list)
            left_most_node = bst.left_most_node
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                left_most_node(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(left_most_node(bst.Get_Root()),0)
        
    def test1_C(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),0)

    def test2_C(self):
        try:
            node_list = [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),38)

    def test3_C(self):
        try:
            node_list = [10]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),0)

    def test4_C(self):
        try:
            node_list = [10,8]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),0)

    def test5_C(self):
        try:
            node_list = [10,11]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),11)
        
    def test6_C(self):
        try:
            node_list = [10,9,13,8,11]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),0)

    def test7_C(self):
        try:
            node_list = [10,13,18,12]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),18)

    def test8_C(self):
        try:
            node_list = [78,79,34,28,14,32,80]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),112)

    def test9_C(self):
        try:
            node_list = [4,2,6,1,3,5,7]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),10)

    def test10_C(self):
        try:
            node_list = [10,15,20]
            bst = self.insert(node_list)
            right_leaves = bst.right_leaves
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                right_leaves(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(right_leaves(bst.Get_Root()),20)
    
    def test1_D(self):
        try:
            node_list = [24,16,9,32,28,19,17]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),2)

    def test2_D(self):
        try:
            node_list = [18,3,2,1,4,27,34]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),1)
    def test3_D(self):
        try:
            node_list = [10]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),0)

    def test4_D(self):
        try:
            node_list = [10,8]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),2)

    def test5_D(self):
        try:
            node_list = [10,11]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),1)
    
    def test6_D(self):
        try:
            node_list = [10,9,13,8,11]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),1)

    def test7_D(self):
        try:
            node_list = [10,13,18,12]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),1)
        
    def test8_D(self):
        try:
            node_list = [78,79,34,28,14,32,80]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),1)

    def test9_D(self):
        try:
            node_list =  [4,2,6,1,3,5,7]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),1)

    def test10_D(self):
        try:
            node_list = [10,15,20]
            bst = self.insert(node_list)
            min_diff = bst.min_diff
        except:
            raise SkipTest
        try:
            with cppyy.ll.signals_as_exception():
                min_diff(bst.Get_Root())
        except:
            self.fail()
        self.assertEqual(min_diff(bst.Get_Root()),5)
    
       
    
    
        
if __name__ == '__main__':
    kwargs = {
    "output": "final_output",
    "report_name": "final",
    "failfast": True }
    unittest.main(testRunner=HTMLTestRunner(os.getcwd()+"/report/", "local"))