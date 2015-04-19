# -*- coding: utf-8 -*-

import psutil
import logging

from datetime import (
    datetime,
)

from psutil import (
    AccessDenied,
    NoSuchProcess,
)

from koenig import (
    koenig_thrift,
)

from koenig.exc import (
    raise_user_exc,
    raise_system_exc,
    KoenigErrorCode,
)

from koenig.utils import (
    serialize,
)


logger = logging.getLogger(__name__)


def __extend_process(process):
    attrs = {
        'pid': process.pid,
        'ppid': process.ppid(),
        'name': process.name(),
        'username': process.username(),
        'create_time': process.create_time(),
        'cpu_percent': process.cpu_percent(),
        'memory_percent': process.memory_percent(),
        'cwd': process.cwd(),
        'status': process.status(),
    }

    try:
        attrs['exe'] = process.exe()
    except AccessDenied:
        if attrs['pid'] == koenig_thrift.KERNEL_TASK_PID:
            attrs['exe'] = 'kernel task not support'
            logger.info('hit kernel task: [PID:{}]'.format(attrs['pid']))
        else:
            raise_user_exc(KoenigErrorCode.ACCESS_DENIED)

    attrs['uids'] = serialize(process.uids(), koenig_thrift.TProcessUID)
    attrs['gids'] = serialize(process.gids(), koenig_thrift.TProcessGID)

    process.__dict__.clear()
    process.__dict__.update(attrs)

    return process


def query_cpu_times():
    cpu_times = psutil.cpu_times()
    return serialize(cpu_times, koenig_thrift.TCPUTimes)


def query_cpu_times_percpu():
    cpu_times_percpu = psutil.cpu_times(percpu=True)
    return serialize(cpu_times_percpu, koenig_thrift.TCPUTimes, _list=True)


def query_cpu_percent(interval):
    cpu_percent = psutil.cpu_percent(interval)
    return cpu_percent


def query_cpu_percent_percpu(interval):
    cpu_percent_percpu = psutil.cpu_percent(interval, percpu=True)
    return cpu_percent_percpu


def query_cpu_times_percent(interval):
    cpu_times_percent = psutil.cpu_times_percent()
    return serialize(
        cpu_times_percent,
        koenig_thrift.TCPUTimesPercent
    )


def query_cpu_times_percent_percpu(interval):
    cpu_times_percent_percpu = psutil.cpu_times_percent(percpu=True)
    return serialize(
        cpu_times_percent_percpu,
        koenig_thrift.TCPUTimesPercent,
        _list=True
    )


def query_virtual_memory():
    virtual_memory = psutil.virtual_memory()
    return serialize(virtual_memory, koenig_thrift.TVirtualMemory)


def query_swap_memory():
    swap_memory = psutil.swap_memory()
    return serialize(swap_memory, koenig_thrift.TSwapMemory)


def query_disk_partitions():
    disk_partitions = psutil.disk_partitions()
    return serialize(
        disk_partitions,
        koenig_thrift.TDiskPartition,
        _list=True
    )


def query_disk_io_counters():
    disk_io_counters = psutil.disk_io_counters()
    return serialize(disk_io_counters, koenig_thrift.TDiskIOCounters)


def query_disk_io_counters_perdisk():
    disk_io_counters_perdisk = psutil.disk_io_counters(perdisk=True)
    return serialize(
        disk_io_counters_perdisk,
        koenig_thrift.TDiskIOCounters,
        _map=True
    )


def query_disk_usage(path):
    try:
        disk_usage = psutil.disk_usage(path)
    except OSError:
        raise_user_exc(KoenigErrorCode.DISK_PATH_NOT_FOUND)

    return serialize(disk_usage, koenig_thrift.TDiskUsage)


def query_net_io_counters():
    net_io_counters = psutil.net_io_counters()
    return serialize(
        net_io_counters,
        koenig_thrift.TNetworkIOCounters
    )


def query_net_io_counters_pernic():
    net_io_counters_pernic = psutil.net_io_counters(pernic=True)
    return serialize(
        net_io_counters_pernic,
        koenig_thrift.TNetworkIOCounters,
        _map=True
    )


def query_net_connections():
    try:
        net_connections = psutil.net_connections()
    except AccessDenied:
        raise_user_exc(KoenigErrorCode.ACCESS_DENIED)

    return serialize(
        net_connections,
        koenig_thrift.TNetworkConnections,
        _list=True
    )


def query_login_users():
    login_users = psutil.users()
    return serialize(login_users, koenig_thrift.TUser, _list=True)


def query_boot_time():
    boot_time = psutil.boot_time()
    return datetime.fromtimestamp(boot_time).strftime('%Y-%m-%d %H:%M:%S')


def query_pids():
    return psutil.pids()


def query_process_by_pid(pid):

    try:
        process = psutil.Process(pid)
    except AccessDenied:
        raise_user_exc(KoenigErrorCode.ACCESS_DENIED)
    except NoSuchProcess:
        raise_system_exc(KoenigErrorCode.PROCESS_NOT_FOUND)

    process = __extend_process(process)

    return serialize(process, koenig_thrift.TProcess)


def query_processes_by_pids(pids):

    def __gen_process(pids):
        for pid in pids:
            try:
                process = psutil.Process(pid)
            except AccessDenied:
                raise_user_exc(KoenigErrorCode.ACCESS_DENIED)
            except NoSuchProcess:
                raise_system_exc(KoenigErrorCode.PROCESS_NOT_FOUND)

            process = __extend_process(process)

            yield (pid, process)

    result = {}
    for pid, process in __gen_process(pids):
        result.update({pid: process})

    return serialize(result, koenig_thrift.TProcess, _map=True)
