"""Check password"""
# install module : pip install requests

# imports
import sys

import requests
# your password
user_password = input("Please enter the password to check : \n")

# Check if password is in the 500 worst passwords


def worst_500_passwords(password):
    """
    Vérifie si le mot de passe se trouve parmi les 500 pires mots de passe.

    :param password: Le mot de passe de l'utilisateur à vérifier.
    :type password: str
    :return: Renvoie un message si le mot de passe figure parmi les 500 pires mots de passe.
    :rtype: None
    """
    # Download the Seclist
    print('Beginning check in 500 worst passwords')
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/'\
        'master/Passwords/Common-Credentials/500-worst-passwords.txt'
    retrieve = requests.get(url, timeout=5)

    content = retrieve.content

    if str(password) in str(content):
        print("Your password is in the 500 worst passwords! change it !!!\n")
        sys.exit(0)

# Check if password is in the 10k worst passwords


def worst_10k_passwords(password):
    """
    Vérifie si le mot de passe se trouve parmi les 10k pires mots de passe.

    :param password: Le mot de passe de l'utilisateur à vérifier.
    :type password: str
    :return: Renvoie un message si le mot de passe figure parmi les 10k pires mots de passe.
    :rtype: None
    """
    print('Beginning check in 10k worst passwords')
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/'\
        'master/Passwords/Common-Credentials/10k-most-common.txt'
    retrieve = requests.get(url, timeout=5)

    content = retrieve.content

    if str(password) in str(content):
        print("Your password is in the 10k worst passwords! change it !!!\n")
        sys.exit(0)


worst_500_passwords(user_password)
worst_10k_passwords(user_password)
