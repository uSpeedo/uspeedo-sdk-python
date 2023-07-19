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
from uspeedo.services.whatsapp.models.Console__Button import Console__Button
from uspeedo.services.whatsapp.models.Console__Example import Console__Example
from uspeedo.services.whatsapp.models.Console__Component import Console__Component
from uspeedo.services.whatsapp.models.Console__QualityScore import Console__QualityScore


class Console__TemplateInfo(schema.Schema):
    """ Console__TemplateInfo - 
    """

    fields = {
        "Status": fields.Str(required=False, dump_to="Status", load_from="Status"),
        "Category": fields.Str(required=False, dump_to="Category", load_from="Category"),
        "Language": fields.Str(required=False, dump_to="Language", load_from="Language"),
        "RejectedReason": fields.Str(required=False, dump_to="RejectedReason", load_from="RejectedReason"),
        "QualityScore":  Console__QualityScore(required=False, dump_to="QualityScore", load_from="QualityScore"),
        "Tags": fields.List(fields.Str(required=False, dump_to="Tags", load_from="Tags")),
        "Components": fields.List(Console__Component(), required=False, dump_to="Components", load_from="Components"),
        "ID": fields.Str(required=False, dump_to="ID", load_from="ID"),
        "Name": fields.Str(required=False, dump_to="Name", load_from="Name"),
    }
