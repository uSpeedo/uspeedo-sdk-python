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
from uspeedo.services.mms.apis.UpdateMMSTemplateReq import UpdateMMSTemplateReq
from uspeedo.services.mms.apis.UpdateMMSTemplateRes import UpdateMMSTemplateRes
from uspeedo.services.mms.apis.CreateMMSTemplateReq import CreateMMSTemplateReq
from uspeedo.services.mms.apis.CreateMMSTemplateRes import CreateMMSTemplateRes
from uspeedo.services.mms.apis.DeleteMMSTemplateReq import DeleteMMSTemplateReq
from uspeedo.services.mms.apis.DeleteMMSTemplateRes import DeleteMMSTemplateRes
from uspeedo.services.mms.apis.QueryMMSTemplateReq import QueryMMSTemplateReq
from uspeedo.services.mms.apis.QueryMMSTemplateRes import QueryMMSTemplateRes
from uspeedo.services.mms.apis.GetMMSSendReceiptReq import GetMMSSendReceiptReq
from uspeedo.services.mms.apis.GetMMSSendReceiptRes import GetMMSSendReceiptRes
from uspeedo.services.mms.apis.SendBatchMMSMessageReq import SendBatchMMSMessageReq
from uspeedo.services.mms.apis.SendBatchMMSMessageRes import SendBatchMMSMessageRes


class MMSClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(MMSClient, self).__init__(config, transport, middleware, logger)
    
    def get_mms_send_receipt(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetMMSSendReceiptReq().dumps(req)
        resp = self.invoke("GetMMSSendReceipt", d, **kwargs)
        return GetMMSSendReceiptRes().loads(resp)
    
    def send_batch_mms_message(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = SendBatchMMSMessageReq().dumps(req)
        resp = self.invoke("SendBatchMMSMessage", d, **kwargs)
        return SendBatchMMSMessageRes().loads(resp)
    
    def update_mms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = UpdateMMSTemplateReq().dumps(req)
        resp = self.invoke("UpdateMMSTemplate", d, **kwargs)
        return UpdateMMSTemplateRes().loads(resp)
    
    def create_mms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = CreateMMSTemplateReq().dumps(req)
        resp = self.invoke("CreateMMSTemplate", d, **kwargs)
        return CreateMMSTemplateRes().loads(resp)
    
    def delete_mms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = DeleteMMSTemplateReq().dumps(req)
        resp = self.invoke("DeleteMMSTemplate", d, **kwargs)
        return DeleteMMSTemplateRes().loads(resp)
    
    def query_mms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = QueryMMSTemplateReq().dumps(req)
        resp = self.invoke("QueryMMSTemplate", d, **kwargs)
        return QueryMMSTemplateRes().loads(resp)
