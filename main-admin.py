import logging
import json
import uuid
import random
import time

from queries import Query
from scenarios import query_and_preserve, query_and_pay, query_and_consign
from datetime import datetime, timedelta, date
from locust import HttpUser, task, between, constant, events


class UserBooking(HttpUser):
    wait_time = between(2, 10)

    @task
    def admin_tasks(self):
        # login
        query = Query(ts_address=self.host)
        query.login(username="admin", password="222222")
        query.query_admin_travel()
        time.sleep(random.randint(1, 5))
        query.query_admin_basic_price()
        time.sleep(random.randint(1, 5))
        query.query_admin_basic_config()
