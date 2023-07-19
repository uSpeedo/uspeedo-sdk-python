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
from uspeedo.services.whatsapp.models.Console__getAccountPhoneListResponseItem import Console__getAccountPhoneListResponseItem
from uspeedo.services.whatsapp.models.Console__getAccountAppKeyResponse import Console__getAccountAppKeyResponse


class Console__data_console_getAccountAppKeyResponse(schema.ResponseSchema):

    """ Console__data_console_getAccountAppKeyResponse - 
    """

    fields = {
        "Data":  Console__getAccountAppKeyResponse(required=False, dump_to="Data", load_from="Data"),
    }