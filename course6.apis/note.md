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

## Django REST framework (DRF)
- What is DRF
  - DRF is a toolkit built on top of Django, designed to streamline API development.
  - Data convertion: serialization/deserialization.
  - support authentication.
- better api view with decorators
  - rate limiting
  - authentications
- routing classes
  - SimpleRouter
```python
class BookView(APIView):
	def get(self, request, pk):
    	return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
	def put(self, request, pk):
    	return Response({"title":request.data.get('title')}, status.HTTP_200_OK)

```

```python
# views.py
Class BookView(viewsets.ViewSet):
	def list(self, request):
    	return Response({"message":"All books"}, status.HTTP_200_OK)
	def create(self, request):
    	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
	def update(self, request, pk=None):
    	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
	def retrieve(self, request, pk=None):
    	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
	def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
	def destroy(self, request, pk=None):
    	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)

# urls.py
urlpatterns = [
	path('books', views.BookView.as_view(
    	{
        	'get': 'list',
        	'post': 'create',
    	})
	),
    path('books/<int:pk>',views.BookView.as_view(
    	{
        	'get': 'retrieve',
        	'put': 'update',
        	'patch': 'partial_update',
        	'delete': 'destroy',
    	})
	)
]
```
- Generic views and ViewSets in DRF
  - ViewSets
    - a collection of resources: list()/GET, create()/POST
    - a single resource: retrive()/GET, update()/PUT, partial_update()/PATCH, destroy()/DELETE
  - Generic Views 

- Function and class-based views
  - class-based 
    - write less code
    - less code duplication
    - extend and add features
    - methods for HTTP request types

- Django debug toolbar
  - profiling
  - sql
  - headers

- Serializers
  - HyperlinkedRelatedField or HyperlinkedModelSerializer
  - Benefit of serialization
    - It cnan convert model instances to native python data types
    - It can convert user input and map it to models
    - It can validate data

- Deserialization and validation
  - serialized_item.is_valid(raise_exception=True)

- Renders types
  - TemplateHTMLRenderer
    - template file
  - StaticHTMLRenderer
  - CSV and YAML Renders


## Advanced API development
- Filtering and searching
  - filter: get subset of all items
  - e.g.: https://xxx.xxx/api/?category=main 
  - e.g.: https://xxx.xxx/api/?search=chocolate 
- ordering
  - The django-filters package is mostly used with class-based views
  - function-based views so you can take advantage of Django's native sorting methods.
  - e.g.: https://xxx.xxx/api/?ordering=price,-inventory
- importance of data validation
  - validation in DRF
```python
# 1 conditions if field: add following line before the Meta class
price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)

# 2 Using keyword arguments in the Meta class
class Meta:
    model = MenuItem
    fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
    extra_kwargs = {
    'price': {'min_value': 2},
    'stock':{'source':'inventory', 'min_value': 0},
}

# 3 Using validate_field() method  above the meta class.
def validate_price(self, value):
        if value < 2:
            raise serializers.ValidationError('Price should not be less than 2.0')
        return value  # Return value if it passes validation


# 4 using validate() method: DRF will pass all input values to this method. 
def validate(self, attrs):
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)
```
- Data sanitization
- pagination
- caching
  - reverse proxy servrer
  - web 
  - database server
  - client

- Token-base authtication
  - add token in admin panel
  - add token from DRF api-token-auth/
- User role
  -  The same API can return different output for different users 
- Setting up API throttling
  - Add support for throttling  
    - throttling for class-based view
    - conditional throttling
    - Custom throttling classes


```python
# setting.py
'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
],

# Throttling for class-based views,
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
class MenuItemsViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# in setting.py
'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '10/minute'
}

# Conditional throttling
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
 
    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []  
        return [throttle() for throttle in throttle_classes]
```

- Djoser library
- JWT: json web token 
  - After an access token expire a client can regenerate an access token again to authenticate its API calls again,
- The only way to stop a client from regenerating an access token is by blacklisting the refresh token.
- You can specify a period after which an access token expires
  - a refresh token expires can not be specify