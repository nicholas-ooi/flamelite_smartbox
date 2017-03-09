#!/usr/bin/python

from lib.database import *
from datetime import datetime

project_status = ['unresolved','reviewed','resolved']

def list_companies():
    return session.query(Company).all()

def add_company(name, address, postal_code):
    company = Company(name="%s" % name, address="%s" % address, postal_code="%s" % postal_code)
    session.add(company)
    session.commit()
    return company

def add_project_complaint(project_id, complaint):
    today = datetime.now().date()
    complaint = Project.Project_Complaints(project_id="%d" % int(project_id), complaint="%s" % complaint, date_added=today, resolution_status = project_status[0])
    session.add(complaint)
    session.commit()
    return complaint

def review_project_complaint(complaint_id, action_taken):
    complaint = session.query(Project.Project_Complaints).filter(Project.Project_Complaints.complaint_id=="%d" % int(complaint_id)).first()
    if complaint:
        complaint.action_taken = "%s" % action_taken
        complaint.resolution_status = project_status[1]
        complaint.date_reviewed = datetime.now().date()
        session.commit()
        return True
    return False

def resolve_project_complaint(complaint_id):
    complaint = session.query(Project.Project_Complaints).filter(Project.Project_Complaints.complaint_id=="%d" % int(complaint_id)).first()
    if complaint:
        complaint.resolution_status = project_status[2]
        complaint.date_resolved = datetime.now().date()
        session.commit()
        return True
    return False

def list_complaint_resolution_recommendations(project_id):
    project = session.query(Project).filter(Project.project_id=="%d" % int(project_id)).first()
    recommendations = []

    similar_project_ids = []
    for material in project.materials_qty:
        projects = session.query(Project.Project_Materials).filter(Project.Project_Materials.material_id=="%d" % material.material_id).all()
        for p in projects:
            if p.project_id not in similar_project_ids:
                similar_project_ids.append(p.project_id)

    for pid in similar_project_ids:
        similar_project = session.query(Project).filter(Project.project_id=="%d" % int(pid)).first()
        for complaint in similar_project.complaints:
            if complaint.resolution_status == project_status[2]:
                recommendations.append(complaint.action_taken)

    return json.dumps(recommendations)
