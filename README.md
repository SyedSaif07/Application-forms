Please follow the instructions carefully.
Create a project named Appforms using startproject command
Create an app named Userforms using startapp command.
Utilize the .py file I have shared. Using whatever .py files I have shared,make changes accordingly.
You will be required to create an urls.py file in your app Userforms similar to what you have in your project. Create an empty urls.py file and take the code below,
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='userapp'),
]
Now create templates folder in your app Userforms and create a folder with the name of your app(Userforms) as a subdirectory of templates folder. Now place Submit.html there.
Create static folder in your app Userforms and create a folder with the name of your app(Userforms) as a subdirectory of static folder.
Open Submit.html and see how .css and .js files are placed.Example: 'Userforms/css/style.css'. So You already have Userforms folder in static. Now you need to create a css folder within which you can place style.css
Follow the above step for all the styling files like .css, img, .js.etc.
Now, you can run your server and locate to localhost. You will be able to view the appplication.
