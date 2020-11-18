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
            self.cors_headers()
            if request.method != 'OPTIONS':
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
        response.headers['Access-Control-Allow-Origin'] = self._get_origin()
        response.headers['Access-Control-Allow-Methods'] = '\
            GET, POST, PUT, PATCH, OPTIONS, DELETE'
        response.headers['Access-Control-Allow-Headers'] = '\
            Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization'

    def _get_origin(self):
        '''
        Function dedicated to return origin if is on list
        '''
        client_origin = request.headers.get('Origin', None)
        if not client_origin or '*' in self.origins:
            return self.origins
        for origin in self.origins:
            if origin == client_origin:
                return origin
        return self.origins

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
    if not isinstance(origins, list):
        origins = [origins]
    cors_plugin_object.origins = origins
    return cors_plugin_object

abort = cors_plugin_object.abort
cors_headers = cors_plugin_object.cors_headers
