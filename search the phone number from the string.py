import re
Txt = """Dave Martin
6155557164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
8005555669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
5605555153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
9005559340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com
"""
for i in re.findall(r'\b[1-9]\d{9}\b', Txt):
    print("The phone number is "+i)