from oslo_config import cfg

CONF = cfg.CONF

miniservice_opts = [
    cfg.IntOpt('api_workers',
               default=1,
               help='Maximum number of workers for this service'),
    cfg.HostAddressOpt('host_ip',
                       default='0.0.0.0',
                       help='The IP address or hostname on which this service '
                            'listens.'),
    cfg.PortOpt('port',
                default=12345,
                help='The TCP port on which this service listens.'),
    cfg.BoolOpt('use_ssl',
                default=False,
                help='Whether or not this server should use SSL.')

]

CONF.register_opts(miniservice_opts, group='miniservice')
