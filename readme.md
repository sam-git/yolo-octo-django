
Requires django 1.5

Run the following commands to use the website:

python manage.py syncdb
-- this creates the sqlite3 database and required tables
-- creates two FlatPage objects from backend/fixtures/initial_data.json 

python manage.py createcachetable my_cache_table 
-- this command is needed to create the table in the database used for caching.

To use the website:
python manage.py runserver

visit
http://127.0.0.1:8000/pages/about
--this is the About FlatPage rendered with the FlatPage template

http://127.0.0.1:8000/api/pages/about
--calls the Backend app and returns a JSON representationn of the content field of the About page (and also the primary key and model type -- but 'content' is the only field from the model in the response').

 http://127.0.0.1:8000/about
--calls frontend app, which calls the backend app API using "/about" as an identifier and display the content field on a web page (same content as the above url)

The above examples also work using 'about/contact' instead of 'about'.


extra
-----
The admin interface can be used to add more FlatPages to the app which can then be accessed using the same pattern as the three urls above

The django project uses database caching for the entire site. Pages are cached for 6000 seconds.

author: Sam Grace