def MakePermu(src):
    from itertools import permutations
    return dict((''.join((e)),1) for e in permutations(src)) 
    
def CompareStr(src,dest):
    import sys
    if src == '' or dest == '':
        print("Empty String received...EXIT")
        sys.exit(1)
    srclen=len(src)
    hash=MakePermu(src)
    for i in range(len(dest)-srclen+1):
        chkme=dest[i:i+srclen]
        try:
            hash[chkme]
            print("Found ",chkme)
        except:
            pass   