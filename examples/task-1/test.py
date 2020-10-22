import cppyy
code = open("task-01.cpp",'r').read().strip()
cppyy.cppdef(code)

from cppyy.gbl import List
out = List()
#out.add_link_node_to_tail(12)
#out.add_node_to_tail(13)
#out.add_node_to_tail(14)
#out.add_node_to_tail(15)
#out.print()

#head = out.get_head()
#data = dict(head)
#print(head.data)
#print(type(head.next))
#head = head.next
#print(head)
assert out.sum(4,5) != 9
