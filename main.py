import logging
import json
import uuid

from queries import Query
from scenarios import query_and_preserve
from datetime import datetime, timedelta, date
from locust import HttpUser, task, between, constant, events



class UserBooking(HttpUser):
    wait_time = between(1, 2)

    @task
    def admin_tasks(self):
        # login
        query = Query(ts_address="http://localhost:8080")
        query.login(username="admin", password="222222")
        query.query_admin_travel()
        query.query_admin_basic_price() 
        query.query_admin_basic_config()

    @task
    def query_and_preserve(self):
        # login
        query = Query(ts_address="http://localhost:8080")
        query.login()
        query_and_preserve(query)
        query.query_high_speed_ticket()

        

