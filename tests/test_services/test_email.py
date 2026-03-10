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
    """最小请求构造（不含 Subject/Abstract）"""
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
    """不传 Subject/Abstract 时 dumps 结果不包含这两个字段，兼容历史版本"""
    req = SendEmailTemplateReq().dumps(_build_minimal_req())
    assert "TemplateId" in req
    assert "SendEmail" in req
    assert "EmailContent" in req
    assert "Subject" not in req
    assert "Abstract" not in req


def test_send_email_template_dumps_with_optional_fields():
    """传入 Subject/Abstract 时 dumps 结果正确包含"""
    d = _build_minimal_req()
    d["Subject"] = "自定义邮件主题"
    d["Abstract"] = "邮件摘要内容"
    req = SendEmailTemplateReq().dumps(d)
    assert req["Subject"] == "自定义邮件主题"
    assert req["Abstract"] == "邮件摘要内容"


@pytest.mark.skipif(
    not os.getenv("USpeedo_PUBLIC_KEY") or not os.getenv("USpeedo_PRIVATE_KEY"),
    reason="Skip: USpeedo_PUBLIC_KEY or USpeedo_PRIVATE_KEY not set",
)
def test_send_email_template_integration():
    """真实 API 调用，需设置环境变量 USpeedo_PUBLIC_KEY、USpeedo_PRIVATE_KEY"""
    config = {
        "public_key": os.getenv("USpeedo_PUBLIC_KEY"),
        "private_key": os.getenv("USpeedo_PRIVATE_KEY"),
    }
    client = EmailClient(config)

    req = _build_minimal_req()
    req["Subject"] = "集成测试主题"
    req["Abstract"] = "集成测试摘要"

    resp = client.send_email_template(req)

    assert resp is not None
