# -*- coding: utf-8 -*-

import logging

from thriftpy.rpc import make_server
from koenig import koenig_thrift

from koenig.dispatcher import (
    KoenigDispatcher,
)

from koenig.settings import (
    KOENIG_THRIFT_SETTINGS,
)


logger = logging.getLogger(__name__)


def server(host=None, port=None):
    host = host or KOENIG_THRIFT_SETTINGS['host']
    port = port or KOENIG_THRIFT_SETTINGS['port']
    return make_server(
        koenig_thrift.KoenigService,
        KoenigDispatcher(),
        host,
        port
    )

server().serve()
