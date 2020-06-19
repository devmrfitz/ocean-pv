*******************************
OCEAN-Personality-Visualization
*******************************

.. image:: https://img.shields.io/github/license/IgnisDa/OCEAN-personality-visualization?style=for-the-badge   
	:alt: GitHub

A website that helps you visualize your personality using graphs and compare it with others. It asks you a
series of questions and analyzes your inputs to create an easy to understand graph. It also provides you an
easy way to share these results with your peers and compare your personalities. It is based on the 
OCEAN_ personality model which is the most acceptable model to measure personality used by researchers. 

.. _OCEAN: https://en.m.wikipedia.org/wiki/Big_Five_personality_traits 

The documentation lives at https://ocean-personality-visualization.readthedocs.io/en/latest/

The Website
===========
.. warning:: This is incomplete 

Prerequisites
=============
This website has been built using the Django_ framework, using Python_ (version: 3.8), HTML_ (version: 5), 
and other web-dev components. 

.. _Django: https://www.djangoproject.com 
.. _Python: https://www.python.org
.. _HTML: https://en.wikipedia.org/wiki/HTML

Installing
==========
First, clone this project from github:
	
.. code:: console 

	$ git clone https://github.com/IgnisDa/OCEAN-personality-visualization.git
	
The root directory contains a ``requirements.txt`` which can you can use to whip up a working environment. 

.. code:: console

	$ cd OCEAN-personality-visualization
	$ python -m venv env
	$ source ./env/bin/activate
	$ pip install -r requirements.txt

If you use Poetry_ package manager to manage your dependencies, you can run the following command in the project root. 

.. code:: console 

	$ poetry install --no-dev

To get the website up and running, you need to run the following:
	
.. code:: console

	$ python manage.py makemigrations
	$ python manage.py migrate
	$ python manage.py loaddata questions.json user_data.json
	$ python manage.py runserver 

You can then visit ``127.0.0.1:8000/`` to access the website.

Project Structure
=================
The project was created using the command ``django-admin startproject ocean_website`` and that is also the main directory where important files like ``settings.py`` and ``wsgi.py`` live. 

This project uses the default django project structure_ with a few modifications. The apps that are part of the website are ``graphs``, ``home``, ``interactions``, ``users`` and are present in their corresponding directories. 

Major modifications include changing the location of ``ocean_website/settings.py`` to ``ocean_website/settings/settings.py``. 
This was done because this project uses 4 different settings files for *development*, *testing*, *production* and *heroku*. The ``manage.py`` and ``wsgi.py`` files have been changed accordingly. 

.. warning:: 
	Add stuff about $OCEAN_PV

.. _structure: https://django-project-skeleton.readthedocs.io/en/latest/structure.html

Running Tests
=============
There is a ``requirements-dev.txt`` in ``docs/`` which will install all the dependencies required for testing this project. The tests are
present in ``*/tests/*`` and ``integrated_tests/*``. 

.. code:: console

	$ python -m venv env
	$ source ./env/bin/activate
	$ pip install -r docs/requirements-dev.txt

If you use Poetry_ package manager to manage your dependencies, you can instead run the following command in the project root. 

.. code:: console 

	$ poetry install

.. _Poetry: https://python-poetry.org/

How tests are arranged
----------------------
Since Django_ allows to separate 
Each app_ contains 
