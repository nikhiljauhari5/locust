import time

from locust import User, task, constant, between, constant_pacing


class MyUser(User):
    # wait_time = constant(1)
    # wait_time = between(2, 5)
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        # print("This will inject 2-5 seconds delay")
        time.sleep(2)
        print("Constant Pacing Demo")
