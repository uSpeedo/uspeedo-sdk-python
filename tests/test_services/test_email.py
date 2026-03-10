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

import os
import pytest

from uspeedo.services.email.apis.SendEmailTemplateReq import SendEmailTemplateReq
from uspeedo.services.email.client import EmailClient


def _build_minimal_req():
    """Build minimal request (without Subject/Abstract)"""
    return {
        "TemplateId": "UETXXXXXXXXXXX",
        "SendEmail": "examples@examples.com",
        "EmailContent": [
            {
                "EmailAddress": "example@examples.com",
                "TemplateVariableParams": ["variableName{##}variableValue"],
            }
        ],
    }


def test_send_email_template_dumps_without_optional_fields():
    """When Subject/Abstract are not passed, dumps result excludes these fields for backward compatibility"""
    req = SendEmailTemplateReq().dumps(_build_minimal_req())
    assert "TemplateId" in req
    assert "SendEmail" in req
    assert "EmailContent" in req
    assert "Subject" not in req
    assert "Abstract" not in req


def test_send_email_template_dumps_with_optional_fields():
    """When Subject/Abstract are passed, dumps result correctly includes them"""
    d = _build_minimal_req()
    d["Subject"] = "Custom email subject"
    d["Abstract"] = "Email abstract content"
    req = SendEmailTemplateReq().dumps(d)
    assert req["Subject"] == "Custom email subject"
    assert req["Abstract"] == "Email abstract content"


@pytest.mark.skipif(
    not os.getenv("USpeedo_PUBLIC_KEY") or not os.getenv("USpeedo_PRIVATE_KEY"),
    reason="Skip: USpeedo_PUBLIC_KEY or USpeedo_PRIVATE_KEY not set",
)
def test_send_email_template_integration():
    """Real API call, requires USpeedo_PUBLIC_KEY and USpeedo_PRIVATE_KEY env vars"""
    config = {
        "public_key": os.getenv("USpeedo_PUBLIC_KEY"),
        "private_key": os.getenv("USpeedo_PRIVATE_KEY"),
    }
    client = EmailClient(config)

    req = _build_minimal_req()
    req["Subject"] = "Integration test subject"
    req["Abstract"] = "Integration test abstract"

    resp = client.send_email_template(req)

    assert resp is not None
