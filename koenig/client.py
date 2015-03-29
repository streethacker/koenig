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


def client():
    return make_client(
        koenig_thrift.KoenigService,
        KOENIG_THRIFT_SETTINGS['host'],
        KOENIG_THRIFT_SETTINGS['port']
    )


if __name__ == '__main__':
    if client().ping():
        print 'server run ok'
