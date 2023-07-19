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
from uspeedo.services.whatsapp.models.Console__Component import Console__Component
from uspeedo.services.whatsapp.models.Console__Button import Console__Button
from uspeedo.services.whatsapp.models.Console__Example import Console__Example
from uspeedo.services.whatsapp.models.Console__TemplateInfo import Console__TemplateInfo
from uspeedo.services.whatsapp.models.Console__QualityScore import Console__QualityScore
from uspeedo.services.whatsapp.models.Console__Cursors import Console__Cursors
from uspeedo.services.whatsapp.models.Console__Paging import Console__Paging
from uspeedo.services.whatsapp.models.Console__GetTemplatesResponse import Console__GetTemplatesResponse


class Console__data_console_GetTemplatesResponse(schema.ResponseSchema):

    """ Console__data_console_GetTemplatesResponse - 
    """

    fields = {
        "Data":  Console__GetTemplatesResponse(required=False, dump_to="Data", load_from="Data"),
    }
