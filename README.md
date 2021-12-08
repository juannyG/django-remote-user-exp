# django-remote-user-exp

### Setup
```sh
git clone git@github.com:juannyG/django-remote-user-exp.git
cd django-remote-user-exp
docker-compose build
docker-compose run web python manage.py migrate
```

You'll want to create a super user so you can access http://localhost:8000/admin

```sh
docker-compose run web python manage.py createsuperuser
```

You should now be able to run the application
```
docker-compose up web
```
