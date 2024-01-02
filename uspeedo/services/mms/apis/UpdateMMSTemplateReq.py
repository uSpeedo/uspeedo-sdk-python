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


class UpdateMMSTemplateReq(schema.RequestSchema):

    """ UpdateMMSTemplateReq - 
    """

    fields = {
        "AccountId": fields.Int(required=True, dump_to="AccountId", load_from="AccountId"),
        "MediaType": fields.Str(required=False, dump_to="MediaType", load_from="MediaType"),
        "Subject": fields.Str(required=False, dump_to="Subject", load_from="Subject"),
        "TemplateId": fields.Str(required=True, dump_to="TemplateId", load_from="TemplateId"),
        "TemplateName": fields.Str(required=False, dump_to="TemplateName", load_from="TemplateName"),
        "Media": fields.Str(required=False, dump_to="Media", load_from="Media"),
        "Tags": fields.List(fields.Int(required=False, dump_to="Tags", load_from="Tags")),
        "Text": fields.Str(required=False, dump_to="Text", load_from="Text"),
        "VariableAttr": fields.Str(required=False, dump_to="VariableAttr", load_from="VariableAttr"),
    }
