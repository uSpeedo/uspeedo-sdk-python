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
from uspeedo.services.whatsapp.models.TemplateAttribute import TemplateAttribute
from uspeedo.services.whatsapp.models.TemplateComponentExample import TemplateComponentExample
from uspeedo.services.whatsapp.models.TemplateComponentButton import TemplateComponentButton
from uspeedo.services.whatsapp.models.TemplateComponent import TemplateComponent


class TemplateInfo(schema.Schema):
    """ TemplateInfo - 
    """

    fields = {
        "Category": fields.Str(required=False, dump_to="Category", load_from="Category"),
        "ID": fields.Str(required=False, dump_to="ID", load_from="ID"),
        "QualityScore":  TemplateQualityScore(required=False, dump_to="QualityScore", load_from="QualityScore"),
        "Status": fields.Str(required=False, dump_to="Status", load_from="Status"),
        "Tags": fields.List(fields.Str(required=False, dump_to="Tags", load_from="Tags")),
        "Attributes": fields.List(TemplateAttribute(), required=False, dump_to="Attributes", load_from="Attributes"),
        "Components": fields.List(TemplateComponent(), required=False, dump_to="Components", load_from="Components"),
        "Language": fields.Str(required=False, dump_to="Language", load_from="Language"),
        "Name": fields.Str(required=False, dump_to="Name", load_from="Name"),
        "RejectedReason": fields.Str(required=False, dump_to="RejectedReason", load_from="RejectedReason"),
    }
