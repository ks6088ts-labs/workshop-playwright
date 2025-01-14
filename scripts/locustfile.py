from os import getenv

from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post(
            url="/flaky",
            json={
                "percent": int(getenv("FLAKY_PERCENT", 30)),
            },
        )
