#!/usr/bin/python

from lib.database import *

def list_users():
    return session.query(User).all()

def get_user_by_id(user_id):
    return session.query(User).filter(User.user_id=="%d" % int(user_id)).first()

def user_login(username, password):
    return session.query(User).filter(User.username==("%s" % username).lower(), User.password=="%s" % password).first()

def add_user(name, username, password, role):
    user = User(name="%s" % name, username="%s" % username.lower(), password="%s" % password, role="%s" % role)
    session.add(user)
    session.commit()
    return user
