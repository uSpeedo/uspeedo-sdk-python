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
from uspeedo.services.whatsapp.models.Console__Cursors import Console__Cursors


class Console__Paging(schema.Schema):
    """ Console__Paging - 
    """

    fields = {
        "cursors":  Console__Cursors(required=False, dump_to="cursors", load_from="cursors"),
        "next": fields.Str(required=False, dump_to="next", load_from="next"),
        "previous": fields.Str(required=False, dump_to="previous", load_from="previous"),
    }
