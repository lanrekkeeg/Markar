from locust import HttpLocust, TaskSet, task
import json
 
data = {"email":"p156058@nu.edu.pk","type":"Assignment","number":1, "token": "3dab49a1-aaa8-442c-b753-a9a293042c6c", "section":"A","coursecode":'cl-201'}
files = {
     'data': (None,json.dumps(data), 'application/json'),
     'Task-File': open('task.cpp','rb')
    }
class UserBehavior(TaskSet):
 
    @task(1)    
    def create_post(self):
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        self.client.post("/Submit",files=files)
        name = "Create a new post")
 
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior