# Barry Yang and Lily Xu
# CS 61 Databases
# Lab 3 part b
# May 25, 2017
import pymongo
from pymongo import MongoClient


class Database:
    def __init__(self, HOST):
        # initialize db connection
        connection = pymongo.MongoClient(HOST)
        connection.server_info()

        self.client = connection.Team28DB

        # self.client = client[team_name]

        self.logged_in = False          # boolean: whether anyone is logged in
        self.user_id   = -1             # int: current user id
        self.user_type = ""             # string: author, editor, or reviewer

    def get_client(self):
        return self.client

    def is_logged_in(self):
        return self.logged_in

    def get_user_id(self):
        return self.user_id

    def get_user_type(self):
        return self.user_type

    def change_user_id(self, user_id):
        self.user_id = int(user_id)

    def change_user_type(self, user_type):
        self.user_type = user_type

    def log_on(self):
        self.logged_in = True

    def log_off(self):
        self.logged_in = False
        self.user_id = -1
        self.user_type = ""
