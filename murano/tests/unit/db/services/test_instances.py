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

#from oslo_utils import timeutils

#from murano.db import models
#from murano.db import session as db_session
from murano.tests.unit import base
from murano.tests.unit import utils

#from murano.db.services import instances


class TestInstanceStatsServices(base.MuranoWithDBTestCase):
    def setUp(self):
        super(TestInstanceStatsServices, self).setUp()
        self.context = utils.dummy_context(tenant_id=self.tenant_id)

        self.context_admin = utils.dummy_context(tenant_id=self.tenant_id)
        self.context_admin.is_admin = True
#
#    def test_track_instance(self):
