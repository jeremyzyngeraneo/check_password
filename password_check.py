"""
password_check.py
This script checks if a given password is in a list of worst passwords.
"""


# install module : pip install requests
# import
import requests

# your password
user_password = input("Please enter the password to check : \n")

# Check if password is in the 500 worst passwords


def worst_500_passwords(password):
    # Download the Seclist
    print('Beginning check in 500 worst passwords')
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/'
    'master/Passwords/Common-Credentials/500-worst-passwords.txt'
    retrieve = requests.get(url, timeout=5)

    content = retrieve.content

    if str(password) in str(content):
        print("Your password is in the 500 worst passwords! change it !!!\n")
        exit(0)

# Check if password is in the 10k worst passwords


def worst_10k_passwords(password):
    print('Beginning check in 10k worst passwords')
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/'
    'master/Passwords/Common-Credentials/10k-most-common.txt'
    retrieve = requests.get(url, timeout=5)

    content = retrieve.content

    if str(password) in str(content):
        print("Your password is in the 10k worst passwords! change it !!!\n")
        exit(0)


worst_500_passwords(user_password)
worst_10k_passwords(user_password)
