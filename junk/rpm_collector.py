#!/usr/bin/python

import os
import re
from datetime import datetime
import collections

def loginDB():
    import MySQLdb
    db=MySQLdb.connect('localhost', 'dave', 'test123', 'rpmdb')
    db.autocommit(False)
    return db

def commitDB(db):
    db.commit()

def logoutDB(db):
    db.commit()
    db.close()

def DropDBTable():

    sql='''
        drop table if exists rpminfo ;
     '''
    db=loginDB()
    curs=db.cursor()
    curs.execute(sql)
    commitDB(db)
    db.close()

def BuildDBTable():

    sql='''
        create table if not exists rpminfo 
        (
          rpm_name varchar(100),
          rpm_version varchar(50),
          rpm_installdate varchar(48)
        );
    '''
    db=loginDB()
    curs=db.cursor()
    curs.execute(sql)
    commitDB(db)
    db.close()

def InsertDBTable(db,name,version,installdate):

    sql='''
       insert into rpminfo 
       (rpm_name, rpm_version, rpm_installdate) 
        values('{}', '{}', '{}');
    '''.format(name,version,installdate)

    curs=db.cursor()
    curs.execute(sql)

def GatherRPMData():

    nameregex=re.compile("^Name\s+:\s+(.+)")
    versionregex=re.compile("^Version\s+:\s+(.+)")
    installregex=re.compile("^Install Date:\s+(.+)")
    info=os.popen(('rpm -qai {}')).read().splitlines()
    rpmname=''; rpminstall=''; rpmversion=''
    rpms={}
    db=loginDB()
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
            InsertDBTable(db=db,name=rpmname,version=rpmversion,installdate=dt)
            rpmname=''; rpminstall=''; rpmversion=''
        except: pass
    ordered=collections.OrderedDict(sorted(rpms.items(), key=lambda t: t[1]['InstallDate']))
    for k,v in ordered.iteritems(): print k,v
    logoutDB(db)        


def main():
    DropDBTable()
    BuildDBTable()
    GatherRPMData()

if __name__ == '__main__':
    main()
