class MergeSort():
    def __init__(self, a1, a2):
        self.a1=list(a1)
        self.a2=list(a2)
        self.a1.sort()
        self.a2.sort()

    def doMerge(self):
        len1=len(self.a1)
        len2=len(self.a2)
        ind1=ind2=0
        merged=list()
        compares=0
        while (ind1<len1 and ind2<len2):
            if self.a1[ind1] == self.a2[ind2]:
                merged.append(self.a1[ind1])
                merged.append(self.a2[ind2])
                ind1+=1; ind2+=1; compares+=1
            elif self.a1[ind1] < self.a2[ind2]:
                merged.append(self.a1[ind1])
                ind1+=1 ; compares+=2
            else: 
                merged.append(self.a2[ind2])
                ind2+=1 ; compares+=3

        # if any array remnants
        if ind1 < len1:
            for i in range(ind1,len1):
                merged.append(self.a1[i])
                compares+=1
        elif ind2 < len2:
            for i in range(ind2,len2):
                merged.append(self.a2[i])
                compares+=2
       
        return merged,compares
