from bottle import route, response, Bottle, request, HTTPError


class CorsPluginObject():

    name = 'cors'
    api = 2

    def __init__(self, origins="*"):
        """ Constructor function

            param: bottle
            ptype: Bottle class
            param: origin
            ptype: string or array
        """
        bottle = Bottle()
        bottle.cors = True
        self.origins = origins
        self.bottle = bottle
        self._options_route()

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            if request.method != 'OPTIONS':
                self.cors_headers()
                # actual request; reply with the actual response
                return fn(*args, **kwargs)
        return _enable_cors

    def _options_route(self):
        """ Function dedicated to add option route to the hole
            app with the route opject
        """
        route('/', method='OPTIONS', callback=self.options_function)
        route(
            '/<filepath:path>', method='OPTIONS', callback=self.options_function
        )

    def options_function(self):
        pass

    def cors_headers(self):
        """ Function dedicated to assing headers

            params: origins
            ptype: string or array of strings
        """
        response.headers['Access-Control-Allow-Origin'] = self.origins
        response.headers['Access-Control-Allow-Methods'] = '\
            GET, POST, PUT, PATCH, OPTIONS, DELETE'
        response.headers['Access-Control-Allow-Headers'] = '\
            Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization'

    def abort(self, code=500, text='Unknown Error.'):
        """ Aborts execution and causes a HTTP error. """
        self.cors_headers()
        headers = response.headers.dict
        headerlist = response.headerlist
        for name, value in headerlist:
            headers[name] = '%s' % (value.strip())
        raise HTTPError(code, text, headers=headers)


cors_plugin_object = CorsPluginObject()

def cors_plugin(origins="*"):
    cors_plugin_object.origins = origins
    return cors_plugin_object

abort = cors_plugin_object.abort
cors_headers = cors_plugin_object.cors_headers