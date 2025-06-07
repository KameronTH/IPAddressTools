# IPAddressTools
Author: Kameron Hall
Date Published: 

# Python Version
Python 3.11.2

## Description
The purpose of this module is to provide an easy way to obtain information about a public ip address. This may be useful for checking that your VPN client is functioning correctly. This project uses https://icanhazip.com/ to get the public ip address of the machine running this code, and http://ip-api.com/ to provide information on public ip addresses. Please review the Terms of Service and Privacy Policies of these services before using this script. 

## Requirements
### Third Party Packages
[requests==2.28.1](https://requests.readthedocs.io/)
### Python Standard Libraries
argparse \
typing

## (External Sites) Website APIs
https://icanhazip.com/ \
http://ip-api.com/

## Quickstart Guide
### 1. Get a public ip address. 
Public ip addresses are what websites use to identify your computer's network. The address is given from your Internet Search Provider (ISP). An easy way to get your own public ip address is via your router's configuration page or by requesting the information from a website. This module's get_current_public_ip() function recieves the public ip address of the running computer using the website, https://icanhazip.com/. 
### 2. Provide a public ip address to the get_public_ip_info() function. 
This function requests information about the public ip address using http://ip-api.com/. http://ip-api.com/ returns the ip address information as json. For documentation on the returned data, see their webpage.
### 3. (Optional) Use the prettify_public_info() function to make public ip information more human readable.
If you would like to see the public ip information in a more human readable way, you can pass the dictionary from get_public_ip_info() function to the prettify_public_info() function. This will return the information as a string with linebreaks for each key and value pair in the dictionary.
### 4. (Optional) Use provide_ip_info() to combine steps 2 and 3.
If you would like to either get a more human readable string or a dictionary output from http://ip-api.com/, you can use the provide_ip_info(), which accepts a public ip address and whether you want the output to be a human readable string or a dictionary.
### 5. (Optional) Use get_ip_info_from_command_line() function to get a simple command line tool.
If you want to get information on public ip addresses from the command line, call the get_ip_info_from_command_line() function in the body of the script and run the script from the command line, specify the public ip address with the flag [-p] for a human readable output. 
## Liscense
Apache License 2.0 (Apache-2.0)
## Disclaimers
Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

External Site Disclaimer. EXTERNAL SITES (websites that this program uses to obtain information from the Internet) are maintained by their respective parties. THE AUTHOR OF THIS PROGRAM HAS NO CONNECTION OR CONTROL OVER THE CONTENT HOSTED ON EXTERNAL SITES. USE OF THIS PROGRAM REQUIRES YOU TO REVIEW AND AGREE TO THE TERMS OF EXTERNAL SITES THAT PROVIDE SERVICES THAT THIS PROGRAM USES IN ITS FUNCTIONALITY. THE SERVICES OF THESE WEBSITES AND ACCESS TO THEIR APIS MAY CHANGE WITHOUT NOTICE AND MAY NEGATIVE IMPACT THE PERFORMANCE OF THIS PROGRAM. USE AT YOUR OWN RISK.