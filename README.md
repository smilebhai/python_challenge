# IBM X-Force Python Module

Given an IP adddress, this module queries the [IBM X-Force Exchange API](https://api.xforce.ibmcloud.com/doc/) and prints out the returning data.

## Setup

### Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python.

	$ pip install -r requirements.txt

### API Credentials

You must have an IBM ID to use the XFE API. Register for an IBM ID at [IBM id registration](https://www.ibm.com/account/profile/us?page=reg). 

Credentials are stored as environment variables (API_KEY, API_PASSWORD). Please see .env.sample

## Usage

```
usage: ibm_xfe_challenge.py [-h] [-i ipaddress] [-t type]

optional arguments:
  -h, --help    show this help message and exit
  -i ipaddress  ip address
  -t type       Report [R] default, History [H], or Malware [M]

Examples:

To return the IP report for the entered IP /ipr/{ip} :

    $ python python_challenge.py -i 1.2.3.4

To return the IP reputation history report for the entered IP /ipr/history{ip} :

    $ python python_challenge.py -i 1.2.3.4 -t H

To return the malware associated with the entered IP /ipr/malware/{ip} :

    $ python python_challenge.py -i 1.2.3.4 -t M
```

## Test

	$ pytest
