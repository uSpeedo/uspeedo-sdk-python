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
from uspeedo.services.asms.models.VariableAttr import VariableAttr


class OutTemplate(schema.Schema):
    """ OutTemplate - 
    """

    fields = {
        "CreateTime": fields.Int(required=False, dump_to="CreateTime", load_from="CreateTime"),
        "Template": fields.Str(required=False, dump_to="Template", load_from="Template"),
        "Attributes": fields.List(VariableAttr(), required=False, dump_to="Attributes", load_from="Attributes"),
        "ErrDesc": fields.Str(required=False, dump_to="ErrDesc", load_from="ErrDesc"),
        "Instruction": fields.Str(required=False, dump_to="Instruction", load_from="Instruction"),
        "Purpose": fields.Int(required=False, dump_to="Purpose", load_from="Purpose"),
        "Remark": fields.Str(required=False, dump_to="Remark", load_from="Remark"),
        "Status": fields.Int(required=False, dump_to="Status", load_from="Status"),
        "Tags": fields.List(fields.Int(required=False, dump_to="Tags", load_from="Tags")),
        "TemplateId": fields.Str(required=False, dump_to="TemplateId", load_from="TemplateId"),
        "TemplateName": fields.Str(required=False, dump_to="TemplateName", load_from="TemplateName"),
    }
