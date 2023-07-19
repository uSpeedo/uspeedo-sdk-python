"""
Copyright 2023 USpeedo Technology Co., Ltd.

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
from uspeedo.services.whatsapp.apis.Console__uploadMediaRequest import Console__uploadMediaRequest
from uspeedo.services.whatsapp.apis.Console__data_console_uploadMediaResponse import Console__data_console_uploadMediaResponse
from uspeedo.services.whatsapp.apis.Console__deleteTemplateRequest import Console__deleteTemplateRequest
from uspeedo.services.whatsapp.apis.Common__Empty import Common__Empty
from uspeedo.services.whatsapp.apis.Console__sendMessageRequest import Console__sendMessageRequest
from uspeedo.services.whatsapp.apis.Console__data_console_sendMessageResponse import Console__data_console_sendMessageResponse
from uspeedo.services.whatsapp.apis.Client__GetMessageSummaryRequest import Client__GetMessageSummaryRequest
from uspeedo.services.whatsapp.apis.Console__data_console_GetMessageSummaryResponse import Console__data_console_GetMessageSummaryResponse
from uspeedo.services.whatsapp.apis.Console__deleteMediaRequest import Console__deleteMediaRequest
from uspeedo.services.whatsapp.apis.Common__Empty import Common__Empty
from uspeedo.services.whatsapp.apis.Console__getMediaRequest import Console__getMediaRequest
from uspeedo.services.whatsapp.apis.Console__data_console_getMediaResponse import Console__data_console_getMediaResponse
from uspeedo.services.whatsapp.apis.Console__getTemplateRequest import Console__getTemplateRequest
from uspeedo.services.whatsapp.apis.Console__data_console_GetTemplatesResponse import Console__data_console_GetTemplatesResponse
from uspeedo.services.whatsapp.apis.GetAccountPhoneListRequest import GetAccountPhoneListRequest
from uspeedo.services.whatsapp.apis.Console__data_console_getAccountAppKeyResponse import Console__data_console_getAccountAppKeyResponse


class WhatsAppClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(WhatsAppClient, self).__init__(config, transport, middleware, logger)
    
    def upload_media(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Console__uploadMediaRequest().dumps(req)
        resp = self.invoke("UploadMedia", d, **kwargs)
        return Console__data_console_uploadMediaResponse().loads(resp)
    
    def delete_template(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Console__deleteTemplateRequest().dumps(req)
        resp = self.invoke("DeleteTemplate", d, **kwargs)
        return Common__Empty().loads(resp)
    
    def send_whatsapp_message(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Console__sendMessageRequest().dumps(req)
        resp = self.invoke("SendWhatsappMessage", d, **kwargs)
        return Console__data_console_sendMessageResponse().loads(resp)
    
    def get_message_summary(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Client__GetMessageSummaryRequest().dumps(req)
        resp = self.invoke("GetMessageSummary", d, **kwargs)
        return Console__data_console_GetMessageSummaryResponse().loads(resp)
    
    def get_templates(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Console__getTemplateRequest().dumps(req)
        resp = self.invoke("GetTemplates", d, **kwargs)
        return Console__data_console_GetTemplatesResponse().loads(resp)
    
    def delete_media(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Console__deleteMediaRequest().dumps(req)
        resp = self.invoke("DeleteMedia", d, **kwargs)
        return Common__Empty().loads(resp)
    
    def get_media(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = Console__getMediaRequest().dumps(req)
        resp = self.invoke("GetMedia", d, **kwargs)
        return Console__data_console_getMediaResponse().loads(resp)
    
    def get_account_phone_list(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        d = GetAccountPhoneListRequest().dumps(req)
        resp = self.invoke("GetAccountPhoneList", d, **kwargs)
        return Console__data_console_getAccountAppKeyResponse().loads(resp)
