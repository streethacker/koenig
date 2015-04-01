# -*- coding: utf-8 -*-

import logging

from koenig.handler import (
    base,
    query,
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

    ###############
    # Query APIs
    ###############

    ################
    # query cpu info
    ################

    def query_cpu_times(self):
        return query.query_cpu_times()

    def query_cpu_times_percpu(self):
        return query.query_cpu_times_percpu()

    def query_cpu_percent(self, interval):
        return query.query_cpu_percent(interval)

    def query_cpu_percent_percpu(self, interval):
        return query.query_cpu_percent_percpu(interval)

    def query_cpu_times_percent(self, interval):
        return query.query_cpu_times_percent(interval)

    def query_cpu_times_percent_percpu(self, interval):
        return query.query_cpu_times_percent_percpu(interval)

    ####################
    # query memory info
    ####################

    def query_virtual_memory(self):
        return query.query_virtual_memory()

    def query_swap_memory(self):
        return query.query_swap_memory()

    #################
    # query disk info
    #################

    def query_disk_partitions(self):
        return query.query_disk_partitions()

    def query_disk_io_counters(self):
        return query.query_disk_io_counters()

    def query_disk_io_counters_perdisk(self):
        return query.query_disk_io_counters_perdisk()

    def query_disk_usage(self, path):
        return query.query_disk_usage(path)

    #####################
    # query network info
    #####################

    def query_net_io_counters(self):
        return query.query_net_io_counters()

    def query_net_io_counters_pernic(self):
        return query.query_net_io_counters_pernic()

    def query_net_connections(self):
        return query.query_net_connections()

    #################
    # query user info
    #################
    def query_login_users(self):
        return query.query_login_users()
