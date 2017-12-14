# -*- coding: utf-8 -*-

first_name = "gustaf"
last_name = "fridolin"
domain = "riksdagen.se"

"""
Tasks:
- Create a variable combining the name and the domain to create an email address.
- Print email address.
"""
email = first_name + "." + last_name + "@" + domain
print(email)
email = "%s%s@%s" % (first_name, last_name, domain)
print(email)
