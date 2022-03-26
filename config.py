import os


class Config:
    SECRET_KEY = 'Hjf2Gh98Jjhfi5786Hjfy7LK'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.sqlite' # путь к базе данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False