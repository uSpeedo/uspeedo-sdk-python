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


class CreateUSMSTemplateReq(schema.RequestSchema):

    """ CreateUSMSTemplateReq - 
    """

    fields = {
        "Remark": fields.Str(required=False, dump_to="Remark", load_from="Remark"),
        "Template": fields.Str(required=True, dump_to="Template", load_from="Template"),
        "TemplateName": fields.Str(required=True, dump_to="TemplateName", load_from="TemplateName"),
        "AccountId": fields.Int(required=False, dump_to="AccountId", load_from="AccountId"),
        "Purpose": fields.Int(required=True, dump_to="Purpose", load_from="Purpose"),
    }
