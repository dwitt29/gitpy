#!/usr/bin/python

class Googlement():
    def __init__(self,G):
        self.G=str(G)
        self.L=self.getL()
        self.Legal=self.Legal()
        if self.L > 9:
            import sys
            sys.exit(1)

    def Decay(self):
        pass

    def Loop(self):
        pass

    def Legal(self):
        illegal=[]
        illegal = [ i for i in self.G if int(i) > self.L ]
        if illegal != []:
            return False

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

if __name__ == '__main__':
    main()




