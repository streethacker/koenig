# -*- coding: utf-8 -*-

import datetime
import psutil

import logging

from koenig.utils import datetime2utc

from koenig.utils.async import (
    send_task,
)

logger = logging.getLogger(__name__)


def ping():
    return True


def serialize_runtime_statistic():
    cpu_percent = psutil.cpu_percent(0.1)
    mem_percent = psutil.virtual_memory().percent
    profile_ts = datetime2utc(
        datetime.datetime.now().replace(second=0, microsecond=0))

    send_task('koenig', 'process_runtime_statistic', cpu_percent,
              mem_percent, profile_ts)
