# Implementation of an information system facilitating the management of commercial stock in an agricultural enterprise.

## Dependencies
**Django**
## Packages
## *django-calculation*
A django app that allows simple calculations in django forms. It provides a Django Widget that derives its value from a expression defined in the widget instance. It updates a field when any of the source fields change
#### Installation : pip install django-calculation

#### To be able to use :
* Add calculation to INSTALLED_APPS in project settings
  
## *django_select2* 
Custom autocomplete fields for Django.
A Django package that improves the user interface for select input fields by integrating the Select2 JavaScript library. It adds features like searching it's especially useful for handling large datasets and simplifies the integration of Select2 into Django projects with an easy-to-use form field and widget.
#### Installation : python3 -m pip install django-select2

#### To be able to use :
* Add django_select2 to INSTALLED_APPS in project settings 
* Add django_select to URL root configuration : path("select2/", include("django_select2.urls")) 

## *BootStrap* :
Install Bootstrap’s source Sass and JavaScript files via npm to get access to the source files, for customization and optimization of the website
#### Installation : npm install bootstrap@5.3.2

## Key Imports
### *django.db.models*
The `models` module is essential for defining the structure of our database models. It provides a set of classes and fields to represent database tables and relationships.

### *django.forms*
The `forms` module is used for creating and handling forms in our application.

### *datetime.datetime*
The `datetime` module is used for handling and manipulating date and time information.

### *django.urls.path*
The `path` function is used for defining URL patterns in our project. It helps in mapping URLs to views and handling routing within the application.

### *django.shortcuts*
The `render`, `redirect`, and `get_object_or_404` functions are used to simplify rendering templates, redirecting users, and handling 404 errors for model instances.

### *django.db.models.Sum/ExpressionWrapper/F/FloatField*
The `Sum`, `ExpressionWraper`, `F` and `FloatField` classes and functions are used for advanced database query operations. They allow us to perform aggregations, apply expressions, and work with numeric fields in our database queries.

### *django.views.decorators.http.require_GET*
The `require_GET` decorator in Django is used to ensure that a view can only be accessed via an HTTP GET request. 

### *django.http.JsonResponse*
`JsonResponse` Django class that represents an HTTP response with a JSON-encoded content. It simplifies the process of returning JSON data from a Django view

### *calculation*
`import calculation` is used in order to be able to use the `django-calculation` package for the calculations done in the forms

### *django_select2.forms as s2forms*
imports the forms module from the `django_select2` package and assign it an alias s2forms. `django_select2` enhances the standard Django select input fields by integrating the `Select2 library`. It adds a search input box to select fields, allowing users to easily search and select options.   

### *django.db.models.sum*
`sum` is functionality that does the sum inside the view
