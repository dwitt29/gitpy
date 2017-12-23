#!/usr/bin/python

import os
import re
from datetime import datetime
import collections

def main():

    nameregex=re.compile("^Name\s+:\s+(.+)")
    versionregex=re.compile("^Version\s+:\s+(.+)")
    installregex=re.compile("^Install Date:\s+(.+)")
    info=os.popen(('rpm -qai {}')).read().splitlines()
    rpmname=''; rpminstall=''; rpmversion=''
    rpms={}
    for i in info:
        try: rpmname=re.match(nameregex,i).group(1)
        except: pass

        try: rpmversion=re.match(versionregex,i).group(1)
        except: pass

        try: 
            rpminstall=re.match(installregex,i).group(1)
            # eg. Sat 19 Nov 2016 09:44:13 PM EST
            dt=datetime.strptime(rpminstall,'%a %d %b %Y %I:%M:%S %p %Z' )
            rpms.update({rpmname:{'InstallDate':dt,'Version':rpmversion}})
            rpmname=''; rpminstall=''; rpmversion=''
        except: pass
    ordered=collections.OrderedDict(sorted(rpms.items(), key=lambda t: t[1]['InstallDate']))
    for k,v in ordered.iteritems(): print k,v
        
if __name__ == '__main__':
    main()
