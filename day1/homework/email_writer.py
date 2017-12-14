# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Write a function that takes a name and a domain.
Transform the email's name to be compatible then print a complete email address.
"""

def emailify(name, domain):
    """
     The code does as follow:
     1) replace spaces with dots in the name.
     2) Convert all characters in lowercase
     3) Replace special characters (å, ä, ö, é) with characters that works in an e-mail.
     4) Print the complete address!
    """
    name = name.replace(" ", ".")
    name = name.lower()
    name = name.replace('å', 'a')
    name = name.replace('ä', 'a')
    name = name.replace('ö', 'o')
    name = name.replace('é', 'e')
    
    print ("%s@%s") % (name, domain)

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")
