# -*- coding: utf-8 -*-

import logging
import psutil
import unittest

from test import TestBase, koenig_client
from koenig import koenig_thrift


logger = logging.getLogger(__name__)


class TestQuery(TestBase):

    def test_query_cpu_times(self):
        with koenig_client() as c:
            result = c.query_cpu_times()
            self.assertTrue(isinstance(result, koenig_thrift.TCPUTimes))

    def test_query_cpu_times_percpu(self):
        with koenig_client() as c:
            result = c.query_cpu_times_percpu()
            self.assertTrue(isinstance(result, list))

            for item in result:
                self.assertTrue(isinstance(item, koenig_thrift.TCPUTimes))

    def test_query_cpu_percent(self):
        with koenig_client() as c:
            result = c.query_cpu_percent()
            self.assertTrue(isinstance(result, float))

            result = c.query_cpu_percent(0.1)
            self.assertTrue(isinstance(result, float))

    def test_query_cpu_percent_percpu(self):
        with koenig_client() as c:
            result = c.query_cpu_percent_percpu()
            self.assertTrue(isinstance(result, list))
            for item in result:
                self.assertTrue(isinstance(item, float))

            result = c.query_cpu_percent_percpu(0.1)
            self.assertTrue(isinstance(result, list))
            for item in result:
                self.assertTrue(isinstance(item, float))

    def test_query_cpu_times_percent(self):
        with koenig_client() as c:
            result = c.query_cpu_times_percent()
            self.assertTrue(isinstance(result, koenig_thrift.TCPUTimesPercent))

            result = c.query_cpu_times_percent(0.1)
            self.assertTrue(isinstance(result, koenig_thrift.TCPUTimesPercent))

    def test_query_cpu_times_percent_percpu(self):
        with koenig_client() as c:
            result = c.query_cpu_times_percent_percpu()
            self.assertTrue(isinstance(result, list))
            for item in result:
                self.assertTrue(
                    isinstance(item, koenig_thrift.TCPUTimesPercent))

            result = c.query_cpu_times_percent_percpu(0.1)
            self.assertTrue(isinstance(result, list))
            for item in result:
                self.assertTrue(
                    isinstance(item, koenig_thrift.TCPUTimesPercent))

    def test_query_virtual_memory(self):
        with koenig_client() as c:
            result = c.query_virtual_memory()
            self.assertTrue(isinstance(result, koenig_thrift.TVirtualMemory))

    def test_query_swap_memory(self):
        with koenig_client() as c:
            result = c.query_swap_memory()
            self.assertTrue(isinstance(result, koenig_thrift.TSwapMemory))

    def test_query_disk_partitions(self):
        with koenig_client() as c:
            result = c.query_disk_partitions()
            self.assertTrue(isinstance(result, list))

            for item in result:
                self.assertTrue(
                    isinstance(item, koenig_thrift.TDiskPartition))

    def test_query_disk_io_counters(self):
        with koenig_client() as c:
            result = c.query_disk_io_counters()
            self.assertTrue(isinstance(result, koenig_thrift.TDiskIOCounters))

    def test_query_disk_io_counters_perdisk(self):
        with koenig_client() as c:
            result = c.query_disk_io_counters_perdisk()
            self.assertTrue(isinstance(result, dict))

            for item in result.values():
                self.assertTrue(
                    isinstance(item, koenig_thrift.TDiskIOCounters))

    def test_query_disk_usage(self):
        with koenig_client() as c:
            result = c.query_disk_usage('/')
            self.assertTrue(isinstance(result, koenig_thrift.TDiskUsage))

    def test_query_net_io_counters(self):
        with koenig_client() as c:
            result = c.query_net_io_counters()
            self.assertTrue(
                isinstance(result, koenig_thrift.TNetworkIOCounters))

    def test_query_net_io_counters_pernic(self):
        with koenig_client() as c:
            result = c.query_net_io_counters_pernic()
            self.assertTrue(isinstance(result, dict))

            for item in result.values():
                self.assertTrue(
                    isinstance(item, koenig_thrift.TNetworkIOCounters))

    def test_query_net_connections(self):
        with koenig_client() as c:
            result = c.query_net_connections()
            self.assertTrue(isinstance(result, list))

            for item in result:
                self.assertTrue(
                    isinstance(item, koenig_thrift.TNetworkConnections))

    def test_query_login_users(self):
        with koenig_client() as c:
            result = c.query_login_users()
            self.assertTrue(isinstance(result, list))

            for item in result:
                self.assertTrue(isinstance(item, koenig_thrift.TUser))

    def test_query_boot_time(self):
        with koenig_client() as c:
            result = c.query_boot_time()
            self.assertTrue(isinstance(result, (unicode, str)))

    def test_query_pids(self):
        with koenig_client() as c:
            result = c.query_pids()
            self.assertTrue(isinstance(result, list))

            for item in result:
                self.assertTrue(isinstance(item, int))

    def test_query_process_by_pid(self):
        pid = psutil.pids()[10]

        with koenig_client() as c:
            result = c.query_process_by_pid(pid)
            self.assertTrue(isinstance(result, koenig_thrift.TProcess))

    def test_query_processes_by_pids(self):
        pids = psutil.pids()

        with koenig_client() as c:
            result = c.query_processes_by_pids(pids)
            self.assertTrue(isinstance(result, dict))

            for item in result.values():
                self.assertTrue(isinstance(item, koenig_thrift.TProcess))

    def test_query_runtime_statistic(self):
        with koenig_client() as c:
            result = c.query_runtime_statistic()
            self.assertTrue(isinstance(result, list))

            for item in result:
                self.assertTrue(
                    isinstance(item, koenig_thrift.TRuntimeProfile))


if __name__ == '__main__':
    unittest.main()
