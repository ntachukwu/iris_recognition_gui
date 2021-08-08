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

Make migrations, export django settings to environment and runserver

```bash
python manage.py migrate
export DJANGO_SETTINGS_MODULE=gui_config.settings
python manage.py runserver
```


# Enjoy
