print("Hello, world!")

r = open('/projects/r.txt', "r")
w = open('/projects/w.txt', "w")
list=[]
for i in r:
    print(i.strip())
    list.append(i.strip())    
    w.write(i.strip().upper()+"\n")
 
f='be' 
for i in list:
    if f in i: print("found %s in %s" % (f,i))
    
import sys
#sys.exit(0)
import subprocess
import re
a=['vmstat', '-t', '-n', '2']
vmstat=subprocess.Popen(args=a, stdout=subprocess.PIPE)
while vmstat.pid:
    print('vmstat',re.sub('^ +','',re.sub(' +', ' ', vmstat.stdout.readline().decode('ascii'))), end='')
