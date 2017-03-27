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

def populate_db():
	emergency_contact_name = 'Zukifli'
	emergency_contact_contact = '+65 92223333'

	# Create employee
	managers = []
	managers.append(hr.create_employee('Alex', job_titles[0], 'images/Alex.jpg', "+65 92223334", emergency_contact_name, emergency_contact_contact, "5000"))
	managers.append(hr.create_employee('Bobby', job_titles[1], 'images/Bobby.jpg', "+65 92223335", emergency_contact_name, emergency_contact_contact, "3500"))
	managers.append(hr.create_employee('Charles', job_titles[1], 'images/Charles.jpg', "+65 92223336", emergency_contact_name, emergency_contact_contact, "3500"))

	workers = []
	workers.append(hr.create_employee('David', job_titles[2], 'images/David.jpg', "+65 92223337", emergency_contact_name, emergency_contact_contact, "2000"))
	workers.append(hr.create_employee('Eugene', job_titles[2], 'images/Eugene.jpg', "+65 92223338", emergency_contact_name, emergency_contact_contact, "1900"))
	workers.append(hr.create_employee('Fabian', job_titles[2], 'images/Fabian.jpg', "+65 92223339", emergency_contact_name, emergency_contact_contact, "1800"))
	workers.append(hr.create_employee('George', job_titles[2], 'images/George.jpg', "+65 92223340", emergency_contact_name, emergency_contact_contact, "1700"))
	workers.append(hr.create_employee('Henry', job_titles[2], 'images/Henry.jpg', "+65 92223341", emergency_contact_name, emergency_contact_contact, "1600"))
	workers.append(hr.create_employee('Ibrahim', job_titles[2], 'images/Ibrahim.jpg', "+65 92223342", emergency_contact_name, emergency_contact_contact, "1500"))
	workers.append(hr.create_employee('Julian', job_titles[2], 'images/Julian.jpg', "+65 92223343", emergency_contact_name, emergency_contact_contact, "1400"))
	workers.append(hr.create_employee('Kenny', job_titles[2], 'images/Kenny.jpg', "+65 92223344", emergency_contact_name, emergency_contact_contact, "1300"))

	# Create user
	users = []
	users.append(ci.create_user('alex', 'alex123', managers[0].job_title, managers[0]))
	users.append(ci.create_user('bobby', 'bobby123', managers[1].job_title, managers[1]))
	users.append(ci.create_user('charles', 'charles123', managers[2].job_title, managers[2]))

	# Create companies
	companies = []
	companies.append(crm.create_company('Singapore Airlines Limited', '25 Airline Road, Airline House', '819829'))
	companies.append(crm.create_company('Shimizu Corporation', '8 Kallang Avenue, #05-01 Aperia Tower 1', '339509'))

	# Create materials
	materials = []
	materials.append(pm.create_material('Fire Rated Glass', 'Fire rated glass rating of up to 4 hours.'))
	materials.append(pm.create_material('X-Ray Resistant Glass', 'X-ray and radiation protective lead glass'))
	materials.append(pm.create_material('Bullet Resistant Glass', 'Composite panel made up of layer of glass with interlayers of polymer and polycarbonate plates.'))

	# Create project
	project_1 = pm.create_project(project_title='West Mall Carpark Basement Doors', project_description='To install 2 x fire rated glass doors at basement 1, lobby 1, 2, and 3.',company=companies[1], poc_name='Julius Tan',poc_contact='+65 9832 4486', site_manager=users[1])

	# Add project materials
	pm.add_project_material_qty(project_1.project_id, materials[0], 10)

	# Add project workers
	pm.assign_project_workers(project_1.project_id, workers[0])
	pm.assign_project_workers(project_1.project_id, workers[1])
	pm.assign_project_workers(project_1.project_id, workers[2])
	pm.assign_project_workers(project_1.project_id, workers[3])

	# Create project timelines
	supply_shipment_start_date = datetime.datetime.strptime('2017-03-10', '%Y-%m-%d').date()
	supply_shipment_end_date = datetime.datetime.strptime('2017-03-17', '%Y-%m-%d').date()
	manufacture_start_date = datetime.datetime.strptime('2017-03-18', '%Y-%m-%d').date()
	manufacture_end_date = datetime.datetime.strptime('2017-03-20', '%Y-%m-%d').date()
	installation_start_date = datetime.datetime.strptime('2017-03-21', '%Y-%m-%d').date()
	installation_end_date = datetime.datetime.strptime('2017-03-31', '%Y-%m-%d').date()
	pm.add_project_timeline(project_1.project_id, timeline_names[0], supply_shipment_start_date, supply_shipment_end_date)
	pm.add_project_timeline(project_1.project_id, timeline_names[1], manufacture_start_date, manufacture_end_date)
	pm.add_project_timeline(project_1.project_id, timeline_names[2], installation_start_date, installation_end_date)

	# Create project statuses
	pm.update_project_status(project_1.project_id, 'Ordered fire-rated glasses from Denmark.', project_statuses[0], supply_shipment_start_date)
	pm.update_project_status(project_1.project_id, 'Fire-rated glasses from Denmark has arrived.', project_statuses[1], supply_shipment_end_date)

	# Create project complaints
	complaint_1 = crm.add_project_complaint(project_1.project_id, "The door handle came off!")
	#crm.review_project_complaint(complaint_1.complaint_id, "Requires application of PVC glue to reinforce steel lining with handle.")

	complaint_2 = crm.add_project_complaint(project_1.project_id, "The glass shatered suddenly!")
	return None
