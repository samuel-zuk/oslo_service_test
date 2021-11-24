from oslo_service import service
from oslo_service import wsgi

from miniservice.conf import CONF

class WSGIService(service.ServiceBase):
    def __init__(self, name, app):
        self.name = name
        self.app = app
        self.workers = CONF[name].api_workers

        if self.workers and self.workers < 1:
            raise ValueError('api_workers value of %d is invalid, must be '
                             'greater than 0.' % self.workers)

        self.server = wsgi.Server(CONF, name, app,
                                  host=CONF[name].host_ip,
                                  port=CONF[name].port,
                                  use_ssl=CONF[name].use_ssl)

    def start(self):
        self.server.start()

    def stop(self):
        self.server.stop()

    def wait(self):
        self.server.wait()

    def reset(self):
        self.server.reset()
