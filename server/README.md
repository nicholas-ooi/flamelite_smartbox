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
You can then use the browser to view the site by typing http://<server_ip>:<server_port>/.
