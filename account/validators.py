import re

def isEmail(email) : 
    regex = re.compile('^([a-zA-Z0-9\.\_-])+\@([a-zA-Z0-9\.\_-])+\.([a-zA-Z0-9]{2,4})$')
    return re.match(regex, email)

def isUserName(username) : 
    regex = re.compile('^([a-zA-Z0-9\_]{8,})$')
    return re.match(regex, username)