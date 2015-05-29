# -*- coding: utf-8 -*-

import logging
import unittest

from thriftpy.rpc import client_context
from koenig import koenig_thrift

logger = logging.getLogger(__name__)


def make_client(service, name):
    return client_context(service, 'localhost', '27028')


def koenig_client():
    return make_client(koenig_thrift.KoenigService, 'koenig')


class TestBase(unittest.TestCase):
    pass
