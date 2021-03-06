********************
Testing this project
********************
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
======================
Each app_ contains its own ``tests`` folder. These tests exclusively test their corresponding app. An ``integrated_tests`` folder present in the root directory contains selenium_ tests that test the website itself. 

.. _app: https://docs.djangoproject.com/en/3.0/ref/applications/
.. _selenium: https://pypi.org/project/selenium/

Running the tests
=================
A ``pytest.ini`` present in the root directory takes care of pointing to the correct settings. It also writes the test coverage in ``htmlcov/``. Simply run ``pytest`` in the root directory to get the tests underway. 

