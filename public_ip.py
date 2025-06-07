#!/bin/python
"""The purpose of this module is to quickly provide information on a public ip address. The module also includes a function to quickly obtain the public IP address of the running machine. 
This module uses https://icanhazip.com/ and http://ip-api.com to gather information on the public ip address."""
# This is the API to get info about public ips https://ip-api.com/docs/api:json
import requests
import argparse
from typing import Union


def get_current_public_ip() -> str:
    """Gets the current  public ip address of the machine. Uses icanhazip.com to get the public ip address."""
    ip_address_request = requests.get("https://icanhazip.com/")
    ip_address_request.raise_for_status()
    ip_address = ip_address_request.text.strip()
    return ip_address


def get_public_ip_info(ip_address: str) -> dict:
    """This function gets information regarding the location, timezone, and ip address of the public ip addres provided as input. This information is provided by ip-api.com."""
    info_api = f"http://ip-api.com/json/{ip_address}"
    returned_api_info = requests.get(info_api)
    # Always good to check that request was successful before attempting to extract data from the object.
    returned_api_info.raise_for_status()

    # If there are no errors, ip-api returns json for a query.
    returned_api_info = returned_api_info.json()
    return returned_api_info


def prettify_public_info(public_ip_info: dict) -> str:
    """This function accepts the dictionary from get_public_ip_info() and converts it to a more readable string."""
    list_of_info = []

    for key, value in public_ip_info.items():
        # This formats the string before putting it into a list, which will be inserted into the empty string.
        list_of_info.extend([str(key.title()) + ": ", str(value) + "\n"])

    return "".join(list_of_info)


def provide_ip_info(public_ip:str, prettify:bool=False) -> Union[str | dict]:
    """This function provides the public ip address info in its dictionary or pretty string format based on boolean flag."""
    json_ip_info = get_public_ip_info(public_ip)
    if prettify:
        return prettify_public_info(json_ip_info)
    else:
        return json_ip_info

def get_ip_info_from_command_line():
    """Allows the program to be used as a command line tool."""
    arg_parser = argparse.ArgumentParser(
        description="Provides information about your public ip address using ip-api.com."
    )

    arg_parser.add_argument("public_ip_address", type=str)
    # store_true action stores False, until the flag is provided. This is more expected than the argument being None if the flag is not provided.
    arg_parser.add_argument("-p", "--pretty", action="store_true")

    parsed_stdin = arg_parser.parse_args()

    print(provide_ip_info(parsed_stdin.public_ip_address, parsed_stdin.pretty))


if __name__ == "__main__":
    get_ip_info_from_command_line()
    