# -*- coding: utf-8 -*-

import logging

from koenig.exc import (
    raise_user_exc,
    KoenigErrorCode,
)

logger = logging.getLogger(__name__)


def ping():
    return True
