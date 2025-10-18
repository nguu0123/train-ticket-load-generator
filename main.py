import logging
import json
import uuid
import random
import time

from queries import Query
from scenarios import query_and_preserve, query_and_pay, query_and_consign
from datetime import datetime, timedelta, date
from locust import HttpUser, task, between, constant, events

random.seed(0)


class UserBooking(HttpUser):
    wait_time = between(2, 10)

    @task
    def query_and_preserve(self):
        print("Perform user tasks")
        # login
        query = Query(self.host, self.client)
        query.login()

        query.query_normal_ticket()
        time.sleep(random.randint(1, 5))

        # 1 out of 10 clients will perform query and preserve, and sleep 1-5 second
        if random.randint(0, 10) == 0:
            query_and_preserve(query)
            time.sleep(random.randint(1, 5))

        if random.randint(0, 10) == 0:
            query_and_pay(query)
            time.sleep(random.randint(1, 5))

        if random.randint(0, 10) == 0:
            query_and_consign(query)
            time.sleep(random.randint(1, 5))

        # 1 out of 3 clients will perform query and preserve
        if random.randint(0, 3) == 0:
            query.query_high_speed_ticket()
            time.sleep(random.randint(1, 5))

        if random.randint(0, 3) == 0:
            query.query_food()
            time.sleep(random.randint(1, 5))

    @task
    def admin_tasks(self):
        print("Perform admin tasks")
        # login
        query = Query(self.host, self.client)
        query.login(username="admin", password="222222")
        query.query_admin_travel()
        time.sleep(random.randint(1, 5))
        query.query_admin_basic_price()
        time.sleep(random.randint(1, 5))
        query.query_admin_basic_config()
