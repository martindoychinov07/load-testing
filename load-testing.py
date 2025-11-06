from locust import HttpUser, task, between

class ExampleUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home(self):
        self.client.get("/")     # https://example.org/
