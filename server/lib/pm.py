#!/usr/bin/python

import lib.ci as ci
from lib.database import *
import datetime
import os

project_statuses = ['Supplies Ordered','Supplies Arrived','Manufacturing Product','Product Manufactured','Installing Product','Product Installed','Completed']
complaint_statuses = ['Unresolved','Reviewed','Resolved']

def create_material(name, description):
	# ==== start of input validation & sanitization ====
	if not (name and description):
		return None

	name = "%s" % name
	description = "%s" % description
	# ==== end of input validation & sanitization ====

	material = Material(name=name, description=description)
	session.add(material)
	session.commit()
	return material

def create_project(project_title, project_description, company, poc_name, poc_contact, site_manager):
	# ==== start of input validation & sanitization ====
	if not (project_title and project_description and company and poc_name and poc_contact and site_manager):
		return None

	project_title = "%s" % project_title
	project_description = "%s" % project_description
	poc_name = "%s" % poc_name
	poc_contact = "%s" % poc_contact

	if not isinstance(company, Company):
		return None

	if not isinstance(site_manager, User):
		return None
	# ==== end of input validation & sanitization ====

	project = Project(project_title=project_title, project_description=project_description, poc_name=poc_name, poc_contact=poc_contact, company=company, site_manager=site_manager)
	session.add(project)
	session.commit()
	return project

def add_project_material_qty(project_id, material, qty):
	# ==== start of input validation & sanitization ====
	if not (project_id and material and qty):
		return None

	try:
		project_id = int(project_id)
		qty = int(qty)
	except:
		return None

	if not isinstance(material, Material):
		return None
	# ==== end of input validation & sanitization ====

	project_material = Project_Material(project_id=project_id, material=material, quantity=qty)
	session.add(project_material)
	session.commit()
	return project_material

def assign_project_workers(project_id, worker):
	# ==== start of input validation & sanitization ====
	if not (project_id and worker):
		return None

	try:
		project_id = int(project_id)
	except:
		return None

	if not isinstance(worker, Employee):
		return None
	# ==== end of input validation & sanitization ====

	project_worker = Project_Worker(project_id=project_id, worker=worker)
	session.add(project_worker)
	session.commit()
	return project_worker

def add_project_timeline(project_id, name, projected_start_date, projected_end_date):
	# ==== start of input validation & sanitization ====
	if not (project_id and name and projected_start_date and projected_end_date):
		return None

	try:
		project_id = int(project_id)
	except:
		return None

	name = "%s" % name
	if not isinstance(projected_start_date, datetime.date) or not isinstance(projected_end_date, datetime.date):
		return None
	# ==== end of input validation & sanitization ====

	timeline = Project_Timeline(project_id=project_id, name=name, projected_start_date=projected_start_date, projected_end_date=projected_end_date)
	session.add(timeline)
	session.commit()
	return timeline

def update_project_status(project_id, comments, status, date_added):
	# ==== start of input validation & sanitization ====
	if not (project_id and comments and status and date_added):
		return None

	try:
		project_id = int(project_id)
	except:
		return None

	comments = "%s" % comments
	status = "%s" % status
	if status not in project_statuses:
		return None

	if not isinstance(date_added, datetime.date):
		return None
	# ==== end of input validation & sanitization ====

	project_status = session.query(Project_Status).filter(Project_Status.project_id == project_id, Project_Status.status == status).first()
	if not project_status:
		project_status = Project_Status(project_id=project_id, comments=comments, status=status, date_added=date_added)
		session.add(project_status)
	else:
		project_status.comments = comments
		project_status.date_added = date_added
	session.commit()
	return project_status

def retrieve_site_manager_projects(site_manager_id):
	# ==== start of input validation & sanitization ====
	if not site_manager_id:
		return None

	try:
		site_manager_id = int(site_manager_id)
	except:
		return None

	if not ci.user_is_site_manager(site_manager_id):
		return None
	# ==== end of input validation & sanitization ====

	return session.query(Project).filter(Project.site_manager_id == site_manager_id).all()

def retrieve_project_by_id(project_id):
	# ==== start of input validation & sanitization ====
	if not project_id:
		return None

	try:
		project_id = int(project_id)
	except:
		return None
	# ==== end of input validation & sanitization ====

	return session.query(Project).filter(Project.project_id == project_id).first()

def add_project_status_photo(status_id, photo_file_path):
	# ==== start of input validation & sanitization ====
	if not (status_id and photo_file_path):
		return None

	try:
		status_id = int(status_id)
	except:
		return None

	if not os.path.exists(os.path.join(os.getcwd(), photo_file_path)):
		return None

	status = session.query(Project_Status).filter(Project_Status.status_id == status_id).first()
	if not status:
		return None
	# ==== end of input validation & sanitization ====

	status_photo = Project_Status_Photo(photo_file_path=photo_file_path, status_id=status_id)
	session.add(status_photo)
	session.commit()
	return status_photo
