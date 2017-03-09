#!/usr/bin/python

import lib.common_infra as ci
import lib.hr as hr
import lib.crm as crm
import lib.project as prj
import json
import sqlalchemy.ext.declarative as ext_dec
import datetime


def populate_db():
    users = []
    users.append(ci.add_user(name='Alex', username='alex'.lower(), password='alex123', role='Project Manager'))
    users.append(ci.add_user(name='Bobby', username='bobby'.lower(), password='bobby123', role='Site Manager'))
    users.append(ci.add_user(name='Charles', username='charles'.lower(), password='charles123', role='Site Manager'))

    managers = []
    managers.append(hr.add_employee(name='Alex', job_title='Project Manager', photo='', salary="5000"))
    managers.append(hr.add_employee(name='Bobby', job_title='Site Manager', photo='', salary="3500"))
    managers.append(hr.add_employee(name='Charles', job_title='Site Manager', photo='', salary="3500"))

    workers = []
    workers.append(hr.add_employee(name='David', job_title='Worker', photo='', salary="2000"))
    workers.append(hr.add_employee(name='Eugene', job_title='Worker', photo='', salary="1900"))
    workers.append(hr.add_employee(name='Fabian', job_title='Worker', photo='', salary="1800"))
    workers.append(hr.add_employee(name='George', job_title='Worker', photo='', salary="1700"))
    workers.append(hr.add_employee(name='Henry', job_title='Worker', photo='', salary="1600"))
    workers.append(hr.add_employee(name='Ian', job_title='Worker', photo='', salary="1500"))
    workers.append(hr.add_employee(name='Julian', job_title='Worker', photo='', salary="1400"))
    workers.append(hr.add_employee(name='Kenny', job_title='Worker', photo='', salary="1300"))

    companies = []
    companies.append(crm.add_company(name='Singapore Airlines Limited', address='25 Airline Road, Airline House', postal_code='819829'))
    companies.append(crm.add_company(name='Shimizu Corporation', address='8 Kallang Avenue, #05-01 Aperia Tower 1', postal_code='339509'))

    materials = []
    materials.append(prj.add_material(name='Fire Rated Glass', description='Fire rated glass rating of up to 4 hours.'))
    materials.append(prj.add_material(name='X-Ray Resistant Glass', description='X-ray and radiation protective lead glass'))
    materials.append(prj.add_material(name='Bullet Resistant Glass', description='Composite panel made up of layer of glass with interlayers of polymer and polycarbonate plates.'))

    project_1 = prj.add_project(project_title='test', project_description='test',company=companies[0], poc_name='test',poc_contact='test', site_manager=users[1])
    prj.add_project_materials_qty(project_1.project_id, materials[0], 10)
    prj.add_project_materials_qty(project_1.project_id, materials[1], 20)
    prj.add_project_materials_qty(project_1.project_id, materials[2], 30)
    prj.add_project_worker(project_1.project_id, workers[0].employee_id)
    prj.add_project_worker(project_1.project_id, workers[1].employee_id)
    prj.add_project_worker(project_1.project_id, workers[2].employee_id)
    prj.add_project_worker(project_1.project_id, workers[3].employee_id)

    supply_shipment_start_date = datetime.datetime.strptime('2017-03-10', '%Y-%m-%d')
    supply_shipment_end_date = datetime.datetime.strptime('2017-03-17', '%Y-%m-%d')
    manufacture_start_date = datetime.datetime.strptime('2017-03-18', '%Y-%m-%d')
    manufacture_end_date = datetime.datetime.strptime('2017-03-20', '%Y-%m-%d')
    installation_start_date = datetime.datetime.strptime('2017-03-21', '%Y-%m-%d')
    installation_end_date = datetime.datetime.strptime('2017-03-31', '%Y-%m-%d')
    prj.add_project_timeline(project_1.project_id, "Supply Shipment", supply_shipment_start_date, supply_shipment_end_date)
    prj.add_project_timeline(project_1.project_id, "Product Manufacture", manufacture_start_date, manufacture_end_date)
    prj.add_project_timeline(project_1.project_id, "Installation", installation_start_date, installation_end_date)
    complaint_1 = crm.add_project_complaint(project_1.project_id, "The door handle came off!")
    crm.review_project_complaint(complaint_1.complaint_id, "Applied reinforced steel lining to with PVC glue.")
    crm.resolve_project_complaint(complaint_1.complaint_id)

    complaint_2 = crm.add_project_complaint(project_1.project_id, "The door handle came off again...")

    today = datetime.datetime.now().date()
    hr.update_worker_work_hours(workers[0].employee_id, today, 16)
    hr.update_worker_work_hours(workers[1].employee_id, today, 16)
    hr.update_worker_work_hours(workers[2].employee_id, today, 18)
    hr.update_worker_work_hours(workers[3].employee_id, today, 18)
    hr.update_worker_work_hours(workers[0].employee_id, today, 5)

def list_users():
    return ci.list_users()

def user_login(username, password):
    return ci.user_login(username=("%s" % username).lower(), password="%s" % password)

def list_employees():
    return hr.list_employees()

def list_companies():
    return crm.list_companies()

def list_projects():
    return prj.list_projects()

def list_site_manager_projects(user_id):
    user = ci.get_user_by_id("%d" % int(user_id))
    if user and "site manager".lower() == ("%s" % user.role).lower():
        return prj.list_site_manager_projects(user.user_id)
    return None

def list_workers_without_project(start_date_str, end_date_str):
    def clash(start_date_1, end_date_1, start_date_2, end_date_2):
        duration_1 = end_date_1 - start_date_1
        period_1 = []
        for i in range(duration_1.days + 1):
            period_1.append(start_date_1 + datetime.timedelta(days=i))

        duration_2 = end_date_2 - start_date_2
        period_2 = []
        for i in range(duration_2.days + 1):
            period_2.append(start_date_2 + datetime.timedelta(days=i))

        return True if len(set(period_1) & set(period_2)) != 0 else False

    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    extracted_projects = []
    projects = prj.list_projects()
    for project in projects:
        for timeline in project.timelines:
            if timeline.name.lower() == "installation".lower() and clash(start_date, end_date, timeline.start_date, timeline.end_date):
                extracted_projects.append(project)
                break

    workers_with_project = []
    for project in extracted_projects:
        for worker in project.workers:
            workers_with_project.append(worker.worker_id)

    workers_without_project = []
    employees_workers = hr.list_workers()
    for worker in employees_workers:
        if worker.employee_id not in workers_with_project:
            workers_without_project.append(worker)

    return None if len(workers_without_project) == 0 else workers_without_project

def add_project_complaint(project_id, complaint):
    project = prj.get_project_by_id(project_id="%d" % int(project_id))
    return crm.add_project_complaint(project_id="%d" % int(project_id), complaint="%s" % complaint) if project else None

def review_project_complaint(complaint_id, action_taken):
    return crm.review_project_complaint(complaint_id, action_taken)

def list_complaint_resolution_recommendations(project_id):
    project = prj.get_project_by_id(project_id="%d" % int(project_id))
    return crm.list_complaint_resolution_recommendations("%d" % int(project_id)) if project else None
