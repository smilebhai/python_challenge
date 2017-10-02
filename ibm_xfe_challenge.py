# Author: Ashish Shah
# Date: Oct 2, 2017
# Python module for IBM X-Force Exchange API
# https://api.xforce.ibmcloud.com/doc/

from os import environ
from json import dumps
from base64 import b64encode
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from requests import get

description_text = """
Examples:

To return the IP report for the entered IP /ipr/{ip} :

    $ python ibm_xfe_challenge.py -i 1.2.3.4

To return the IP reputation history report for the entered IP /ipr/history{ip} :

    $ python ibm_xfe_challenge.py -i 1.2.3.4 -t H

To return the malware associated with the entered IP /ipr/malware/{ip} :

    $ python ibm_xfe_challenge.py -i 1.2.3.4 -t M

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


def main():
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            epilog=description_text)
    parser.add_argument("-i", dest="ip", default=None, type=str,
                        help="ip address", metavar="ipaddress")
    parser.add_argument("-t", dest="type", default="r", type=str,
                        help="Report [R] default, History [H], or Malware [M]",
                        metavar="type", choices=['r', 'h', 'm', 'R', 'H', 'M'])
    args = parser.parse_args()
    if args.ip is None:
        parser.print_help()
        exit()
 
    action_type = str(args.type).lower()
    type_actions = {
        'r': '/ipr/',
        'h': '/ipr/history/',
        'm': '/ipr/malware/'
    }
    headers = create_header(get_credential('API_KEY'), get_credential('API_PASSWORD'))
    base_url = "https://api.xforce.ibmcloud.com"
    api_url = "{}{}{}".format(base_url, type_actions[action_type], args.ip)
    api_response_data = api_request(api_url, headers)
    print (dumps(api_response_data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
