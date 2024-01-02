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

from uspeedo.core.typesystem import schema, fields
from uspeedo.services.whatsapp.models.TemplateQualityScore import TemplateQualityScore
from uspeedo.services.whatsapp.models.TemplateComponentExample import TemplateComponentExample
from uspeedo.services.whatsapp.models.TemplateComponentButton import TemplateComponentButton
from uspeedo.services.whatsapp.models.TemplateInfo import TemplateInfo
from uspeedo.services.whatsapp.models.TemplateAttribute import TemplateAttribute
from uspeedo.services.whatsapp.models.TemplateComponent import TemplateComponent
from uspeedo.services.whatsapp.models.GetTemplatesCursors import GetTemplatesCursors
from uspeedo.services.whatsapp.models.GetTemplatesPaging import GetTemplatesPaging


class GetTemplatesRes(schema.Schema):
    """ GetTemplatesRes - 
    """

    fields = {
        "Data": fields.List(TemplateInfo(), required=False, dump_to="Data", load_from="Data"),
        "Paging":  GetTemplatesPaging(required=False, dump_to="Paging", load_from="Paging"),
    }
