# Flamelite SmartBox Server
A python flask server using sqlalchemy as Object Relational Model (ORM) database.

## Pre-requisites
You'll need to install python, flask, sqlalchemy and sqlite for this to work. I've done this on an ubuntu environment and here are the instructions ran:

```console
$ sudo apt-get install python python-flask python-sqlalchemy sqlite3
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
<li><a href='http://localhost:8080/ws/list_users' target='_blank'>http://localhost:8080/ws/list_users</a></li>
<li><a href='http://localhost:8080/ws/list_employees'>http://localhost:8080/ws/list_employees</a></li>
<li><a href='http://localhost:8080/ws/list_companies'>http://localhost:8080/ws/list_companies</a></li>
<li><a href='http://localhost:8080/ws/list_projects'>http://localhost:8080/ws/list_projects</a></li>
<li><a href='http://localhost:8080/ws/list_site_manager_projects?site_manager_id=2'>http://localhost:8080/ws/list_site_manager_projects?site_manager_id=2</a></li>
<li><a href='http://localhost:8080/ws/list_workers_without_project?start_date=2017-03-10&end_date=2017-03-21'>http://localhost:8080/ws/list_workers_without_project?start_date=2017-03-10&end_date=2017-03-21</a></li>
</ul>

URLs that have some kind of HTML formatting.
<ul>
<li><a href='http://localhost:8080/ws/login'>http://localhost:8080/ws/login</a></li>
<li><a href='http://localhost:8080/list_projects.html'>http://localhost:8080/list_projects.html</a></li>
</ul>
