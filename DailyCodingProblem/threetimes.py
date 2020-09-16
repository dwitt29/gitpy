
# Daily Coding Problem: Problem #549 [Hard] Sept 14, 2020

a = [ 13,19,13,13 ]
print(a)
onlyone=list()
hash=dict()

for i in a:
    #print(i)
    if not i in hash:
        hash[i]=1
        onlyone.append(i)
        #print('adding {} to onlyone[]={}'.format(i, onlyone))
    else:
        try:
            onlyone.remove(i)
            #print('removing {} to onlyone[]={}'.format(i, onlyone))
        except:
            pass

print(onlyone)

