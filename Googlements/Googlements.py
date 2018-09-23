#!/usr/bin/python

# https://code.google.com/codejam/contest/8304486/dashboard

class Googlement():
    def __init__(self,G):
        self.G=str(G)
        self.newG=''
        self.L=self.getL()
        self.Legal=self.Legal()
        self.PastG=[]
        if self.L > 9:
            import sys
            sys.exit(1)

    def PreviousGooglement(self):
        import itertools as I
        temp=[int(i) for i in self.G]  # convert current googlement into an list of ints
        if sum(temp) > len(temp): return False # sum < len if from a googlement
        Previous = [ str(i+1)*temp[i] for i in range(len(temp)) if temp[i] ] # find previous parent googlement
        del temp # clear earlier usage
        temp=I.permutations(''.join([ i for i in Previous if i ]),len(self.G)) # calc possibilities
        return [''.join(i) for i in temp]  # return possible googlements

    def NextGooglement(self):
        temp=[int(i) for i in self.G]
        Next=[ str(temp.count(i)) for i in range(1,self.L+1) ]
        return ''.join(decay)

    def addPastG(self):
        self.PastG.append(self.G)
        self.printPastG()

    def nextG(self):
        self.G=self.newG
        self.newG=''

    def printPastG(self):
        print self.PastG

    def Summary(self):
        return len(self.PastG)

    def Loop(self):
        return self.newG in self.PastG

    def valid(self):
        return range(self.L+1)

    def Legal(self):
        import re
        # digits only
        if not re.search('[1-9]+', self.G):
            return False

        # zero test
        if sum([int(i) for i in self.G]) == 0: return False
        # test digits used are less than length

        v=self.valid()
        illegal = [ i for i in self.G if int(i) not in v ]
        if illegal != []:
            return False
        else:
            return True

    def getL(self):
        return len(self.G)

def ReadCases():
    testdata=open('Googlements.txt')

    qty=int(testdata.readline().rstrip())

    cases=[]
    for i in range(qty):
        case=str(testdata.readline().rstrip().split()[0])
        cases.append(case)

    testdata.close()

    return cases
 
def main():
    cases=ReadCases()

    Gcases=[]
    for i in range(len(cases)):
        Gcases.append(Googlement(cases[i]))

    item=0
    for case in Gcases:
        item+=1
        if not case.Legal: continue
        case.addPastG()
        case.newG=case.Decay()
        while not case.Loop():
            case.nextG()
            case.addPastG()
            case.newG=case.Decay()
        print 'Case #{}: {}'.format(item,case.Summary())

if __name__ == '__main__':
    main()
