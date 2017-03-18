#!/usr/bin/python

import lib.hr as hr
import lib.crm as crm
import lib.pm as pm
import lib.ci as ci

import json
import datetime

job_titles = ['Project Manager','Site Manager','Worker']
timeline_names = ['Supply Shipment','Product Manufacture','Installation']
project_statuses = ['Supplies Ordered','Supplies Arrived','Manufacturing Product','Product Manufactured','Installing Product','Product Installed','Completed']
complaint_statuses = ['Unresolved','Reviewed','Resolved']

def login(username, password):
	# Retrieve user details
	retrieved_user = ci.user_login(username, password)

	# Ensure user exists
	if not retrieved_user:
		return None

	# Specify return fields
	retrieved_user = json.loads("%s" % retrieved_user)
	user = {}
	user['user_id'] = retrieved_user.user_id
	user['name'] = retrieved_user.name
	user['photo'] = retrieved_user.employee.photo
	user['job_title'] = retrieved_user.employee.job_title
	return json.dumps(user)

def list_site_manager_projects(user_id):
	# Retrieve site manager projects
	retrieved_projects = pm.retrieve_site_manager_projects(user_id)

	# Return nothing if no projects
	if not retrieved_projects:
	    return None

	# Specify return fields
	retrieved_projects = json.loads("%s" % retrieved_projects)
	projects = []
	for retrieved_project in retrieved_projects:

	    installation_start_date, installation_end_date = get_timeline_dates(retrieved_project.get('timelines'), 'installation')
	    if not (installation_start_date and installation_end_date):
	        continue

	    latest_status, latest_status_date = get_latest_status(retrieved_project.get('statuses'))
	    if not (latest_status and latest_status_date):
	        continue

	    project = {}
	    project['project_id'] = retrieved_project.get('project_id')
	    project['project_title'] = retrieved_project.get('project_title')
	    project['company_name'] = retrieved_project.get('company').get('name')
	    project['installation_start_date'] = installation_start_date
	    project['installation_end_date'] = installation_end_date
	    project['status'] = latest_status
	    projects.append(project)

	return json.dumps(projects)

def retrieve_project_details(project_id):
	# Retrieve project
	retrieved_project = pm.retrieve_project_by_id(project_id)

	# Return nothing if project does not exist
	if not retrieved_project:
		return None

	retrieved_project = json.loads("%s" % retrieved_project)
	project_materials = []
	for retrieved_material in retrieved_project.get('materials_qty'):
		material = {
			'material': retrieved_material.get('material_name'),
			'qty': retrieved_material.get('quantity')
			}
		project_materials.append(material)

	project_timelines = []
	for retrieved_timeline in retrieved_project.get('timelines'):
		timeline_name = retrieved_timeline.get('name')
		start_date, end_date = get_timeline_dates(retrieved_project.get('timelines'), timeline_name)
		timeline = {
			'timeline': timeline_name,
			'start_date': start_date,
			'end_date': end_date
		}

		project_timelines.append(timeline)

	project = {}
	project['project_id'] = retrieved_project.get('project_id')
	project['project_title'] = retrieved_project.get('project_title')
	project['project_description'] = retrieved_project.get('project_description')
	project['company_name'] = retrieved_project.get('company').get('name')
	project['poc_name'] = retrieved_project.get('poc_name')
	project['poc_contact'] = retrieved_project.get('poc_contact')
	project['project_materials'] = project_materials
	project['project_timelines'] = project_timelines
	return json.dumps(project)

def retrieve_project_statuses(project_id):
	# Retrieve project
	retrieved_project = pm.retrieve_project_by_id(project_id)

	# Return nothing if project does not exist
	if not retrieved_project:
		return None

	retrieved_project = json.loads("%s" % retrieved_project)
	project_statuses = {}
	latest_status, latest_status_date = get_latest_status(retrieved_project.get('statuses'))
	current_status = {
		'status': latest_status,
		'date_added': latest_status_date
	}

	past_statuses = []
	for retrieved_status in retrieved_project.get('statuses'):
		if retrieved_status.get('status') != latest_status:
			status = {
				'status': retrieved_status.get('status'),
				'date_added': retrieved_status.get('date_added'),
				'comments': retrieved_status.get('comments')
			}
			past_statuses.append(status)
		else:
			current_status['comments'] = retrieved_status.get('comments')


	project_statuses['current_status'] = current_status
	project_statuses['past_statuses'] = past_statuses
	return json.dumps(project_statuses)

def retrieve_project_complaints(project_id):
	# Retrieve project
	retrieved_project = pm.retrieve_project_by_id(project_id)

	# Return nothing if project does not exist
	if not retrieved_project:
		return None

	retrieved_project = json.loads("%s" % retrieved_project)
	unresolved = []
	reviewed = []
	resolved = []

	for retrieved_complaint in retrieved_project.get('complaints'):
		complaint = {
			'complaint_id': retrieved_complaint.get('complaint_id'),
			'complaint': retrieved_complaint.get('complaint'),
			'date_added': retrieved_complaint.get('date_added')
		}

		resolution_status = retrieved_complaint.get('resolution_status')
		if resolution_status != complaint_statuses[0]:
			complaint['review'] = retrieved_complaint.get('review')
			complaint['date_reviewed'] = retrieved_complaint.get('date_reviewed')

		if resolution_status == complaint_statuses[2]:
			complaint['date_resolved'] = retrieved_complaint.get('date_resolved')
			resolved.append(complaint)
		elif resolution_status == complaint_statuses[1]:
			reviewed.append(complaint)
		else:
			unresolved.append(complaint)

	complaints = {}
	complaints['unresolved'] = unresolved
	complaints['reviewed'] = reviewed
	complaints['resolved'] = resolved

	return json.dumps(complaints)

def retrieve_project_workers(project_id):
	# Retrieve project
	retrieved_project = pm.retrieve_project_by_id(project_id)

	# Return nothing if project does not exist
	if not retrieved_project:
		return None

	retrieved_project = json.loads("%s" % retrieved_project)
	workers = []

	for retrieved_worker in retrieved_project.get('workers'):
		worker = {}
		worker['employee_id'] = retrieved_worker.get('employee_id')
		worker['name'] = retrieved_worker.get('name')
		worker['photo'] = retrieved_worker.get('photo')
		worker['contact'] = retrieved_worker.get('contact')
		worker['emergency_contact_name'] = retrieved_worker.get('emergency_contact_name')
		worker['emergency_contact_contact'] = retrieved_worker.get('emergency_contact_contact')

		workers.append(worker)
	return json.dumps(workers)

def submit_project_update(project_id, comments, photo_locations):
	if not (project_id and comments):
		return False
	return False

def submit_project_complaint_review(complaint_id, review):
	if not (complaint_id and review):
		return False
	return False

def update_worker_work_hours(employee_id, date, start_time, end_time):
	return hr.update_worker_work_hours(employee_id, date, start_time, end_time)

#===============================================================================
def get_timeline_dates(timelines, timeline_name):
	# Identify installation timeline
	extracted_timeline = None
	for timeline in timelines:
		if (timeline.get('name')).lower() == timeline_name.lower():
			extracted_timeline = timeline
			break

	# Ensure installation timeline exists
	if not extracted_timeline:
		return None, None

	# If installation has started, use actual start date, otherwise use projected start date
	start_date = extracted_timeline.get('actual_start_date') if extracted_timeline.get('actual_start_date') else extracted_timeline.get('projected_start_date')

	# If installation has ended, use actual end date, otherwise use projected end date
	end_date = extracted_timeline.get('actual_end_date') if extracted_timeline.get('actual_end_date') else extracted_timeline.get('projected_end_date')
	return start_date, end_date

def get_latest_status(project_statuses):
	# Retrieve the latest status of project
	date_format = '%Y-%m-%d'
	statuses = {}
	for status in project_statuses:
		statuses[status.get('date_added')] = status.get('status')
	statuses_dates = statuses.keys()

	# Ensure the project has a status
	if len(statuses_dates) <= 0:
		return None, None

	# Assign first status as latest status
	latest_status_date = statuses_dates[0]

	# If any status appears later, use it as latest status
	for i in range(1, len(statuses_dates)):
		if datetime.datetime.strptime(statuses_dates[i], date_format) > datetime.datetime.strptime(latest_status_date, date_format):
			latest_status_date = statuses_dates[i]

	latest_status = statuses.get(latest_status_date)
	return latest_status, latest_status_date
