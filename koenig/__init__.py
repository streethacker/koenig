# -*- coding: utf-8 -*-

import thriftpy
import contextlib

import os

koenig_thrift = thriftpy.load(
    os.path.join(os.path.dirname(__file__), 'koenig.thrift'),
    'koenig_thrift'
)

from logging import (
    config,
)

from koenig.settings import (
    LOGGING_SETTINGS,
)


config.dictConfig(LOGGING_SETTINGS)


from koenig.client import (
    client,
)


@contextlib.contextmanager
def koenig_client(host=None, port=None):
    yield client(host, port)
