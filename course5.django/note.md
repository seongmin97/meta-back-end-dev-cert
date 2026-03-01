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

## Models

## Templates

