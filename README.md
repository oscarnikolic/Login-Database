# Login-Database
A quick project that sets up a login and signup website that will be connected to a postgreSQL database. This is integrated into a docker image and uses docker-compose to create a container for the database and a container for the website.

IMPORTANT!
if you want to run the code you need to add a .env file with your postgre sql database! Also remember to change the docker-compose user and password to match your user and password!

Would reccomend running with a venv. 
Templates folder holds the templates for the online website, includes a signup page a loginpage and a home page. They arent designed very well as I am new to HTML but they function.
app.py uses flask and flask-sqlalchemy in order to set up the website, the database, and connect the two, the code is very self explanitory and has a few comments, see the flask documentation if you do not understand how it works. 
config.py is used to configure the database settings before the docker-compose creates the database. It pulls the databaseURL from the .env file which will be used in the app.py when creating the db

dockerfile and dockercompose file are very standard and are set up to create a testserver that you can access through localhost:5000

to run have dockerdesktop installed and use the command "docker-compose up --build" in your cmd. 
