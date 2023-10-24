from typing import List, Union

from uspeedo.core.utils.compat import str


def encode(d: dict) -> dict:
    result = {}

    for k, v in d.items():
        if isinstance(v, dict):
            for ek, ev in encode(v).items():
                result["{}.{}".format(k, ek)] = encode_value(ev)
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    for ek, ev in encode(item).items():
                        result["{}.{}.{}".format(k, i, ek)] = encode_value(ev)
                else:
                    result["{}.{}".format(k, i)] = encode_value(item)
        else:
            result[k] = encode_value(v)

    return result


def encode_value(v):
    if isinstance(v, (str, bool, int, float)):
        return simple2string(v)
    elif isinstance(v, list):
        return slice2string(v)
    elif isinstance(v, dict):
        return map2string(v)
    else:
        return str(v)


def simple2string(v: Union[str, bool, int, float]) -> str:
    if isinstance(v, bool):
        return str(v).lower()
    return str(v)


def slice2string(arr: List[Union[str, bool, int, float, dict]]) -> str:
    return ''.join([encode_value(v) for v in arr])


def map2string(params: dict) -> str:
    return ''.join([k + encode_value(params[k]) for k in extract_keys(params)])


def extract_keys(d: dict) -> List[str]:
    return sorted(d.keys())
