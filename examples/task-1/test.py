import pytest
import os
import cppyy
code = open("compute_sum.cpp",'r').read().strip()
cppyy.cppdef(code)
from cppyy.gbl import compute_sum
from pytest_jsonreport.plugin import JSONReport

def test_func1():
    out = compute_sum(1,3) 
    assert out == 6

def d_test_func2():
    assert compute_sum(1,3) == 6  

def d_test_func3():
    assert compute_sum(1,3) == 6

if __name__ == '__main__':
    #test_func1()
    plugin = JSONReport()
    pytest.main(['--json-report-file=none', 'test.py'], plugins=[plugin])
    print(len(plugin.report['tests']))
    for i in plugin.report['tests']:
        print(i['nodeid'])
    #print(type(cppyy.gbl.compute_sum(1,3)))