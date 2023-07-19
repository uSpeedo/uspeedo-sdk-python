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

from uspeedo.core.typesystem import schema, fields
from uspeedo.services.whatsapp.models.Client__MessageSummary import Client__MessageSummary


class Console__GetMessageSummaryResponse(schema.Schema):
    """ Console__GetMessageSummaryResponse - 
    """

    fields = {
        "MsgList": fields.List(Client__MessageSummary(), required=False, dump_to="MsgList", load_from="MsgList"),
        "MsgNum": fields.Int(required=False, dump_to="MsgNum", load_from="MsgNum"),
        "MsgAmount": fields.Int(required=False, dump_to="MsgAmount", load_from="MsgAmount"),
    }
