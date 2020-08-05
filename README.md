## udn-el
### Python package requirements

```
pip install -r requirements.txt
```

### Project Data

[google-drive link](https://drive.google.com/drive/folders/135CXe7IoqR3fg79LIm0Tz_l4NEytbdRZ?usp=sharing)


Put all directories in google drive into data directory.

```
[projectname]/
├── [appname]/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
└── data    <-- here
```


### Run the website

```
python manage.py runserver 0.0.0.0:5487
```