=====
Calendar File
=====

CalFile is a simple Django app to create a calendar file.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "calfile" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'calfile',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('calfile/', include('calfile.urls')),

3. Post http://127.0.0.1:8000/calfile/ with parameters.