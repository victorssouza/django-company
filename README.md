# Django's Company

This project was created as a POC for an fictional e-commerce app for managing employees through an API REST and/or Django's administration page

### Prerequisites

We current support both Docker and virtualenv project's execution, if you do not want to configure virtualenv just use Docker for the entire setup.

- Python 3 +
- virtualenv 15.x +
- Docker 17.x +

## Getting Started

### Docker

Docker makes everything easy, just build the image and run it binding the application port between the container and your local machine:

```
# Build the image
$ docker build -t django-company:0.1.2 .
$ docker run -d -p 8000:8000 django-company:0.1.2
```

Now open your browser through the url: http://localhost:8000/ to check the API REST minimal documentation.  

### virtualenv

If you want to manage the setup for yourself feel free to use a virtualenv (to not mess with your system):

```
$ pip3 install virtualenv
$ virtualenv mycustomenv
$ mycustomenv/bin/activate
$ pip3 install -r requirements.txt
```  

Start Django's migrations:  

```
$ python3 manage.py makemigrations employees
$ python3 manage.py migrate
$ python3 manage.py loaddata employees/fixtures.json
```  
  
Start the server running `python3 manage.py runserver`  

You are ready to rock: http://localhost:8000/  

## Running the automated tests

If you are running the project with Docker, the tests will run before the server startup automatically and will `exit 1` the container if any unit test fails.  

You can also run the tests in a separated container:  

`docker run -it django-company:0.1.2 python3 manage.py test -v 2`  

If you want to run the tests locally, just: `python3 manage.py test -v 2`  

## Usage

You can now interact with the API REST, for example using the terminal:  

```
# To list all employees
$ curl -H "Content-Type: application/javascript" http://localhost:8000/api/v1/employee/  

# To create a new employee
$ curl -d '{"name":"Employee Name", "email":"some@domain.com", "department":"Developer"}' -XPOST -H "Content-Type: application/javascript" http://localhost:8000/api/v1/employee/  

# To list an specific employee
$ curl -H "Content-Type: application/javascript" http://localhost:8000/api/v1/employee/2/

# To update an attribute from an employee
$ curl -d '{"name":"New Name"}' -XPUT -H "Content-Type: application/javascript" http://localhost:8000/api/v1/employee/1/

# To delete an employee
$ curl -XDELETE -H "Content-Type: application/javascript" http://localhost:8000/api/v1/employee/3/
```  

You can also manage employees data through Django's [admin](http://www.localhost:8000/django-admin "Django's Admin Page") area:  
  
**Credentials**  
login: `developer_guest`  
password: `luiza@123`  
