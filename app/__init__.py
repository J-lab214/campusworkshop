"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi8n5l269vf5qbkl6mg-a.oregon-postgres.render.com",
        database="todo_afvl",
        user="todo_afvl_user",
        password="2bRiMEoB2Vo5uAorVjF1vdhcHeMKWPNO")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
