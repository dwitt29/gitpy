def BuildHash(qty):
    temphash=dict()
    for i in range(qty):
        for j in range(qty):
            v=i**3 + j**3
            if temphash.get(v):
                temphash[v].append((i,j))
            else:
                temphash[v]=list()
                temphash[v].append((i,j))
    return temphash
    
def Compare(qty):
    hash=BuildHash(qty)
    for a in range(qty):
        for b in range(qty):
            v=a**3 + b**3
            try:
                hash[v]
                print("Found : a,b={}, c,d={}".format((a,b), hash[v]))
            except:
                pass
        