bottle-cors-plugin
==================

The easiest way to implement CORS on your bottle py web application.

Installing the plugin
---------------------

::

    pip install bottle-cors-plugin

Then, on your bottle app import the `cors_plugin` and install it like so:

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

The `cors_plugin` function accepts a string or an array of strings representing the allowed origins.
Passing no origins to the function will assume `'*'`, that is, all origins are allowed.

.. code-block:: python

  cors_plugin()

This will allow all origins (`'*'`).

.. code-block:: python

    cors_plugin('https://google.com')

Allows just "https://google.com" as origin.

.. code-block:: python

    cors_plugin(['https://google.com', 'http://google.com'])

Is how you define multiple allowed origins.

Aborts
------

For regular abort errors you need to import the `abort` function from `cors_plugin` like so:

.. code-block:: python

    from bottle_cors_plugin import abort


    @route('/', method='GET')
    def landing():
      response.content_type = 'application/json'
      abort(500, 'Hola')
      return {'status': 'Internal error'}

It works with all errors, and if you need a custom error handler, use the `cors_headers` function like so:

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

