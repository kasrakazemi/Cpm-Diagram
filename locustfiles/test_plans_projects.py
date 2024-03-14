################# Libs #################
from locust import HttpUser, task, between
from random import randint
#######################################

class WebUser(HttpUser):
    wait_time = between(1,6)

    @task(5)
    def view_projects(self):
        
        pk = randint(4,10)
        self.client.get(
            f'/projects/projects/{pk}',
              name = '/projects/projects')
        
    @task(4)
    def view_plans(self):
       
        pk = randint(4,10)
        self.client.get(
            f'/projects/plans/{pk}',
              name = '/projects/plans')
        
    @task(6)
    def view_generalinfo(self):
        
        self.client.get(
            f'/core/generalinfo/3',
              name = '/core/generalinfo')
        
    @task(20)
    def test_performance(self):
        self.client.get(f'/core/test_get/', name = '/core/test_get')

