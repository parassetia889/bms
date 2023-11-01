# team_hashmap - BMS

The website should have the following features -

1. An API to view all the movies playing in user's city
2. An API to check all cinemas in which a movie is playing along with all the showtimes
3. For each showtime, check the availability of seats
4. User Sign up and login
5. Ability to book a ticket. (No payment gateway integration is required. Assume tickets can be booked for free)

#### Install virtualenv
```pip install virtualenv```

#### Create a virtual environment
```virtualenv venv```

#### Activate the virtual environment
```.\venv\Scripts\activate```

#### Install Django
```pip install django```

#### Create django project
```django-admin startproject book_my_show```

#### Create heartbeat app
```django-admin startapp heartbeat```

#### Install flake8 linter
```pip install flake8```

#### Install pre-commit
```pip install pre-commit```

#### Add pre-commit to .git folder
```pre-commit install```

#### Run server
```python manage.py runserver```
