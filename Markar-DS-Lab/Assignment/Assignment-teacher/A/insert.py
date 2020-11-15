
import cppyy
code = open("task.cpp",'r').read().strip()
cppyy.cppdef(code)
from cppyy.gbl import BST
bst = BST()
def insert(node_list):
    for i in node_list:
        bst.Insertion(bst.Get_Root(), i)
    return bst

insert([1,2,3,4,5])
bst.print(bst.Get_Root())