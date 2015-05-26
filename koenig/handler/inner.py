# -*- coding: utf-8 -*-

import logging

from koenig.utils import (
    profile_,
    utc2datetime,
)

from koenig.models import (
    db_commit,
    RuntimeProfile,
)


logger = logging.getLogger(__name__)


@db_commit
@profile_
def process_runtime_statistic(cpu_percent, mem_percent,
                              profile_ts):

    profile_ts = utc2datetime(profile_ts)
    RuntimeProfile.new(
        cpu_percent=cpu_percent,
        mem_percent=mem_percent,
        profile_ts=profile_ts
    )
