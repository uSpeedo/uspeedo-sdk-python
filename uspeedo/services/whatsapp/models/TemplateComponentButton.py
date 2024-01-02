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


class TemplateComponentButton(schema.Schema):
    """ TemplateComponentButton - 
    """

    fields = {
        "PhoneNumber": fields.Str(required=False, dump_to="PhoneNumber", load_from="PhoneNumber"),
        "Text": fields.Str(required=False, dump_to="Text", load_from="Text"),
        "Type": fields.Str(required=False, dump_to="Type", load_from="Type"),
        "URL": fields.Str(required=False, dump_to="URL", load_from="URL"),
        "Example": fields.List(fields.Str(required=False, dump_to="Example", load_from="Example")),
    }
