#!/usr/bin/python

from lib.database import *
roles = ['Project Manager','Site Manager','Worker']

def create_user(username, password, role, employee):
	# ==== start of input validation & sanitization ====
	if not (username and password and role and employee):
		return None

	username = ("%s" % username).lower()
	password = "%s" % password
	role = "%s" % role
	if role not in roles:
		return None

	if not isinstance(employee, Employee):
		return None
	# ==== end of input validation & sanitization ====

	user = User(username=username, password=password, role=role, employee=employee)
	session.add(user)
	session.commit()
	return user

def user_login(username, password):
	# ==== start of input validation & sanitization ====
	if not (username and password):
		return None

	username = ("%s" % username).lower()
	password = "%s" % password
	# ==== end of input validation & sanitization ====

	return session.query(User).filter(User.username == username, User.password == password).first()

def retrieve_user_by_id(user_id):
	# ==== start of input validation & sanitization ====
	if not user_id:
		return None

	try:
		user_id = int(user_id)
	except:
		return None
	# ==== end of input validation & sanitization ====

	return session.query(User).filter(User.user_id == user_id).first()

def user_is_site_manager(user_id):
	# ==== start of input validation & sanitization ====
	if not user_id:
		return None

	try:
		user_id = int(user_id)
	except:
		return None
	# ==== end of input validation & sanitization ====

	# Ensure that user exists
	user = retrieve_user_by_id(user_id)
	if not user:
		return False

	# Ensure that user is a site manager
	if user and user.role != roles[1]:
		return False

	return True
