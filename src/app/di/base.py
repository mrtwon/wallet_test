from fastapi import FastAPI
from .setup import di_setup


def di_all(app: FastAPI):
    di_setup(app)
