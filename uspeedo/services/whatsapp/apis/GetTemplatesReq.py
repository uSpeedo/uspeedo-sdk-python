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


class GetTemplatesReq(schema.RequestSchema):

    """ GetTemplatesReq - 
    """

    fields = {
        "After": fields.Str(required=False, dump_to="After", load_from="After"),
        "Before": fields.Str(required=False, dump_to="Before", load_from="Before"),
        "BusinessPhone": fields.Str(required=True, dump_to="BusinessPhone", load_from="BusinessPhone"),
        "Limit": fields.Int(required=False, dump_to="Limit", load_from="Limit"),
        "Name": fields.Str(required=False, dump_to="Name", load_from="Name"),
    }
