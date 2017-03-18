#!/usr/bin/python

# imports
import flask
import json
import os
import lib.queries as queries
import lib.populate_db as populate_db
from flask_cors import CORS

# globals
server_ip = 'localhost'
server_port = 8080
app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)
images_dir = "images"

# functions
@app.errorhandler(404)
def page_not_found(e):
	return "Resource not found.", 404

@app.route("/images/<path:path>")
def send_images(path):
	return flask.send_from_directory(images_dir,path)

@app.route('/ws/login', methods=['POST'])
def user_login():
	username = flask.request.forms.get('username')
	password = flask.request.form.get('password')
	results = queries.user_login(username, password)
	return results if results else ""

@app.route('/ws/list_site_manager_projects')
def list_site_manager_projects():
	user_id = flask.request.args.get('site_manager_id')
	results = queries.list_site_manager_projects(user_id)
	return results if results else ""

@app.route('/ws/retrieve_project_details')
def retrieve_project_details():
	project_id = flask.request.args.get('project_id')
	results = queries.retrieve_project_details(project_id)
	return results if results else ""

@app.route('/ws/retrieve_project_statuses')
def retrieve_project_statuses():
	project_id = flask.request.args.get('project_id')
	results = queries.retrieve_project_statuses(project_id)
	return results if results else ""

@app.route('/ws/retrieve_project_complaints')
def retrieve_project_complaints():
	project_id = flask.request.args.get('project_id')
	results = queries.retrieve_project_complaints(project_id)
	return results if results else ""

@app.route('/ws/retrieve_project_workers')
def retrieve_project_workers():
	project_id = flask.request.args.get('project_id')
	results = queries.retrieve_project_workers(project_id)
	return results if results else ""

@app.route('/ws/update_worker_work_hours')
def update_worker_work_hours():
	employee_id = flask.request.args.get('employee_id')
	date = flask.request.args.get('date')
	start_time = flask.request.args.get('start_time')
	end_time = flask.request.args.get('end_time')
	results = update_worker_work_hours(employee_id, date, start_time, end_time)
	return "OK" if results else ""

if __name__ == "__main__":
	populate_db.populate_db()
	app.run(host=server_ip, port=server_port)
