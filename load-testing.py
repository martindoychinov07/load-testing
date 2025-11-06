from locust import HttpUser, task, between

class GoogleUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home(self):
        # main page
        self.client.get("/")

    @task
    def search_q(self):
        # simple search request
        self.client.get("/search?q=python")

    @task
    def images(self):
        # google images page
        self.client.get("/imghp")
