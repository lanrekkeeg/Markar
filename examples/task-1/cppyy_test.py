import cppyy
code = open("task-01.cpp",'r').read().strip()
cppyy.cppdef(code)

from cppyy.gbl import List
out = List()
out.add_link_node_to_tail(12)
out.add_link_node_to_tail(13)
#out.add_link_node_to_tail(14)
#out.add_link_node_to_tail(15)
#out.print()
#list_ = list()
list_ = out.get_head()
#for data in list_:
#    print(data)
print(out.check_null(list_))
list_ = list_.next
print(out.check_null(list_))
#print(cppyy.nullptr)
print(list_)
if list_ == cppyy.nullptr:
    print("null")
else:
    print("not null")

#head = out.get_head()
#data = dict(head)
#print(head.data)
#print(type(head.next))
#head = head.next
#print(head)
#assert out.sum(4,5) != 9
