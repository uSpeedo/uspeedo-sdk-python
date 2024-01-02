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
from uspeedo.services.whatsapp.apis.DeleteTemplateReq import DeleteTemplateReq
from uspeedo.services.whatsapp.apis.DeleteTemplateRes import DeleteTemplateRes
from uspeedo.services.whatsapp.apis.DeleteMediaReq import DeleteMediaReq
from uspeedo.services.whatsapp.apis.DeleteMediaRes import DeleteMediaRes
from uspeedo.services.whatsapp.apis.GetMediaReq import GetMediaReq
from uspeedo.services.whatsapp.apis.GetMediaResData import GetMediaResData
from uspeedo.services.whatsapp.apis.SendWhatsappMessageReq import SendWhatsappMessageReq
from uspeedo.services.whatsapp.apis.SendWhatsappMessageResData import SendWhatsappMessageResData
from uspeedo.services.whatsapp.apis.GetMessageSummaryReq import GetMessageSummaryReq
from uspeedo.services.whatsapp.apis.GetMessageSummaryResData import GetMessageSummaryResData
from uspeedo.services.whatsapp.apis.GetAccountPhoneListRequest import GetAccountPhoneListRequest
from uspeedo.services.whatsapp.apis.GetAccountPhoneListResData import GetAccountPhoneListResData
from uspeedo.services.whatsapp.apis.UploadMediaReq import UploadMediaReq
from uspeedo.services.whatsapp.apis.UploadMediaResData import UploadMediaResData
from uspeedo.services.whatsapp.apis.GetTemplatesReq import GetTemplatesReq
from uspeedo.services.whatsapp.apis.GetTemplatesResData import GetTemplatesResData


class WhatsAppClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(WhatsAppClient, self).__init__(config, transport, middleware, logger)
    
    def upload_media(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = UploadMediaReq().dumps(req)
        resp = self.invoke("UploadMedia", d, **kwargs)
        return UploadMediaResData().loads(resp)
    
    def get_templates(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetTemplatesReq().dumps(req)
        resp = self.invoke("GetTemplates", d, **kwargs)
        return GetTemplatesResData().loads(resp)
    
    def delete_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = DeleteTemplateReq().dumps(req)
        resp = self.invoke("DeleteTemplate", d, **kwargs)
        return DeleteTemplateRes().loads(resp)
    
    def delete_media(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = DeleteMediaReq().dumps(req)
        resp = self.invoke("DeleteMedia", d, **kwargs)
        return DeleteMediaRes().loads(resp)
    
    def get_media(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetMediaReq().dumps(req)
        resp = self.invoke("GetMedia", d, **kwargs)
        return GetMediaResData().loads(resp)
    
    def send_whatsapp_message(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = SendWhatsappMessageReq().dumps(req)
        resp = self.invoke("SendWhatsappMessage", d, **kwargs)
        return SendWhatsappMessageResData().loads(resp)
    
    def get_message_summary(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetMessageSummaryReq().dumps(req)
        resp = self.invoke("GetMessageSummary", d, **kwargs)
        return GetMessageSummaryResData().loads(resp)
    
    def get_account_phone_list(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetAccountPhoneListRequest().dumps(req)
        resp = self.invoke("GetAccountPhoneList", d, **kwargs)
        return GetAccountPhoneListResData().loads(resp)
