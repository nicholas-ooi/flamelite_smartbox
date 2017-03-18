#!/usr/bin/python

from lib.database import *
import datetime
import os
complaint_statuses = ['Unresolved','Reviewed','Resolved']

def create_company(name, address, postal_code):
	# ==== start of input validation & sanitization ====
	if not (name and address and postal_code):
		return None

	name = "%s" % name
	address = "%s" % address
	postal_code = "%s" % postal_code
	# ==== end of input validation & sanitization ====

	company = Company(name=name, address=address, postal_code=postal_code)
	session.add(company)
	session.commit()
	return company

def add_project_complaint(project_id, complaint):
	# ==== start of input validation & sanitization ====
	if not (project_id and complaint):
		return None

	try:
		project_id = int(project_id)
	except:
		return None

	complaint = "%s" % complaint

	# ==== end of input validation & sanitization ====
	project_complaint = Project_Complaint(project_id=project_id, complaint=complaint, date_added=datetime.datetime.now().date(), resolution_status=complaint_statuses[0])
	session.add(project_complaint)
	session.commit()
	return project_complaint

def retrieve_project_complaint_by_id(complaint_id):
	# ==== start of input validation & sanitization ====
	if not complaint_id:
		return None

	try:
		complaint_id = int(complaint_id)
	except:
		return None
	# ==== end of input validation & sanitization ====

	return session.query(Project_Complaint).filter(Project_Complaint.complaint_id == complaint_id).first()


def review_project_complaint(complaint_id, review):
	# ==== start of input validation & sanitization ====
	if not (complaint_id and review):
		return None

	complaint = retrieve_project_complaint_by_id(complaint_id)
	if not complaint:
		return None

	review = "%s" % review
	# ==== end of input validation & sanitization ====

	print "error here?"
	if complaint.resolution_status == complaint_statuses[0]:
		complaint.review = review
		complaint.resolution_status = complaint_statuses[1]
		complaint.date_reviewed = datetime.datetime.now().date()
		session.commit()
		return True
	return False

def add_review_photo(complaint_id, photo_file_path):
	# ==== start of input validation & sanitization ====
	if not (complaint_id and photo_file_path):
		return None

	try:
		complaint_id = int(complaint_id)
	except:
		return None

	if not os.path.exists(os.path.join(os.getcwd(), photo_file_path)):
		return None

	complaint = retrieve_project_complaint_by_id(complaint_id)
	if not complaint:
		return None
	# ==== end of input validation & sanitization ====

	review_photo = Review_Photo(photo_file_path=photo_file_path, complaint_id=complaint_id)
	session.add(review_photo)
	session.commit()
	return review_photo

def resolve_project_complaint(complaint_id):
	# ==== start of input validation & sanitization ====
	if not complaint_id:
		return None

	complaint = retrieve_project_complaint_by_id(complaint_id)
	if not complaint:
		return None
	# ==== end of input validation & sanitization ====

	if complaint_statuses.resolution_status == complaint_statuses[1]:
		complaint.resolution_status = complaint_statuses[2]
		complaint.date_resolved = datetime.datetime.now().date()
		session.commit()
		return True
	return False
