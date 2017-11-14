import sys
#sys.exit(0)
import subprocess
import re
a=['vmstat', '-t', '-n', '2']
vmstat=subprocess.Popen(args=a, stdout=subprocess.PIPE)
while vmstat.pid:
    print('vmstat',re.sub('^ +','',re.sub(' +', ' ', vmstat.stdout.readline().decode('ascii'))), end='')
