# -*- coding: utf-8 -*-

import logging

from koenig.handler import (
    base,
)

logger = logging.getLogger(__name__)


class KoenigDispatcher(object):

    def __init__(self):
        logger.info('koenig server starting...')

    ###############
    # BASE APIs
    ###############

    def ping(self):
        return base.ping()
