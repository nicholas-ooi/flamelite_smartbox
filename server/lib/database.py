#!/usr/bin/python

# imports
import json
import sqlalchemy as sql
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as ext_dec

engine = sql.create_engine("sqlite:///:memory:", convert_unicode=True)
session = orm.scoped_session(orm.sessionmaker(bind=engine))
Base = ext_dec.declarative_base()
date_format = '%Y-%m-%d'
time_format = '%H:%M'

# classes
class User(Base):
	__tablename__ = "users"
	user_id = sql.Column(sql.Integer, primary_key=True)
	username = sql.Column(sql.String)
	password = sql.Column(sql.String)
	role = sql.Column(sql.String)
	employee_id = sql.Column(sql.ForeignKey('employees.employee_id'))
	employee = orm.relationship('Employee')

	def __repr__(self):
		employee_data = json.loads("%s" % self.employee)
		data = {
			'user_id': self.user_id,
			'name': employee_data.get('name'),
			'username': self.username,
			'role': self.role,
			'employee_id': employee_data.get('employee_id'),
			'job_title': employee_data.get('job_title'),
			'photo': employee_data.get('photo')
		}
		return json.dumps(data)

class Employee(Base):
	__tablename__ = "employees"
	employee_id = sql.Column(sql.Integer, primary_key=True)
	name = sql.Column(sql.String)
	photo = sql.Column(sql.String)
	contact = sql.Column(sql.String)
	emergency_contact_name = sql.Column(sql.String)
	emergency_contact_contact = sql.Column(sql.String)
	job_title = sql.Column(sql.String)
	monthly_salary = sql.Column(sql.Integer)

	def __repr__(self):
		data = {
			'employee_id': self.employee_id,
			'name': self.name,
			'photo': self.photo,
			'contact': self.contact,
			'emergency_contact_name': self.emergency_contact_name,
			'emergency_contact_contact': self.emergency_contact_contact,
			'job_title': self.job_title,
			'monthly_salary': self.monthly_salary
		}
		return json.dumps(data)

class Worker_Work_Hours(Base):
	__tablename__ = "worker_work_hours"
	worker_id = sql.Column(sql.ForeignKey('employees.employee_id'), primary_key=True)
	worker = orm.relationship('Employee')
	date = sql.Column(sql.Date, primary_key=True)
	start_time = sql.Column(sql.DateTime)
	end_time = sql.Column(sql.DateTime)

	def __repr__(self):
		worker_data = json.loads('%s' % self.worker)
		data = {
			'employee_id': worker_data.get('employee_id'),
			'name': worker_data.get('name'),
			'photo': worker_data.get('photo'),
			'monthly_salary': worker_data.get('monthly_salary'),
			'date': "%s" % self.date.strftime(date_format),
			'start_time': "%s" % self.start_time.strftime(time_format),
			'end_time': "%s" % self.end_time.strftime(time_format)
		}
		return json.dumps(data)

class Company(Base):
	__tablename__ = "companies"
	company_id = sql.Column(sql.Integer, primary_key=True)
	name = sql.Column(sql.String)
	address = sql.Column(sql.String)
	postal_code = sql.Column(sql.String)

	def __repr__(self):
		data = {
			'company_id': self.company_id,
			'name': self.name,
			'address': self.address,
			'postal_code': self.postal_code
		}
		return json.dumps(data)

class Material(Base):
	__tablename__ = "materials"
	material_id = sql.Column(sql.Integer, primary_key=True)
	name = sql.Column(sql.String)
	description = sql.Column(sql.String)

	def __repr__(self):
		data = {
			'material_id': self.material_id,
			'name': self.name,
			'description': self.description
		}
		return json.dumps(data)

class Project(Base):
	__tablename__ = "projects"
	project_id = sql.Column(sql.Integer, primary_key=True)
	project_title = sql.Column(sql.String)
	project_description = sql.Column(sql.String)
	poc_name = sql.Column(sql.String)
	poc_contact = sql.Column(sql.String)

	# one to one
	company_id = sql.Column(sql.Integer, sql.ForeignKey('companies.company_id'))
	company = orm.relationship("Company")

	# one to many, but with additional params
	materials_qty = orm.relationship("Project_Material")

	# one to many
	timelines = orm.relationship("Project_Timeline")
	statuses = orm.relationship("Project_Status")

	# one to one
	site_manager_id = sql.Column(sql.Integer, sql.ForeignKey('users.user_id'))
	site_manager = orm.relationship("User")

	# one to many
	workers = orm.relationship("Project_Worker")
	project_complaints = orm.relationship('Project_Complaint')

	def __repr__(self):
		data = {
			'project_id': self.project_id,
			'project_title': self.project_title,
			'project_description': self.project_description,
			'poc_name': self.poc_name,
			'poc_contact': self.poc_contact,
			'company': json.loads("%s" % self.company),
			'materials_qty': json.loads("%s" % self.materials_qty),
			'timelines': json.loads("%s" % self.timelines),
			'statuses': json.loads("%s" % self.statuses),
			'site_manager': json.loads("%s" % self.site_manager),
			'workers': json.loads("%s" % self.workers),
			'complaints': json.loads("%s" % self.project_complaints)
		}
		return json.dumps(data)

class Project_Material(Base):
	__tablename__ = "project_materials"
	project_id = sql.Column(sql.ForeignKey('projects.project_id'), primary_key=True)
	material_id = sql.Column(sql.ForeignKey('materials.material_id'), primary_key=True)
	material = orm.relationship("Material")
	quantity = sql.Column(sql.Integer)

	def __repr__(self):
		material_data = json.loads("%s" % self.material)
		data = {
			'material_id': material_data.get('material_id'),
			'material_name': material_data.get('name'),
			'quantity': self.quantity
		}
		return json.dumps(data)

class Project_Timeline(Base):
	__tablename__ = "project_timelines"
	timeline_id = sql.Column(sql.Integer, primary_key=True)
	project_id = sql.Column(sql.ForeignKey('projects.project_id'))
	name = sql.Column(sql.String)
	projected_start_date = sql.Column(sql.Date)
	projected_end_date = sql.Column(sql.Date)
	actual_start_date = sql.Column(sql.Date)
	actual_end_date = sql.Column(sql.Date)

	def __repr__(self):
		data = {
			'timeline_id': self.timeline_id,
			'project_id': self.project_id,
			'name': self.name,
			'projected_start_date': "%s" % self.projected_start_date.strftime(date_format) if self.projected_start_date else None,
			'projected_end_date': "%s" % self.projected_end_date.strftime(date_format) if self.projected_end_date else None,
			'actual_start_date': "%s" % self.actual_start_date.strftime(date_format) if self.actual_start_date else None,
			'actual_end_date': "%s" % self.actual_end_date.strftime(date_format) if self.actual_end_date else None
		}
		return json.dumps(data)

class Project_Worker(Base):
	__tablename__ = "project_workers"
	project_id = sql.Column(sql.ForeignKey('projects.project_id'), primary_key=True)
	worker_id = sql.Column(sql.ForeignKey('employees.employee_id'), primary_key=True)
	worker = orm.relationship("Employee")

	def __repr__(self):
		worker_data = json.loads("%s" % self.worker)
		data = {
			'employee_id': worker_data.get('employee_id'),
			'name': worker_data.get('name'),
			'photo': worker_data.get('photo'),
			'contact': worker_data.get('contact'),
			'emergency_contact_name': worker_data.get('emergency_contact_name'),
			'emergency_contact_contact': worker_data.get('emergency_contact_contact')
		}
		return json.dumps(data)

class Project_Status(Base):
	__tablename__ = "project_statuses"
	status_id = sql.Column(sql.Integer, primary_key=True)
	project_id = sql.Column(sql.ForeignKey('projects.project_id'))
	comments = sql.Column(sql.String)
	status = sql.Column(sql.String)
	date_added = sql.Column(sql.Date)

	def __repr__(self):
		data = {
			'status_id': self.status_id,
			'project_id': self.project_id,
			'comments': self.comments,
			'status': self.status,
			'date_added': "%s" % self.date_added.strftime(date_format)
		}
		return json.dumps(data)

class Project_Complaint(Base):
	__tablename__ = "project_complaints"
	complaint_id = sql.Column(sql.Integer, primary_key=True)
	project_id = sql.Column(sql.ForeignKey('projects.project_id'))
	complaint = sql.Column(sql.String)
	date_added = sql.Column(sql.Date)
	resolution_status = sql.Column(sql.String) # unsolved, reviewed, resolved
	review = sql.Column(sql.String)
	date_reviewed = sql.Column(sql.Date)
	date_resolved = sql.Column(sql.Date)

	def __repr__(self):
		data = {
			'complaint_id': self.complaint_id,
			'project_id': self.project_id,
			'complaint': self.complaint,
			'date_added': "%s" % self.date_added.strftime(date_format),
			'resolution_status': "%s" % self.resolution_status,
			'review': self.review,
			'date_reviewed': "%s" % self.date_reviewed.strftime(date_format) if self.date_reviewed else None,
			'date_resolved': "%s" % self.date_resolved.strftime(date_format) if self.date_resolved else None
		}
		return json.dumps(data)

Base.metadata.create_all(bind=engine)
