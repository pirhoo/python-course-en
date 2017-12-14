# -*- coding: utf-8 -*-

name = "Stefan Löfven"
name = name.lower()
name = name.replace(" ", ".").replace("ö", "o")
domain = "riksdagen.se"

"""
Task:
- Use .replace() to replace all spaces with dots and the "ö" by a "o" in the name.
- Use .lower() to transform to lower case.
"""

email = ("%s@%s") % (name, domain)
print(email)
