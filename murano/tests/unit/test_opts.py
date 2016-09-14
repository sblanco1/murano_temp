# Copyright (c) 2016 AT&T
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy

import mock
from oslo_config import cfg

from murano import opts
from murano.tests.unit import base


class TestOpts(base.MuranoTestCase):
    def setUp(self):
        super(TestOpts, self).setUp()
        self.addCleanup(mock.patch.stopall)

    def test_list_opts(self):
        self.assertEqual(opts.list_opts(),
            [(g, copy.deepcopy(o)) for g, o in opts._opt_lists])

    def test_list_cfapi_opts(self):
        self.assertEqual(opts.list_cfapi_opts(),
            [(g, copy.deepcopy(o)) for g, o in opts._cfapi_opt_lists])
