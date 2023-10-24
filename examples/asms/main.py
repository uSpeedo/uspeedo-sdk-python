import logging
import os

from uspeedo.client import Client
from uspeedo.core.exc import USpeedoException

logger = logging.getLogger("uspeedo")
logger.setLevel(logging.DEBUG)


def get_asms_client():
    client = Client(
        {
            "public_key": os.getenv("USPEEDO_PUBLIC_KEY"),
            "private_key": os.getenv("USPEEDO_PRIVATE_KEY"),
            "base_url": "https://api.uspeedo.com/api/"
        }
    )
    return client


def invoke_send_message():
    client = get_asms_client()

    req = {
        "TaskContent": [{
            "TemplateId": "UTAXXXXXXXXXXX",
            "SenderId": "uspeedo",
            "Target": [{
                "Phone": "(1)11111111",
                "TemplateParams": ["1111"]
            }]
        }]
    }
    try:
        response_json = client.asms().send_batch_usms_message(req)
        print(response_json)
    except USpeedoException as e:
        print(e)


def invoke_template_api():
    client = get_asms_client()

    try:
        create_template_req = {
            "Template": "Your verification code is {1}",
            "Purpose": 1,
            "Remark": "this is a test template",
            "TemplateName": "test template"
        }
        response_json = client.asms().create_usms_template(create_template_req)
        print(response_json)
    except USpeedoException as e:
        print(e)

    try:
        query_template_req = {
            "AccountId": "60000011",
            "TemplateId": ["UTA230227EL4IW1", "UTA230227JVIB02"],
        }
        response_json = client.asms().query_usms_template(query_template_req)
        print(response_json)
    except USpeedoException as e:
        print(e)

    try:
        update_template_req = {
            "TemplateId": "UTAXXXXXXXXXXX",
            "Template": "Your verification code is {1},thanks"
        }
        response_json = client.asms().update_usms_template(update_template_req)
        print(response_json)
    except USpeedoException as e:
        print(e)

    try:
        delete_template_req = {
            "TemplateIds": ["UTAXXXXXXXXXXX"],
        }
        response_json = client.asms().delete_usms_template(delete_template_req)
        print(response_json)
    except USpeedoException as e:
        print(e)


def main():
    # invoke_send_message()
    invoke_template_api()


if __name__ == '__main__':
    main()
