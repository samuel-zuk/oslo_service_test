from flask import Flask


def setup_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.get('/')
    def get_root():
        return 'bombus\n'

    return app.wsgi_app


class MiniserviceApplication(object):
    def __init__(self):
        self.app = setup_app()

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)
