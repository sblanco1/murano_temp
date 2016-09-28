# Copyright (c) 2017 AT&T
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import mock

from murano.engine import execution_session

from murano.tests.unit import base


class TestExecutionSession(base.MuranoTestCase):
    def setUp(self):
        super(TestExecutionSession, self).setUp()
        self.execution_session = execution_session.ExecutionSession()

    def test_start(self):
        delegate = "test"
        self.execution_session.on_session_start(delegate)
        self.assertEqual(self.execution_session._set_up_list, ["test"])
        self.execution_session.start()
        self.assertEqual(self.execution_session._set_up_list, [])

    def test_finish(self):
        delegate = "test"
        self.execution_session.on_session_finish(delegate)
        self.assertEqual(self.execution_session._tear_down_list, ["test"])
        self.execution_session.finish()
        self.assertEqual(self.execution_session._tear_down_list, [])
