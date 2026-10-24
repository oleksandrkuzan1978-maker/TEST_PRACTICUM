import requests

class EmployeeApi:
    def __init__(self, base_url=  'http://5.101.50.27:8000/employee/'):
        self.base_url = base_url
