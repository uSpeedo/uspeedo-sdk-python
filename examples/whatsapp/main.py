import os
import logging

from uspeedo.client import Client

logger = logging.getLogger("uspeedo")
logger.setLevel(logging.DEBUG)


def main():
    client = Client(
        {
            "public_key": os.getenv("USPEEDO_PUBLIC_KEY"),
            "private_key": os.getenv("USPEEDO_PRIVATE_KEY"),
            "base_url": "https://api.uspeedo.com/api/"
        }
    )

    resp = client.whatsapp().get_message_summary({})
    print(resp)


if __name__ == '__main__':
    main()
