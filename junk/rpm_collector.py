#!/usr/bin/python

import os
import re

rpms=os.popen(('rpm -qa'))
pattern=re.compile(r"^Name\s+|^Install Date")

def main():

    for rpm in rpms:
        info=os.popen(('rpm -qi {}'.format(rpm))).read().splitlines()
        for i in [ i for i in (i.split(':',1) for i in info if re.search(pattern,i)) ]:
            try: print dict([[a.strip() for a in i]]) 
            except: pass

main()
