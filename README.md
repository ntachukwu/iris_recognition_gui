## Set Up

These system was deployed and executed on an Ubuntu 20.04 OS and the Python interpreter is Python 3.8.5.

First, create a virtual environment

```bash
python3 -m venv gui_venv 
source gui_venv/bin/activate
```

Clone this repository and install requirements

```bash
git clone https://github.com/Th3nn3ss/iris_recognition_gui.git
cd iris-recognition_gui
pip install -r requirements.txt
```

Make migrations, export django settings to environment

```bash
python manage.py migrate
export DJANGO_SETTINGS_MODULE=gui_config.settings
```

Create superuser. Run the command below and provide your name and password at the prompt.

```bash
python manage.py createsuperuser
```

Run server
```bash
python manage.py runserver
```

Click the "register a new profile" button on the home page or enter the url "localhost:8000/admin/"
At the admin panel, click on "Add new profile".
Fill in the profile details and enter a valid iris image for identifying the profile.


Navigate back to the home screen at "localhost:8000" and login to view any profile detail.

# Enjoy
