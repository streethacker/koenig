# -*- coding: utf-8 -*-

from thriftpy.rpc import client_context
from koenig import koenig_thrift

from koenig.settings import (
    KOENIG_THRIFT_SETTINGS,
)


def make_client(host=None, port=None):
    host = host or KOENIG_THRIFT_SETTINGS['host']
    port = port or KOENIG_THRIFT_SETTINGS['port']

    return client_context(
        koenig_thrift.KoenigService,
        host,
        port
    )


if __name__ == '__main__':
    if make_client().ping():
        print 'server run ok'
