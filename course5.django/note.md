## Introduction
- Create a project
  - create directory
  - create virtual env and activate
  - install Django
  - run Django command such as: `Django-admin startproject demoproject`
  - inside the demoproject, run `python3 manage.py xxxxxx` as needed. e.g. 
    - python3 manage.py startapp myapp
    - python3 manage.py runserver
- django-admin and manage.py commands
- Web framework
  - fast development, clean structure, change, code reusability
  - fast, feature-rich, secure, scalable
  - three-tier arch: presentation, application and data tier.
- MVT overview
  - **urls**: Django's URL dispatcher
  - **view**: The view function reads the path, query, and body parameters included in the client's request 
    - If required, it uses this data to interact with the models to perform CRUD operations.
  - **model**: A python class, Django's Object Relational Mapper helps perform CRUD operations in an object-oriented way instead of invoking SQL queries.
  - **template**: A template is a web page containing a mix of static HTML and Django Template Language code blocks.
    - You place Template web pages in the templates folder with the .html extension.


## Views
- Views functions need to be mapped to URL
- The primary role of the view function is to fetch the data from the client's request, apply a certain processing logic to it and send an appropriate response back to the client. 

```python
from django.shortcuts import render     

def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 
```

- HTTP requests
  - An HTTP request consists of a method (GET, POST, PUT, DELETE), a path to the resource, a version, and headers containing additional information.
  - status codes
    - informational: 100+
    - Successful: 200+
    - Redirection: 300+
    - Client error: 400+
    - Server error: 500+
  - Role of https
    - secure version of http, use encrption to protect data during transmission
    - It ensures that sensitive information remains confidential and secure from unauthorized access.
- Request and Response objects
- URL
  - Scheme/protocol
  - domain name
  - file path
  - URL parameters
- Mapping URLs with params
- render()
  - Combines a given template with a given context dictionary and return an HttpResponse object with that rendered text
- Error handling
  - by raise exceptions

## Models
### Model and migrate
- CRUD operation
  - create, read, update, delete
- django: get() and save()
- model relationship
- create model
- migration
  - syncing
  - version control
  - maintenance: elimintiong the need to write SQL queries directly.
- python3 manage.py `makemigrations`/`migrate`
- Object relationship mapping

### Models and forms
- Django form
- Form Elements and Structure
  - HTML forms collect user data and send it to the server for processing.
  - Django uses the Form class to define and process forms, with form fields as building blocks.
- Types of Form Fields:
  - CharField: Accepts string input, equivalent to text input in HTML.
  - EmailField: Validates email format, equivalent to email input in HTML.
  - IntegerField: Accepts only integers, equivalent to number input in HTML.
  - MultipleChoiceField: Allows multiple options, similar to select elements in HTML.
  - FileField: Enables file uploads, equivalent to file input in HTML.
- Django fields
  - model
  - field properties
    - primary_key, defaultt, unique, choices
  - field type: 
    - CharField, IntegerField, Float Field ...
  - relationship field:
    - ForeignKey
    - on_delete: CASCADE, PROTECT, RESTRICT
    - one-to-one, many-to-one, many-to-many
- Form API

### Admin
- python3 manage.py createsuperuser
  - login into admin panel
  - manage users and permissions.
- default permissions
  - add, change, delete, view

### DB configuratino
- DB options
  - SQLite: simple
  - MySQL: scalabe
- changes configurations in setting.py

## Templates



