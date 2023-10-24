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
from uspeedo.services.asms.models.TargetPhoneWithFailure import TargetPhoneWithFailure


class SendInfoWithFailure(schema.Schema):
    """ SendInfoWithFailure - 
    """

    fields = {
        "TemplateId": fields.Str(required=False, dump_to="TemplateId", load_from="TemplateId"),
        "FailureDetails": fields.Str(required=False, dump_to="FailureDetails", load_from="FailureDetails"),
        "SenderId": fields.Str(required=False, dump_to="SenderId", load_from="SenderId"),
        "Target": fields.List(TargetPhoneWithFailure(), required=False, dump_to="Target", load_from="Target"),
    }
