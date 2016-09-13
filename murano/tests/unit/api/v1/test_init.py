import mock
from oslo_utils import timeutils

from murano.api.v1 import environments
from murano.api.v1 import sessions

from oslo_config import fixture as config_fixture
from oslo_serialization import jsonutils

from murano.db import session as db_session

from murano.api import v1
from murano.common import policy
from murano.db import models
import murano.tests.unit.api.base as tb
import murano.tests.unit.utils as test_utils


class TestInitApi(tb.ControllerTest, tb.MuranoApiTestCase):
    def setUp(self):
        super(TestInitApi, self).setUp()
        self.environments_controller = environments.Controller()
        self.sessions_controller = sessions.Controller()
	self.fixture = self.useFixture(config_fixture.Config())
        self.fixture.conf(args=[])

    def test_execute_action(self):
	session = db_session.get_session()
	
	environment = models.Environment(
            name='test_environment', tenant_id='test_tenant_id',
            version='v3', id='1234'
        )
	result = session.add(environment)
	print(dir(session))
