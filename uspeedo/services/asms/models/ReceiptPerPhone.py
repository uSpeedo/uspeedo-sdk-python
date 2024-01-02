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


class ReceiptPerPhone(schema.Schema):
    """ ReceiptPerPhone - 
    """

    fields = {
        "AccountId": fields.Int(required=False, dump_to="AccountId", load_from="AccountId"),
        "CostCount": fields.Int(required=False, dump_to="CostCount", load_from="CostCount"),
        "Phone": fields.Str(required=False, dump_to="Phone", load_from="Phone"),
        "ReceiptCode": fields.Str(required=False, dump_to="ReceiptCode", load_from="ReceiptCode"),
        "ReceiptDesc": fields.Str(required=False, dump_to="ReceiptDesc", load_from="ReceiptDesc"),
        "ReceiptResult": fields.Str(required=False, dump_to="ReceiptResult", load_from="ReceiptResult"),
        "ReceiptTime": fields.Int(required=False, dump_to="ReceiptTime", load_from="ReceiptTime"),
        "UserId": fields.Str(required=False, dump_to="UserId", load_from="UserId"),
    }
