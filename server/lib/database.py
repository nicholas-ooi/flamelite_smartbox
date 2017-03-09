#!/usr/bin/python

# imports
import json
import sqlalchemy as sql
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as ext_dec

engine = sql.create_engine("sqlite:///:memory:", convert_unicode=True)
session = orm.scoped_session(orm.sessionmaker(bind=engine))
Base = ext_dec.declarative_base()

# classes
class User(Base):
    __tablename__ = "users"
    user_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    username = sql.Column(sql.String)
    password = sql.Column(sql.String)
    role = sql.Column(sql.String)

    def __repr__(self):
        data = {
            'user_id': self.user_id,
            'name': self.name,
            'username': self.username,
            'role': self.role
        }
        return json.dumps(data)

class Employee(Base):
    class Work_Half_Hours(Base):
        __tablename__ = "worker_work_half_hours"
        worker_id = sql.Column(sql.ForeignKey('employees.employee_id'), primary_key=True)
        date = sql.Column(sql.Date, primary_key=True)
        num_of_half_hours = sql.Column(sql.Integer)

        def __repr__(self):
            data = {
                'date': "%s" % self.date,
                'num_of_half_hours': self.num_of_half_hours
            }
            return json.dumps(data)

    __tablename__ = "employees"
    employee_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    job_title = sql.Column(sql.String)
    salary = sql.Column(sql.Integer)
    work_half_hours = orm.relationship("Work_Half_Hours")
    photo = sql.Column(sql.String)

    def __repr__(self):
        data = {
            'employee_id': self.employee_id,
            'name': self.name,
            'job_title': self.job_title,
            'salary': self.salary,
            'work_half_hours': json.loads("%s" % self.work_half_hours),
            'photo': self.photo
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
    class Project_Materials(Base):
        __tablename__ = "project_materials"
        project_id = sql.Column(sql.ForeignKey('projects.project_id'), primary_key=True)
        material_id = sql.Column(sql.ForeignKey('materials.material_id'), primary_key=True)
        material = orm.relationship("Material")
        quantity = sql.Column(sql.Integer)

        def __repr__(self):
            data = {
                'material': json.loads("%s" % self.material),
                'quantity': self.quantity
            }
            return json.dumps(data)

    class Project_Timelines(Base):
        __tablename__ = "project_timelines"
        timeline_id = sql.Column(sql.Integer, primary_key=True)
        project_id = sql.Column(sql.ForeignKey('projects.project_id'))
        name = sql.Column(sql.String)
        start_date = sql.Column(sql.Date)
        end_date = sql.Column(sql.Date)

        def __repr__(self):
            data = {
                'timeline_id': self.timeline_id,
                'project_id': self.project_id,
                'name': self.name,
                'start_date': "%s" % self.start_date,
                'end_date': "%s" % self.end_date
            }
            return json.dumps(data)

    class Project_Workers(Base):
        __tablename__ = "project_workers"
        project_id = sql.Column(sql.ForeignKey('projects.project_id'), primary_key=True)
        worker_id = sql.Column(sql.ForeignKey('employees.employee_id'), primary_key=True)
        worker = orm.relationship("Employee")

        def __repr__(self):
            return json.dumps(json.loads("%s" % self.worker))

    class Project_Complaints(Base):
        __tablename__ = "project_complaints"
        complaint_id = sql.Column(sql.Integer, primary_key=True)
        project_id = sql.Column(sql.ForeignKey('projects.project_id'))
        complaint = sql.Column(sql.String)
        date_added = sql.Column(sql.Date)
        resolution_status = sql.Column(sql.String) # unsolved, reviewed, resolved
        action_taken = sql.Column(sql.String)
        date_reviewed = sql.Column(sql.Date)
        date_resolved = sql.Column(sql.Date)

        def __repr__(self):
            data = {
                'complaint_id': self.complaint_id,
                'project_id': self.project_id,
                'complaint': self.complaint,
                'date_added': "%s" % self.date_added,
                'resolution_status': self.resolution_status,
                'action_taken': self.action_taken,
                'date_resolved': "%s" % self.date_resolved
            }
            return json.dumps(data)

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
    materials_qty = orm.relationship("Project_Materials")

    # one to many
    timelines = orm.relationship("Project_Timelines")

    # one to one
    site_manager_id = sql.Column(sql.Integer, sql.ForeignKey('users.user_id'))
    site_manager = orm.relationship("User")

    # one to many
    workers = orm.relationship("Project_Workers")
    complaints = orm.relationship("Project_Complaints")

    def __repr__(self):
        data = {
            'project_id': self.project_id,
            'project_title': self.project_title,
            'project_description': self.project_description,
            'poc_name': self.poc_name,
            'poc_contact': self.poc_contact,
            'company': json.loads("%s" % self.company),
            'materials_qty': json.loads("%s" % self.materials_qty),
            'site_manager': json.loads("%s" % self.site_manager),
            'workers': json.loads("%s" % self.workers),
            'complaints': json.loads("%s" % self.complaints),
            'timelines': json.loads("%s" % self.timelines)
        }
        return json.dumps(data)

Base.metadata.create_all(bind=engine)
