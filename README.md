# Dutch-Run Backend

This server is a backend built with Django and Django REST Framework to manage a game's leaderboard.

1. Installation & Setup
   Here is how to set up and run the Django project.

### Create the virtual environment

python -m venv venv

### Activate the virtual environment (Windows)

venv\Scripts\activate

### Activate the virtual environment (macOS/Linux)

source venv/bin/activate

### Install dependencies:

pip install -r requirements.txt

### Run the server:

python manage.py runserver

## API LIST

### Create Game Entry

URL: games/create/

Method: POST

Description: Creates a new game score entry.

### Get Leaderboard

URL: games/leaderboard/

Method: GET

Description: Retrieves the top 100 game scores.
