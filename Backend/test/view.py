from fastapi import FastAPI
from database.models import user, write
from main import read, return_account_operation
from pydantic import BaseModel


class User(BaseModel):
    data:str

users = return_account_operation("tz1bPmDANudr2SjSyg6MY5kBsdSMY3Xiirat")
a = user.insert().values(
    data=users
)
write(a)
us = read(user)
