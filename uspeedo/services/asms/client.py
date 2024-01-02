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
from uspeedo.services.asms.apis.QueryUSMSTemplateReq import QueryUSMSTemplateReq
from uspeedo.services.asms.apis.QueryUSMSTemplateResp import QueryUSMSTemplateResp
from uspeedo.services.asms.apis.SendBatchUSMSMessageReq import SendBatchUSMSMessageReq
from uspeedo.services.asms.apis.SendBatchUSMSMessageResp import SendBatchUSMSMessageResp
from uspeedo.services.asms.apis.GetUSMSSendReceiptReq import GetUSMSSendReceiptReq
from uspeedo.services.asms.apis.GetUSMSSendReceiptResp import GetUSMSSendReceiptResp
from uspeedo.services.asms.apis.DeleteUSMSTemplateReq import DeleteUSMSTemplateReq
from uspeedo.services.asms.apis.DeleteUSMSTemplateResp import DeleteUSMSTemplateResp
from uspeedo.services.asms.apis.CreateUSMSTemplateReq import CreateUSMSTemplateReq
from uspeedo.services.asms.apis.CreateUSMSTemplateResp import CreateUSMSTemplateResp
from uspeedo.services.asms.apis.UpdateUSMSTemplateReq import UpdateUSMSTemplateReq
from uspeedo.services.asms.apis.UpdateUSMSTemplateResp import UpdateUSMSTemplateResp


class AsmsClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(AsmsClient, self).__init__(config, transport, middleware, logger)
    
    def get_usms_send_receipt(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetUSMSSendReceiptReq().dumps(req)
        resp = self.invoke("GetUSMSSendReceipt", d, **kwargs)
        return GetUSMSSendReceiptResp().loads(resp)
    
    def create_usms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = CreateUSMSTemplateReq().dumps(req)
        resp = self.invoke("CreateUSMSTemplate", d, **kwargs)
        return CreateUSMSTemplateResp().loads(resp)
    
    def delete_usms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = DeleteUSMSTemplateReq().dumps(req)
        resp = self.invoke("DeleteUSMSTemplate", d, **kwargs)
        return DeleteUSMSTemplateResp().loads(resp)
    
    def update_usms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = UpdateUSMSTemplateReq().dumps(req)
        resp = self.invoke("UpdateUSMSTemplate", d, **kwargs)
        return UpdateUSMSTemplateResp().loads(resp)
    
    def send_batch_usms_message(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = SendBatchUSMSMessageReq().dumps(req)
        resp = self.invoke("SendBatchUSMSMessage", d, **kwargs)
        return SendBatchUSMSMessageResp().loads(resp)
    
    def query_usms_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = QueryUSMSTemplateReq().dumps(req)
        resp = self.invoke("QueryUSMSTemplate", d, **kwargs)
        return QueryUSMSTemplateResp().loads(resp)
