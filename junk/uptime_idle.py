#/usr/bin/python

f=open('/proc/uptime', 'r')
line=f.readline()
up,idle=line.rstrip().split(' ')
print '%.6f ' % (float(idle)/float(up)*100)
f.close()
