#!/usr/bin/python

# imports
import flask
import json
import os
import lib.queries as queries
import lib.populate_db as populate_db
import hashlib
from PIL import Image
from flask_cors import CORS
from werkzeug.utils import secure_filename

# globals
server_ip = 'localhost'
server_port = 8080
app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)
images_dir = "images"
image_upload_dir = os.path.join(os.getcwd(), images_dir)

# functions
@app.errorhandler(404)
def page_not_found(e):
	return "Resource not found.", 404

@app.route("/images/<path:path>")
def send_images(path):
	return flask.send_from_directory(images_dir,path)

@app.route('/ws/login', methods=['POST'])
def user_login():
	username = flask.request.json.get('username')
	password = flask.request.json.get('password')
	results = queries.login(username, password)
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
	results = queries.update_worker_work_hours(employee_id, date, start_time, end_time)
	return "OK" if results else ""

@app.route('/ws/submit_project_installed_update')
def submit_project_installed_update():
	project_id = flask.request.args.get('project_id')
	comments = flask.request.args.get('comments')
	print "%s %s" % (project_id, comments)
	results = queries.submit_project_installed_update(project_id, comments)
	return results if results else ""

@app.route('/ws/add_status_photo', methods=['POST'])
def add_status_photo():
	status_id = flask.request.form.get('status_id')
	photo_file_path = upload_file()
	results = queries.add_status_photo(status_id, photo_file_path)
	return "OK" if results else ""

@app.route('/ws/submit_project_complaint_review')
def submit_project_complaint_review():
	complaint_id = flask.request.args.get('complaint_id')
	review = flask.request.args.get('review')
	results = queries.submit_project_complaint_review(complaint_id, review)
	return "OK" if results else ""

@app.route('/ws/add_review_photo', methods=['POST'])
def add_review_photo():
	complaint_id = flask.request.form.get('complaint_id')
	photo_file_path = upload_file()
	results = queries.add_review_photo(complaint_id, photo_file_path)
	return "OK" if results else ""

@app.route('/ws/upload_file', methods=['POST'])
def upload_file():
	if flask.request.method == 'POST':
		# check if the post request has the file part
		if 'file' in flask.request.files:
			f = flask.request.files['file']
			temp_file_path = "%s" % os.path.join(image_upload_dir, secure_filename(f.filename))
			f.save(temp_file_path)

			try:
				im = Image.open(temp_file_path)
				file_type = ("%s" % im.format).lower()
				file_hash = ("%s" % hashlib.sha1(file(temp_file_path).read()).hexdigest()).upper()
				file_name = "%s.%s" % (file_hash,file_type)
				real_file_path = "%s" % os.path.join(image_upload_dir, file_name)
				os.rename(temp_file_path, real_file_path)
				return os.path.join(images_dir, file_name)
			except:
				os.remove(temp_file_path)
				return None
	return None

@app.route('/test/login')
def test_login():
	content = "<form action='/ws/login' method='POST'>"
	content += "Username: <input type='text' name='username'><br/>"
	content += "Password: <input type='password' name='password'><br/>"
	content += "<input type='submit' value='Login'>"
	content += "</form>"
	return content

@app.route('/test/submit_project_installed_update')
def test_submit_project_installed_update():
	content = "<form action='/ws/submit_project_installed_update''>"
	content += "Project ID: <input type='text' name='project_id'><br/>"
	content += "Comments: <input type='text' name='comments'><br/>"
	content += "<input type='submit' value='Submit'>"
	content += "</form>"
	return content

@app.route('/test/add_status_photo')
def test_add_status_photo():
	content = "<form action='/ws/add_status_photo' method='POST' enctype='multipart/form-data'>"
	content += "Status ID: <input type='text' name='status_id'><br/>"
	content += "<input type='file' name='file'><br/>"
	content += "<input type='submit' value='Upload'>"
	content += "</form>"
	return content

@app.route('/test/submit_project_complaint_review')
def test_submit_project_complaint_review():
	content = "<form action='/ws/submit_project_complaint_review'>"
	content += "Complaint ID: <input type='text' name='complaint_id'><br/>"
	content += "Review: <input type='text' name='review'><br/>"
	content += "<input type='submit' value='Submit'>"
	content += "</form>"
	return content


@app.route('/test/add_review_photo')
def test_add_review_photo():
	content = "<form action='/ws/add_review_photo' method='POST' enctype='multipart/form-data'>"
	content += "Complaint ID: <input type='text' name='complaint_id'><br/>"
	content += "<input type='file' name='file'><br/>"
	content += "<input type='submit' value='Upload'>"
	content += "</form>"
	return content


if __name__ == "__main__":
	populate_db.populate_db()
	app.run(host=server_ip, port=server_port)
