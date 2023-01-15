# My New site
This project was created using Python Object-Oriented programming language and the Django virtual 
environment the goal is to demonstrate how we can create models and views. Following this tutorial allow me to see the inside
of Django and how easy or complex it can get. We can easily store data and connect to a database.


## About this Project:
This project was created based in [Django Documentation](https://docs.djangoproject.com/en/4.1/).

- Back-End Web Development - BSC30922 & BTM0922 - Semester 1 & 2.
- Student Number: `22773`
- Student name: `Madelin Vasquez`
- Lecturer: Geoff-Wright. 

## Part 1:
[Django Documentation, part 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- Creating your first project
- Server development 
- Polls app creation
- Writing the first view 

For running the server type on terminal:
> py manage.py runserver

> http://127.0.0.1:8000/

> http://127.0.0.1:8000/polls/


## Part 2:
[Django Documentation, part 2](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)
- [Setting up the mySQL database](https://www.javatpoint.com/how-to-connect-mysql-to-django)
we do this by creating a new database, and linking to the Django project by installing mysqlclient
<img title="Choice and question table in the my_site_datase" src="C:\Users\Tymek\PycharmProjects\mynewsite\polls\static\polls\images\screenshots\Screenshot 2023-01-12 180150.jpg">
<img src="C:\Users\Tymek\PycharmProjects\mynewsite\polls\static\polls\images\screenshots\Screenshot 2023-01-12 171159.jpg">


- Creating models
- Activating models
- Modifying API
- Creating an admin user
### Admin details:
> http://127.0.0.1:8000/admin/ 
- Username: `maddie`
- Email: `22773@student.dorset-college.ie`
- Password: `739295`

## Part 3:
[Django Documentation, part 3](https://docs.djangoproject.com/en/4.1/intro/tutorial03/)
- Writing more views using arguments
- Raising a 404 error
- Using the template system
- Removing hardcoded URLs in templates, and Namespacing URL names:
by creating a template directory inside a poll directory and inside this directory an index.html.
Using this namespacing is ideal so the Django chooses the right template for our specific poll app.
- Add namespace to URL

## Part 4:
[Django Documentation, part 4](https://docs.djangoproject.com/en/4.1/intro/tutorial04/)
- Write a minimal form
- Amend URLconf
- Amend views (generic views)

## Part 5:
[Django Documentation, part 5](https://docs.djangoproject.com/en/4.1/intro/tutorial05/)
- Introducing automated testing
- Create a test to expose the bug in the models file
- Improving tour view file

## Part 6:
[Django Documentation, part 6](https://docs.djangoproject.com/en/4.1/intro/tutorial06/)
- Customize your app’s look and feel
- Adding a background-image
- Adding color to the admin page to customize it which allows us to implement and change the color of 
the admin without changing the code. However since this color changes are saved on the local DB
, therefore if we create a new one it would have the default theme colors.
- [Changing colors in Django admin page](https://www.dothedev.com/blog/django-admin-change-color/)
To access the color change Django theme we go to ["themes app"](http://127.0.0.1:8000/admin/admin_interface/theme/).
One of the best features of using this Django package are: 
   - Use the dropdown menu to edit the list_filter in the app.
    - We can change and edit the logo and favicon in the admin app.
    - Rounded corners for a more "modern" appearance
  
 <img src="C:\Users\Tymek\PycharmProjects\mynewsite\polls\static\polls\images\screenshots\Screenshot 2023-01-12 212416.jpg">
## Part7
- Customize admin form  by adding a publication date for a new question



## Login and Logout:
[Login and Logout Documentation](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
- The Django auth app
- Login Page
- User Details:
    - Username: `user`
    - Email: `user@user.com`
    - Password: `123456`
- Create a homepage
- Logout link

## Reset Password:
[Django Password Reset Tutorial](https://learndjango.com/tutorials/django-password-reset-tutorial)
- Django lets us store emails either in the console or as a file.
- http://127.0.0.1:8000/accounts/password_reset/

