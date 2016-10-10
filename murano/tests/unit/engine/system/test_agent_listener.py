#    Copyright (c) 2016 AT&T
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import tempfile

import mock
from oslo_serialization import base64
import yaml as yamllib

from murano.dsl import murano_object
from murano.dsl import murano_type
from murano.dsl import object_store
from murano.engine.system import agent_listener
from murano.engine.system import resource_manager
from murano.tests.unit import base


class TestExecutionPlan(base.MuranoTestCase):
    def setUp(self):
        super(TestExecutionPlan, self).setUp()
        name = "test"
        self.agent = agent_listener.AgentListener(name)
        self.addCleanup(mock.patch.stopall)

    def test_queue_name(self):
        self.assertEqual(self.agent._results_queue, self.agent.queue_name())

    @mock.patch("murano.engine.system.agent_listener.dsl.get_execution_session")
    def test_subscribe_unsubscribe(self, execution_session):
        self.agent.subscribe('msg_id', 'event')
        self.assertIn('msg_id', self.agent._subscriptions)
        self.agent.unsubscribe('msg_id')
        self.assertNotIn('msg_id', self.agent._subscriptions)
        self.assertTrue(execution_session.called)
