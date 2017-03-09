#!/usr/bin/python

# imports
import flask
import json
import os
import lib.queries as queries
from flask_cors import CORS, cross_origin

# globals
server_ip = 'localhost'
server_port = 8080
app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)
images_dir = "images"
pages_dir = "pages"
js_dir = "js"

# functions
@app.route("/")
def index():
	content = "<a href='/ws/login'>Login</a><br/>"
	content += "<a href='/ws/list_users'>List Users</a><br/>"
	content += "<a href='/ws/list_employees'>List Employees</a><br/>"
	content += "<a href='/ws/list_companies'>List Companies</a><br/>"
	content += "<a href='/ws/list_projects'>List Projects</a><br/>"
	content += "<a href='/ws/list_site_manager_projects?site_manager_id=2'>List Site Manager Projects</a><br/>"
	content += "<a href='/ws/list_workers_without_project?start_date=2017-03-10&end_date=2017-03-20'>List Workers Without Project</a><br/>"
	return content

@app.route("/favicon.ico")
def send_favicon():
	return flask.send_from_directory(images_dir,'favicon.ico')

@app.route("/images/<path:path>")
def send_images(path):
	return flask.send_from_directory(images_dir,path)

@app.route("/js/<path:path>")
def send_js(path):
	return flask.send_from_directory(js_dir,path)

@app.route("/<path:path>")
def send_pages(path):
	return flask.send_from_directory(pages_dir,path)

def is_logged_in():
	return True if flask.session.get('user') else False

@app.route("/ws/login", methods=['GET','POST'])
def user_login():
	if is_logged_in():
		return flask.redirect(flask.url_for('list_users'))

	if flask.request.method == 'POST':
		username = flask.request.form.get('username')
		password = flask.request.form.get('password')

		if username and password:
			user = queries.user_login(username=username, password=password)
			if user:
				flask.session['user'] = json.loads("%s" % user)
				return flask.redirect(flask.url_for('list_users'))

		message = "Invalid username or password "
		message += "<a href='login'><input type='button' value='OK'/></a>"
		return message
	return flask.send_from_directory("pages", 'login.html')

@app.route("/ws/logout")
def user_logout():
	flask.session.pop('user', None)
	return flask.redirect(flask.url_for('index'))

@app.route("/ws/list_users")
def list_users():
	users = queries.list_users()
	return "%s" % users
	#return "<br/>".join(["%s" % user for user in users])

@app.route("/ws/list_employees")
def list_employees():
	employees = queries.list_employees()
	return "%s" % employees
	#return "<br/>".join(["%s" % employee for employee in employees])

@app.route("/ws/list_companies")
def list_companies():
	companies = queries.list_companies()
	return "%s" % companies
	#return "<br/>".join(["%s" % company for company in companies]) if len(companies) > 0 else "None"

@app.route("/ws/list_projects")
def list_projects():
	projects = queries.list_projects()
	return "%s" % projects
	#return print_projects(projects) if len(projects) > 0 else "None"

@app.route("/ws/list_site_manager_projects")
def list_site_manager_projects():
	user_id = flask.request.args.get('site_manager_id')
	if user_id:
		projects = queries.list_site_manager_projects(int(user_id))
		return "%s" % projects
		#return print_projects(projects) if len(projects) > 0 else "None"
	return "Param(s) needed: user_id"

@app.route("/ws/list_workers_without_project")
def list_workers_without_project():
	start_date = flask.request.args.get('start_date')
	end_date = flask.request.args.get('end_date')
	if start_date and end_date:
		workers = queries.list_workers_without_project("%s" % start_date, "%s" % end_date)
		return "%s" % workers
	return "Params(s) needed: start_date, end_date"

@app.route("/ws/add_project_complaint")
def add_project_complaint():
	project_id = flask.request.args.get('project_id')
	complaint = flask.request.args.get('complaint')
	if project_id and complaint:
		complaint = queries.add_project_complaint(project_id, complaint)
		return "Complaint has been added." if complaint else "Project does not exist."
	return "Param(s) needed: project_id, complaint"

@app.route("/ws/review_project_complaint")
def review_project_complaint():
	complaint_id = flask.request.args.get('complaint_id')
	action_taken = flask.request.args.get('action_taken')
	if complaint_id and action_taken:
		update = queries.review_project_complaint(complaint_id, action_taken)
		return "Complaint has been reviewed." if update else "Project does not exist."
	return "Param(s) needed: complaint_id, action_taken"

@app.route("/ws/list_complaint_resolution_recommendations")
def list_complaint_resolution_recommendations():
	project_id = flask.request.args.get('project_id')
	if project_id:
		recommendations = queries.list_complaint_resolution_recommendations(project_id)
		if recommendations:
			return recommendations if len(recommendations) > 0 else "None"
		else:
			return "Project does not exist."
	return "Param(s) needed: project_id"

if __name__ == "__main__":
	queries.populate_db()
	app.run(host=server_ip, port=server_port)
