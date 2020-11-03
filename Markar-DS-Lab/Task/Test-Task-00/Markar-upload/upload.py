import requests
import json

def post():
    """
    Uploading Task to Markar
    """
    section="B"
    type_="Task"
    number=0
    authorization='f8685c3d-a960-4488-86ed-ec7ec07e1d44'
    coursecode="cl-201"
    marks=10
    deadline='2020-11-4 23:59:00'
    headers = {'authorization':authorization}
    data= {"email":"p156058@nu.edu.pk","type": type_,"number":number,"coursecode":coursecode, "section": section,"marks":marks, "deadline":deadline}
    files = {
     'data': (None,json.dumps(data), 'application/json'),
     'upload_file': open('./task-server-test.py','rb')
    }
    out = requests.post('http://markar.faisalwork.net/AddTaskAssign', files=files, headers=headers)
    print(out.json())

if __name__ == "__main__":
    post()
