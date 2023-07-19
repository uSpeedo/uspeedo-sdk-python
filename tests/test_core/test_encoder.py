import pytest

from uspeedo.core.typesystem import encoder


@pytest.mark.parametrize(
    "input_vector,expected",
    [
        ({"foo": "bar"}, {"foo": "bar"}),
        ({"foo": 42}, {"foo": "42"}),
        ({"foo": 42.42}, {"foo": "42.42"}),
        ({"foo": 42.0}, {"foo": "42"}),
        ({"foo": True}, {"foo": "true"}),
        ({"foo": False}, {"foo": "false"}),
    ],
)
def test_params_encode(input_vector, expected):
    result = encoder.encode(input_vector)
    assert result == expected
