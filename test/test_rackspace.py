# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import sys
import os
import unittest
import httplib
from os.path import join as pjoin

from rackspace_monitoring.base import (MonitoringDriver, Entity,
                                      NotificationPlan,
                                      Notification, CheckType, Alarm, Check,
                                      AlarmChangelog)
from rackspace_monitoring.drivers.rackspace import RackspaceMonitoringDriver

from test import MockResponse, MockHttpTestCase, XML_HEADERS
from test.file_fixtures import FIXTURES_ROOT
from test.file_fixtures import FileFixtures, OpenStackFixtures
from secrets import RACKSPACE_PARAMS

FIXTURES_ROOT['monitoring'] = pjoin(os.getcwd(), 'test/fixtures')

class MonitoringFileFixtures(FileFixtures):
    def __init__(self, sub_dir=''):
        super(MonitoringFileFixtures, self).__init__(fixtures_type='monitoring',
                                                     sub_dir=sub_dir)

class RackspaceTests(unittest.TestCase):
    def setUp(self):
        RackspaceMonitoringDriver.connectionCls.conn_classes = (RackspaceMockHttp,
                                                                RackspaceMockHttp)
        RackspaceMonitoringDriver.connectionCls.auth_url = "https://auth.api.example.com/v1.1/"
        RackspaceMockHttp.type = None
        self.driver = RackspaceMonitoringDriver(*RACKSPACE_PARAMS,
                ex_force_base_url='http://www.todo.com')

    def test_list_monitoring_zones(self):
        result = list(self.driver.list_monitoring_zones())
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 'mzxJ4L2IU')

    def test_list_entities(self):
        result = list(self.driver.list_entities())
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0].id, 'en8B9YwUn6')
        self.assertEqual(result[0].label, 'bar')

    def test_list_check_types(self):
        result = list(self.driver.list_check_types())
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].id, 'remote.dns')
        self.assertTrue(result[0].is_remote)

    def test_list_notification_types(self):
        result = list(self.driver.list_notification_types())
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 'webhook')

    def test_list_notifications(self):
        result = list(self.driver.list_notifications())
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].type, 'webhook')
        self.assertEqual(result[0].details['url'], 'http://www.postbin.org/lulz')

    def test_list_notification_plans(self):
        result = list(self.driver.list_notification_plans())
        self.assertEqual(len(result), 8)
        self.assertEqual(result[0].label, 'test-notification-plan')


class RackspaceMockHttp(MockHttpTestCase):
    auth_fixtures = MonitoringFileFixtures('rackspace/auth')
    fixtures = MonitoringFileFixtures('rackspace/v1.0')
    json_content_headers = {'content-type': 'application/json; charset=UTF-8'}

    def _v2_0_tokens(self, method, url, body, headers):
        body = self.auth_fixtures.load('_v2_0_tokens.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])

    def _23213_monitoring_zones(self, method, url, body, headers):
        body = self.fixtures.load('monitoring_zones.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])

    def _23213_entities(self, method, url, body, headers):
        body = self.fixtures.load('entities.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])

    def _23213_check_types(self, method, url, body, headers):
        body = self.fixtures.load('check_types.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])

    def _23213_notification_types(self, method, url, body, headers):
        body = self.fixtures.load('notification_types.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])

    def _23213_notifications(self, method, url, body, headers):
        body = self.fixtures.load('notifications.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])

    def _23213_notification_plans(self, method, url, body, headers):
        body = self.fixtures.load('notification_plans.json')
        return (httplib.OK, body, self.json_content_headers, httplib.responses[httplib.OK])


if __name__ == '__main__':
    sys.exit(unittest.main())
