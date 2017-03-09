#!/usr/bin/python

from lib.database import *
from datetime import datetime

job_titles = ['Project Manager','Site Manager','Worker']

def list_employees():
    return session.query(Employee).all()

def list_project_managers():
    return session.query(Employee).filter(Employee.job_title == job_titles[0]).all()

def list_site_managers():
    return session.query(Employee).filter(Employee.job_title == job_titles[1]).all()

def list_workers():
    return session.query(Employee).filter(Employee.job_title == job_titles[2]).all()

def add_employee(name, job_title, photo, salary):
    employee = Employee(name="%s" % name, job_title="%s" % job_title, photo="%s" % photo, salary="%s" % salary)
    session.add(employee)
    session.commit()
    return employee

def update_worker_work_hours(worker_id, date_str, num_of_half_hours):
    date = datetime.strptime("%s" % date_str,'%Y-%m-%d').date()
    work_half_hours = session.query(Employee.Work_Half_Hours).filter(Employee.Work_Half_Hours.worker_id=="%d" % int(worker_id), Employee.Work_Half_Hours.date==date).first()
    if not work_half_hours:
        session.add(Employee.Work_Half_Hours(worker_id="%d" % int(worker_id), date=date, num_of_half_hours="%d" % int(num_of_half_hours)))
    else:
        work_half_hours.num_of_half_hours = "%d" % num_of_half_hours
    session.commit()
