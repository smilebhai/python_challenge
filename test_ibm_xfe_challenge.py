from base64 import b64encode

from ibm_xfe_challenge import *


def test_create_header():
    base64_value = b64encode("{}:{}".format("THE-KEY", "THE-PASSWORD"))
    expected_result = {
        'Authorization': "Basic {}".format(base64_value),
        'Accept': 'application/json'
    }
    
    assert expected_result == create_header("THE-KEY", "THE-PASSWORD")
