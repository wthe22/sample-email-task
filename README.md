# Sample Flask Web Server and Email Scheduler #
A simple email scheduler with website as the user interface.
The goal of this project is to create a simple design of a scheduler,
and it does not actually send any emails.
Peewee ORM is used. Python and SQLite3 for Python natively supports
unicode so emails are also unicode compliant.


## Installation ##
Setup script for Windows
1. Run `manage.bat` (windows) or `manage.sh` (linux)
2. **Linux only**: select `Install required packages`
3. Create virtual environment
4. Activate virtual environment
5. Check PIP path, make sure it points to
PIP of the virtual environment
6. Select `Install server` to install project and dependencies
7. You are all set up! Now you can start the server

Database will be initialized automatically
when you start the project.

### Scripts ###
There are several scripts that are useful to know:
```
# Start the web server
start-web

# Start the email scheduler
start-sched

# Populate database with example values
db-populate
```
