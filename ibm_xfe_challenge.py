# Author: Ashish Shah
# Date: Oct 2, 2017
# Python module for IBM X-Force Exchange API
# https://api.xforce.ibmcloud.com/doc/

from os import environ
from sys import argv
from json import dumps
from base64 import b64encode
from optparse import OptionParser

from requests import get

description_text = """Examples:

$ python python_challenge.py -i 8.8.8.8 -t R # returns the Report for the ip.
$ python python_challenge.py -i 8.8.8.8 -t H # returns the History for the ip.
$ python python_challenge.py -i 8.8.8.8 -t M # returns the Malware for the ip.
"""


def get_credential(name):
    return environ.get(name, "provide your credentials")


def create_header(key, password):
    b64Key = b64encode("{}:{}".format(key, password))
    return {
        'Authorization': "Basic {}".format(b64Key),
        'Accept': 'application/json'
    }


def api_request(api_url, headers):
    try:
        api_response = get(api_url, headers=headers, timeout=30)
    except Exception as e:
        print ("Exiting due to {}".format(e.message))
        exit()
    return api_response.json()


if __name__ == "__main__":

    parser = OptionParser(description=description_text)
    parser.add_option("-i", dest="ip", default=None, type=str,
                      help="Returns the IP report for the entered IP.",
                      metavar="ip-address")
    parser.add_option("-t", dest="type", default="r", type=str,
                      help="Report [R], History [H], or Malware [M]",
                      metavar="ip-address")
    options, _ = parser.parse_args()
    if len(argv[1:]) == 0:
        parser.print_help()

    options_type = str(options.type).lower()
    if options_type not in ['r', 'h', 'm']:
        print (parser.description)
        exit()

    type_actions = {
        'r': '/ipr/',
        'h': '/ipr/history/',
        'm': '/ipr/malware/'
    }

    headers = create_header(get_credential('API_KEY'), get_credential('API_PASSWORD'))
    base_url = "https://api.xforce.ibmcloud.com"
    api_url = "{}{}{}".format(base_url, type_actions[options_type], options.ip)
    api_response_data = api_request(api_url, headers)

    print (dumps(api_response_data, indent=4, sort_keys=True))
