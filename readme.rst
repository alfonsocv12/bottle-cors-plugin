bottle-cors-plugin
==================

The easiest way to implement cors on your bottle py web application

Installing the plugin
---------------------

::

    pip install bottle-cors-plugin

after this on your bottle app you need to import cors_plugin and install
for example.

.. code-block:: python

    # -*- coding: utf-8 -*-
    from bottle import app, response, route, run
    from bottle_cors_plugin import cors_plugin

    @route('/', method='GET')
    def landing():
      response.content_type = 'application/json'
      return {'status': 'Works'}

    #Confugure the server
    app = app()
    app.install(cors_plugin('*'))

    if name == "__main__":
      run(host='localhost', port=7000)

On the cors_plugin function you can send a simple string or array of origins
this variable will set globaly on the plugin so you just set-it one time to add *
origins just don't put anything on the function

.. code-block:: python

  cors_plugin()

This will return the * origins

.. code-block:: python

    cors_plugin('https://google.com')

with just google.com as and origin or

.. code-block:: python

    cors_plugin(['https://google.com', 'http://google.com'])

for multiple origins

Aborts
------

for normal abort errors you need to import the abort of the cors_plugin like
this

.. code-block:: python

    from bottle_cors_plugin import abort


    @route('/', method='GET')
    def landing():
      response.content_type = 'application/json'
      abort(500, 'Hola')
      return {'status': 'Works'}

It works with all errors, and for custom error handler just import the cors_headers
to apply on the function example like this

.. code-block:: python

    # -*- coding: utf-8 -*-
    from import_env import os
    from bottle import error, response
    from bottle_cors_plugin import cors_headers

    error_log = error

    for status_code in range(200, 600):
    @error(status_code)
    def errorCustom(error_log):
        cors_headers()
        error_log.content_type = 'application/json'
        return error_log.body
