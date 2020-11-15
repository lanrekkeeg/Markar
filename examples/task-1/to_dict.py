import xml.etree.ElementTree as ET

from copy import copy

def dictify(r,root=True):
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

file_ = open("report2.xml",'r').read().strip()
root = ET.fromstring(file_)
        #print(file_)
out = dictify(root)
REPORT = str()
ls = out['testsuites']['testsuite'][0]
i = 1
print(ls)
print("________________________________")
for ds in ls['testcase']:
    print(ds['name'])
    if ds.get("failure",None) is not None:
        
        REPORT += "Test-Case-{0}, outcome:{1}, AssertError:{2}\n"\
            .format(str(i), "Fail", ds['failure'][0]['_text'])
        #REPORT.update({"TEST-"+str(i):ds['name'], "outcome":"Fail", "AssertError":ds['failure'][0]['_text']})
    else:
        REPORT += "Test-Case-{0}, outcome:{1}\n"\
            .format(str(i), "Pass")
    i += 1
 #if ds.get("failure",None) is not None:
 #       REPORT.update({"TEST-"+str(i):ds['name'], "outcome":"Fail", "AssertError":ds['failure'][0]['_text']})
 #   else:
 #       REPORT.update({"TEST-"+str(i):ds['name'], "outcome":"Pass"})
 #   i += 1
#print(REPORT)