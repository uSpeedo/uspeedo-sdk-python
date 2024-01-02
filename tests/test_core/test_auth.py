from uspeedo.core import auth


def test_verify_ac():
    d = {
        "Action": "CreateUSMSTemplate",
        "Purpose": 1,
        "Template": "your code is {1}",
        "AccountId": 60000011,
        "TemplateName": "demo",
    }
    cred = auth.Credential(
        "0dca1d51a9b3113c6f562acb0f813bce",
        "NTk1Mzk0MAItOWI0My10MGM4LTg0NmMMNDM0ZGM5Y2ZkMmNk",
    )
    assert cred.verify_ac(d) == "11a0430ae6f1a4dc0c656e64dfc1886b0ac4b63a"
    assert cred.to_dict() == {
        "public_key": "0dca1d51a9b3113c6f562acb0f813bce",
        "private_key": "NTk1Mzk0MAItOWI0My10MGM4LTg0NmMMNDM0ZGM5Y2ZkMmNk",
    }

    d = {
        "Action": "SendBatchUSMSMessage",
        "TaskContent": [{
            "TemplateId": "UTAXXXXXXXXXXX",
            "SenderId": "uspeedo",
            "Target": [{
                "Phone": "1111",
                "TemplateParams": ["1111"]
            }]
        }]
    }
    assert cred.verify_ac(d) == "7175ca50d6204dfd469e8aab447810c08f9da53f"
