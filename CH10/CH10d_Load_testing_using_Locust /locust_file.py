from locust import HttpUser, task
from random import choice
from string import ascii_uppercase

class User(HttpUser):
    @task
    def predict(self):
        payload = {"text": ''.join(choice(ascii_uppercase) for i in range(20))}
        self.client.post("/sentiment", json=payload)
