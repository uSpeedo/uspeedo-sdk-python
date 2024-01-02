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
from uspeedo.services.asms.models.TargetPhone import TargetPhone


class SendInfo(schema.Schema):
    """ SendInfo - 
    """

    fields = {
        "SenderId": fields.Str(required=False, dump_to="SenderId", load_from="SenderId"),
        "Target": fields.List(TargetPhone(), required=False, dump_to="Target", load_from="Target"),
        "TemplateId": fields.Str(required=False, dump_to="TemplateId", load_from="TemplateId"),
    }
