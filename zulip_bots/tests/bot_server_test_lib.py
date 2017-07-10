from unittest import TestCase
import server.bot_server
import json
from typing import Any, List, Dict, Mapping

class BotServerTestCase(TestCase):

    def setUp(self):
        # type: () -> None
        server.bot_server.app.testing = True
        self.app = server.bot_server.app.test_client()

    def assert_bot_server_response(self,
                                   available_bots=None,
                                   bots_config=None,
                                   bots_lib_module=None,
                                   payload_url="/bots/testbot",
                                   message=dict(message={'key': "test message"}),
                                   check_success=False,
                                   ):
        # type: (List[str], Dict[str, Any], Dict[str, Any], str, Dict[str, Dict[str, Any]], bool) -> None

        if available_bots is not None:
            server.bot_server.available_bots = available_bots

        if bots_config is not None:
            server.bot_server.bots_config = bots_config

        if bots_lib_module is not None:
            server.bot_server.bots_lib_module = bots_lib_module

        response = self.app.post(payload_url, data=json.dumps(message))

        if check_success:
            assert response.status_code >= 200 and response.status_code < 300
        else:
            assert response.status_code >= 400 and response.status_code < 500
