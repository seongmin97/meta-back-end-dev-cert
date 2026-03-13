## REST APIs
### Course intro
- pipenv
  - cd dir
  - pip shell
  - pip install
- REST APIs
  - Characteristics
  - Benefits
  - States and resource types
  - Request life cycle
- authentication, authorisation
- serialization, deserialization

### APIs intro
- HTTP, HTTPS
  - GET, POST, PUT, PATCH, DELETE
  - status code
  - response type: HTML, JSON, XML, YAML
- RESTfulness
  - client server
  - stateless
    - ​The server cannot recognize the client automatically. ​API calls must include more information about the user
  - cacheable
 
 - Naming convention
  - Always lower case
  - variables: camel case
  - forward slash: inheritence relationship
  - API always use noun
  - Avoid special characters 
  - Use query parameters to filter when necessary 
    - /articles?per-page=10&page=2

### Principles of API development
- REST best practice: 
  - KISS: keep it simple stupied
  - always provide a way to filter large result sets and rearrange
  - versioning
  - caching
  - rate limiting, monitoring
    - response time
    - bandwidth
- Security and authtication
  - SSL certificates
  - signed URL: use signature
    - Signed URLs give someone limited access to a specific resource for a brief period of time. 
    - HMAC: popular signing mechanism
  - Token-based authtication
    - JSON web token, JWT
  - HTTP code in auth process
    - 401 unauthorized: it lacks valid authentication credentials, e.g. invalid password
    - 403 forbidden
  - CORS
  - firewalls
- access control
  - with access control you can specify which users are allowed to access your API.
  - roles and privileges
    - A role is a collection of privileges and a privilege is whether you are allowed to do a specific task.
  - authorization

### Writing your first API
- pipenv, requirements.txt
  - split app
  - use virtual env
  - versioning, new folder
  - list dependencies
  - seperate resource folders
  - multiple settings files
  - Business logic in model rather than view.
- consequences of a poorly designed API
  - data breach
  - data corruption
  - wastage of computing power and memory
  - wastage of bandwidth
  - bad user experience
  - breaking client applicaitons
  - failure to manage the app
- Debugging

## Django REST framework


## Advanced API development