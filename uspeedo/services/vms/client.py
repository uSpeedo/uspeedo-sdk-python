"""
Copyright 2024 USpeedo Technology Co., Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import typing

from uspeedo.core.client import Client
from uspeedo.services.vms.apis.SendMessageRequest import SendMessageRequest
from uspeedo.services.vms.apis.SendMessageResponse import SendMessageResponse


class VMSClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(VMSClient, self).__init__(config, transport, middleware, logger)
    
    def send_vms_message(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = SendMessageRequest().dumps(req)
        resp = self.invoke("SendVMSMessage", d, **kwargs)
        return SendMessageResponse().loads(resp)
