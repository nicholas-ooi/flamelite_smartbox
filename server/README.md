# Flamelite SmartBox Server
A python flask server using sqlalchemy as Object Relational Model (ORM) database.

## Pre-requisites
You'll need to install python, flask, sqlalchemy and sqlite for this to work. I've done this on an ubuntu environment and here are the instructions ran:

```console
$ sudo apt-get install python python-flask python-sqlalchemy sqlite3
$ sudo pip install flask-cors
```

## Configuration
In smartbox.py, you'll there are only two main options you'll have to edit.
<ul><li>server_ip</li><li>server_port</li></ul>

Change to any ip and port that you are comfortable with exposing for your machine. Afterwards you can run the server.

```console
$ python smartbox.py
```

## Visiting the page
You can then use the browser to view the site by typing `http://<server_ip>:<server_port>/`.

## Easy access to available URLs
Assuming you kept the server_ip as localhost and server_port as 8080, here are some quick access links after you launch the server.
<ul>
<li><a href='http://localhost:8080/ws/login'>http://localhost:8080/ws/login</a><br/>
Params required (Only POST request method accepted):<br/>
- username<br/>
- password<br/>
</li><br/>
<li><a href='http://localhost:8080/ws/list_site_manager_projects'>http://localhost:8080/ws/list_site_manager_projects</a><br/>
Params required (Only GET request method accepted):<br/>
- site_manager_id (use the user_id, not the employee_id)<br/>
</li><br/>
<li><a href='http://localhost:8080/ws/retrieve_project_details'>http://localhost:8080/ws/retrieve_project_details</a><br/>
Params required (Only GET request method accepted):<br/>
- project_id<br/>
</li><br/>
<li><a href='http://localhost:8080/ws/retrieve_project_statuses'>http://localhost:8080/ws/retrieve_project_statuses</a><br/>
Params required (Only GET request method accepted):<br/>
- project_id<br/>
</li><br/>
<li><a href='http://localhost:8080/ws/retrieve_project_complaints'>http://localhost:8080/ws/retrieve_project_complaints</a><br/>
Params required (Only GET request method accepted):<br/>
- project_id<br/>
</li><br/>
<li>
<a href='http://localhost:8080/ws/retrieve_project_workers'>http://localhost:8080/ws/retrieve_project_workers</a><br/>
Params required (Only GET request method accepted):<br/>
- project_id<br/>
</li><br/>
<li><a href='http://localhost:8080/ws/update_worker_work_hours'>http://localhost:8080/ws/update_worker_work_hours</a><br/>
Params required (Only GET request method accepted):<br/>
- employee_id<br/>
- date (YYYY-mm-dd format)<br/>
- start_time (HH:MM format)<br/>
- end_time (HH:MM format)<br/>
</li>
</ul>
