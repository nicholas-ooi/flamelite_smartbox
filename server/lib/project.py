#!/usr/bin/python

from lib.database import *

timeline_names = ['Supply Shipment','Product Manufacture','Installation']

def list_materials():
    return session.query(Material).all()

def add_material(name, description):
    material = Material(name="%s" % name, description="%s" % description)
    session.add(material)
    session.commit()
    return material

def list_projects():
    return session.query(Project).all()

def get_project_by_id(project_id):
    return session.query(Project).filter(Project.project_id == "%d" % int(project_id)).first()

def list_site_manager_projects(site_manager_id):
    return session.query(Project).filter(Project.site_manager_id == "%d" % int(site_manager_id)).all()

def add_project(project_title, project_description, company, poc_name, poc_contact, site_manager):
    project = Project(project_title="%s" % project_title, project_description="%s" % project_description, poc_name="%s" % poc_name, poc_contact="%s" % poc_contact, company=company, site_manager=site_manager)
    session.add(project)
    session.commit()
    return project

def add_project_materials_qty(project_id, material, qty):
    session.add(Project.Project_Materials(project_id=project_id, material_id=material.material_id, material=material, quantity=qty))
    session.commit()

def add_project_worker(project_id, worker_id):
    session.add(Project.Project_Workers(project_id="%d" % int(project_id), worker_id="%d" % int(worker_id)))
    session.commit()

def remove_project_worker(project_id, worker_id):
    worker = session.query(Project.Project_Workers).filter(project_id="%d" % int(project_id), worker_id="%d" % int(worker_id)).first()
    session.delete(worker)
    session.commit()

def add_project_timeline(project_id, name, start_date, end_date):
    if name in timeline_names:
        timeline = Project.Project_Timelines(project_id="%d" % int(project_id), name="%s" % name, start_date=start_date, end_date=end_date)
        session.add(timeline)
        session.commit()
        return timeline
    return None
