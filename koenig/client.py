# -*- coding: utf-8 -*-

from thriftpy.rpc import (
    make_client,
)

from koenig import (
    koenig_thrift,
)

from koenig.settings import (
    KOENIG_THRIFT_SETTINGS,
)


def client(host=None, port=None):
    host = host or KOENIG_THRIFT_SETTINGS['host']
    port = port or KOENIG_THRIFT_SETTINGS['port']

    return make_client(
        koenig_thrift.KoenigService,
        host,
        port
    )


if __name__ == '__main__':
    if client().ping():
        print 'server run ok'
