#!/usr/bin/python

from lib.database import *

def create_employee(name, job_title, photo, contact, emergency_contact_name, emergency_contact_contact, monthly_salary):
	# ==== start of input validation & sanitization ====
	if not (name and job_title and contact and emergency_contact_name and emergency_contact_contact and monthly_salary):
		return None

	name = "%s" % name
	job_title = "%s" % job_title
	photo = "%s" % photo
	contact = "%s" % contact
	emergency_contact_name = "%s" % emergency_contact_name
	emergency_contact_contact = "%s" % emergency_contact_contact
	try:
		monthly_salary = float(monthly_salary)
	except:
		return None
	# ==== end of input validation & sanitization ====

	employee = Employee(name=name, job_title=job_title, photo=photo, contact=contact, emergency_contact_name=emergency_contact_name, emergency_contact_contact=emergency_contact_contact, monthly_salary=monthly_salary)
	session.add(employee)
	session.commit()
	return employee

def update_worker_work_hours(employee_id, date_str, start_time, end_time):
	# ==== start of input validation & sanitization ====
	if not (employee_id and date_str and start_time and end_time):
		return False

	try:
		date = datetime.datetime.strptime("%s" % date_str,'%Y-%m-%d').date()
		start_time = datetime.datetime.strptime("%s" % start_time, "%H:%M")
		end_time = datetime.datetime.strptime("%s" % end_time, "%H:%M")
		employee_id = int(employee_id)
	except:
		return False

	if end_time < start_time:
		return None
	# ==== end of input validation & sanitization ====

	worker_work_hours = session.query(Worker_Work_Hours).filter(Worker_Work_Hours.worker_id == employee_id, Worker_Work_Hours.date==date).first()
	if not worker_work_hours:
		worker_work_hours = Worker_Work_Hours(worker_id=employee_id, date=date, start_time=start_time, end_time=end_time)
		session.add(worker_work_hours)
	else:
		worker_work_hours.start_time = start_time
		worker_work_hours.end_time = end_time
	session.commit()
	return True
