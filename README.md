This is a Django app which is basically a E-library or a online bookstore.

In this app you can view books of different sections and you can add books also if you are a registered user


 INSTALLATION :
  
  Just pull the app from the repository to your local enviornment
  

HOW TO RUN ON LOCAL ENVIORNMENT :

  Basically this app can be run on local surver and it can also be run on the gunicorn server.
  
  To run this app on local server just run python manage.py runserver --settings=mysite.settings.local
  
HOW TO RUN ON PRODUCTION ENVIORNMENT :
  
  To run this app on gunicorn server just run gunicorn mysite.wsgi:application.
  
  To run this app on local server with production settings run python manage.py runserver --settings=mysite.settings.production
  
This library is live at http://aqueous-ridge-4845.herokuapp.com/.  Please have a look :) .
