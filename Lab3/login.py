#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

# Create login form and set cookie iff login correct:

# set up cgi form:
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# Check if correct login info provided to cgi form:
form_ok = username == secret.username and password == secret.password

# Set up cookie:
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

# Check if cookie username/password == secret username/password:
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# ... Then set username/password to cookie username/password:
if cookie_ok:
    username = cookie_username
    password = cookie_password

# from this point on, everything prints to html
print("Content-Type: text/html")
if form_ok:
    # Set cookie iff login info correct:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

# load relevant html pages:
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())