# -*- coding: utf-8 -*-

import psutil
import logging

from datetime import (
    datetime,
)

from psutil import (
    AccessDenied,
)

from koenig import (
    koenig_thrift,
)

from koenig.exc import (
    raise_user_exc,
    KoenigErrorCode,
)

from koenig.utils import (
    serialize_to_ttype,
    serialize_to_ttype_list,
    serialize_to_ttype_dict,
)


logger = logging.getLogger(__name__)


def query_cpu_times():
    cpu_times = psutil.cpu_times()
    return serialize_to_ttype(cpu_times, koenig_thrift.TCpuTimes)


def query_cpu_times_percpu():
    cpu_times_percpu = psutil.cpu_times(percpu=True)
    return serialize_to_ttype_list(cpu_times_percpu, koenig_thrift.TCpuTimes)


def query_cpu_percent(interval):
    cpu_percent = psutil.cpu_percent(interval)
    return cpu_percent


def query_cpu_percent_percpu(interval):
    cpu_percent_percpu = psutil.cpu_percent(interval, percpu=True)
    return cpu_percent_percpu


def query_cpu_times_percent(interval):
    cpu_times_percent = psutil.cpu_times_percent()
    return serialize_to_ttype(
        cpu_times_percent,
        koenig_thrift.TCpuTimesPercent
    )


def query_cpu_times_percent_percpu(interval):
    cpu_times_percent_percpu = psutil.cpu_times_percent(percpu=True)
    return serialize_to_ttype_list(
        cpu_times_percent_percpu,
        koenig_thrift.TCpuTimesPercent
    )


def query_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    return serialize_to_ttype(virtual_memory, koenig_thrift.TVirtualMemory)


def query_swap_memory():
    swap_memory = psutil.swap_memory()
    return serialize_to_ttype(swap_memory, koenig_thrift.TSwapMemory)


def query_disk_partitions():
    disk_partitions = psutil.disk_partitions()
    return serialize_to_ttype_list(
        disk_partitions,
        koenig_thrift.TDiskPartition
    )


def query_disk_io_counters():
    disk_io_counters = psutil.disk_io_counters()
    return serialize_to_ttype(disk_io_counters, koenig_thrift.TDiskIOCounters)


def query_disk_io_counters_perdisk():
    disk_io_counters_perdisk = psutil.disk_io_counters(perdisk=True)
    return serialize_to_ttype_dict(
        disk_io_counters_perdisk,
        koenig_thrift.TDiskIOCounters
    )


def query_disk_usage(path):
    disk_usage = psutil.disk_usage(path)
    return serialize_to_ttype(disk_usage, koenig_thrift.TDiskUsage)


def query_net_io_counters():
    net_io_counters = psutil.net_io_counters()
    return serialize_to_ttype(
        net_io_counters,
        koenig_thrift.TNetworkIOCounters
    )


def query_net_io_counters_pernic():
    net_io_counters_pernic = psutil.net_io_counters(pernic=True)
    return serialize_to_ttype_dict(
        net_io_counters_pernic,
        koenig_thrift.TNetworkIOCounters
    )


def query_net_connections():
    try:
        net_connections = psutil.net_connections()
    except AccessDenied:
        raise_user_exc(KoenigErrorCode.ACCESS_DENIED)

    return serialize_to_ttype_list(
        net_connections,
        koenig_thrift.TNetworkConnections
    )


def query_login_users():
    login_users = psutil.users()
    return serialize_to_ttype_list(login_users, koenig_thrift.TUser)


def query_boot_time():
    boot_time = psutil.boot_time()
    return datetime.fromtimestamp(boot_time).strftime('%Y-%m-%d %H:%M:%S')


def query_pids():
    return psutil.pids()
