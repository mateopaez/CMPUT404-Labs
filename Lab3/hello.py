#!/usr/bin/env python3
import os, json

# Printing out all variables as plain text:

# print("Content-Type: text/plain")  # Let browser know to expect plain text
# print()
# print(os.environ)

# Printing out env variables as josn:
# print("Content-Type: application/json")  # Let browser know to expect json
# print()
# print(json.dumps(dict(os.environ), indent=2)) # Print with nice formatting

# Printing query parameter data in HTML:
# print("Content-Type: text/html")  # Let browser know to expect html
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}<\p>")

# Printing user's browser in html:
print("Content-Type: text/html")  # Let browser know to expect html
print()
print(f"<p>QUERY_STRING={os.environ['HTTP_USER_AGENT']}<\p>")