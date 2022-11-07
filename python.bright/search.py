

import re


text = "NIGERIA"
pattern= re.compile('^[A-Z0-9]+$') # $ mean end wit
rs= pattern.search(text)            #^mean starr with
                                     #\d mean digits
                                     #? mean one or none
                                     #* mean all

print(rs)