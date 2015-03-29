# -*- coding: utf-8 -*-

import logging

from thriftpy.rpc import (
    make_server,
)

from koenig.dispatcher import (
    KoenigDispatcher,
)

from koenig import (
    koenig_thrift,
)

from koenig.settings import (
    KOENIG_THRIFT_SETTINGS,
)


logger = logging.getLogger(__name__)

server = make_server(
    koenig_thrift.KoenigService,
    KoenigDispatcher(),
    KOENIG_THRIFT_SETTINGS['host'],
    KOENIG_THRIFT_SETTINGS['port']
)

server.serve()
