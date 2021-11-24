import logging
import sys

from oslo_service.service import ProcessLauncher

from miniservice.app import MiniserviceApplication
from miniservice import conf
from miniservice import service

CONF = conf.CONF
CONF(args=sys.argv[1:])

LOG = logging.getLogger()

def setup_logger():
    LOG.setLevel(logging.DEBUG)
    TermHandler = logging.StreamHandler(stream=sys.stdout)
    TermHandler.setLevel(logging.DEBUG)
    fmt = logging.Formatter(fmt='%(name)s: %(asctime)s [%(levelname)s] - '
                                '%(message)s')
    TermHandler.setFormatter(fmt)
    LOG.addHandler(TermHandler)


def main():
    setup_logger()

    server = service.WSGIService('miniservice', MiniserviceApplication())

    launcher = ProcessLauncher(CONF, restart_method='mutate')
    launcher.launch_service(server, workers=server.workers)
    launcher.wait()


if __name__ == '__main__':
    sys.exit(main())
