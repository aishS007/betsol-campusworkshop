"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgprglorddl9mmojgvjg-a.singapore-postgres.render.com",
        database="aishtodo",
        user="aish",
        password="45XW55FDs8aJUdmjeq36P8QOw1q0sD4v")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
