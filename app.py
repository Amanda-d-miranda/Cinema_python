import os
from dotenv import load_dotenv
from flask import Flask
from db import db
load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://postgres:postgres@localhost:5432/books"
)


